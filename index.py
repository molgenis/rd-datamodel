#//////////////////////////////////////////////////////////////////////////////
# FILE: index.py
# AUTHOR: David Ruvolo
# CREATED: 2021-10-19
# MODIFIED: 2022-09-05
# PURPOSE: compile and build EMX files
# STATUS: stabe
# PACKAGES: yamlemxconvert
# COMMENTS: NA
#//////////////////////////////////////////////////////////////////////////////

from clize import run
# from rd_datamodel.utils.emxtools import buildEmxTags, extractTagId
from yamlemxconvert.convert import Convert
from yamlemxconvert.convert2 import Convert2
import yaml
import re

# pathToProfile='profiles/cosas.yaml'

# emx2 = yamlemxconvert.Convert2(file='model/umdm.yaml')
# emx2.convert(flattenNestedPkgs=False)


def buildModel(pathToProfile):
  """Build Emx Model
  Build an EMX data model based on a yaml-profile.
  
  :profile pathToProfile: location of the yaml-profile file
  """
  with open(pathToProfile, 'r') as file:
    profile=yaml.safe_load(file)
    file.close()
    del file
      
  if 'buildOptions' not in profile:
    raise KeyError('No build options defined')
      
  # build emx1 version with options
  emx1options=profile['buildOptions']['emx1']
  if emx1options['active']:
    emx1 = Convert(files=profile['modelFilePath'])
    emx1.convert()
    
    emx1.compileSemanticTags()
    # tags=emx1.tags
    # tags.extend(buildEmxTags(emx1.packages))
    # tags.extend(buildEmxTags(emx1.entities))
    # tags.extend(buildEmxTags(emx1.attributes))
    # emx1.tags=tags
        
    # extractTagId(emx1.packages)
    # extractTagId(emx1.entities)
    # extractTagId(emx1.attributes)
        
    pkgMetaDescription = {
      '<version>': f"(v{emx1.version})" if emx1.version else None,
      '<date>': f"({emx1.date})" if emx1.date else None,
      '<version:date>': f"(v{emx1.version}, {emx1.date})" if emx1.version and emx1.date else None,
      '<date:version>': f"({emx1.date}, v{emx1.version})" if emx1.version and emx1.date else None
    }
        
    # override package-level labels
    if profile.get('setEmxLabels'):
      newPackageLabels=profile['setEmxLabels']
      if newPackageLabels.get('setUmdmLabel'):
        emx1.packages[0]['label']=newPackageLabels['setUmdmLabel']
            
      # rebuild description and replace <version:date> variations
      if newPackageLabels.get('setUmdmDescription'):
        newDescription=newPackageLabels['setUmdmDescription']
        pkgMetaPatterns = '|'.join(pkgMetaDescription.keys())
        hasModelMetadata = re.search(re.compile(pkgMetaPatterns), newDescription)
        if hasModelMetadata:
          emx1.packages[0]['description']=re.sub(
            pattern=hasModelMetadata.group(),
            repl=pkgMetaDescription[hasModelMetadata.group()],
            string=newDescription
          )
      if newPackageLabels.get('setLookupsLabel'):
        emx1.packages[1]['label']=newPackageLabels['setLookupsLabel']
    
    # override labels
    if emx1options.get('overrideLabels'):
      # override entity labels
      for table in profile['overrideEmxAttributes']:
        tableOverrides=profile['overrideEmxAttributes'][table]
            
        # rename entity label
        if tableOverrides.get('overrideTableLabelWith'):
          for row in emx1.entities:
            if row['name']== table:
              row['label']=tableOverrides['overrideTableLabelWith']
                        
        # rename attribute labels
        if tableOverrides.get('attributeLabelsToOverride'):
          newLabels=tableOverrides.get('attributeLabelsToOverride')
          for row in emx1.attributes:
            for label in newLabels.keys():
              if (row['entity']==f"umdm_{table}") and (row['name']==label):
                row['label']=newLabels[label]    
    
    
    # override visibility: hide attributes if defined
    if emx1options.get('overrideVisibility'): 
      globalHiddenAttribs=profile['overrideEmxAttributes'].get('_all',{}).get('attributesToHide')
      for row in emx1.attributes:
        # hide if in global definitions
        if row['name'] in globalHiddenAttribs:
          row['visible']=False
                
        # hide in table definitions
        tableName=row['entity'].split('_')[1]
        if tableName in profile['overrideEmxAttributes']:
          tableOverrides=profile['overrideEmxAttributes'][tableName]
          if 'attributesToHide' in tableOverrides:
            tableAttribsToHide=tableOverrides['attributesToHide']
            if row['name'] in tableAttribsToHide:
              row['visible']=False

    emx1.write(name=profile['name'], outDir=emx1options['outputDir'])
    emx1.write_schema(path=f"{emx1options['schemasDir']}/{profile['name']}_schema.md")
        
  # build emx2 version with options
  emx2options=profile['buildOptions']['emx2']
  if emx2options['active']:
    for model in profile['modelFilePath']:
      emx2=Convert2(file=model)
      emx2.convert(keepModelPackage=True)
      
      # rename refSchema
      if emx2options.get('splitLookups'):
        schemaOptions=profile['overrideEmxAttributes']['_all']['renameRefEntityToSchema']
        for row in emx2.model['molgenis']:
          
          # change refScheme for splitting nested EMX1 packages
          if row.get('refSchema'):
            if schemaOptions['currentName'] == row['refSchema']:
              row['refSchema']=schemaOptions['newName']
            if row['refSchema'] == emx2.name:
              row['refSchema'] = None
          
          # format semantic tags
          if row.get('semantics'):
            tag = row.get('semantics')
            search = re.search(r'^([0-9a-zA-Z]{1,}([:_])[0-9a-zA-Z]{1,}\s+([a-zA-Z0-9.]{1,}))', tag)
            if search:
              newtag = re.split(r'\s+', tag)[1]
              row['semantics'] = newtag
      
      # bind extra emx2 definitions
      if profile.get('additionalRecordsForEmx2'):
        emxExtensions = profile.get('additionalRecordsForEmx2')
        
        # bring over extension key names to model
        for row in emx2.model['molgenis']:
          if 'refBack' not in row:
            row['refBack'] = None
        
        # bring over model key names to emx extensions
        for row in emxExtensions:
          for key in emx2.model['molgenis'][0].keys():
            if key not in row:
              row[key] = None
        
        # append extensions to model
        emx2.model['molgenis'].extend(emxExtensions)

      emx2_model_name=emx2.filename.replace('.yaml','_emx2')
      emx2.write(name=emx2_model_name, outDir='dist/')
      
if __name__ == '__main__':
  run(buildModel)
