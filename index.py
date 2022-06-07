#'////////////////////////////////////////////////////////////////////////////
#' FILE: index.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-10-19
#' MODIFIED: 2022-06-07
#' PURPOSE: compile and build EMX files
#' STATUS: stabe
#' PACKAGES: yamlemxconvert
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

from clize import run
from rd_datamodel.utils.emxtools import (
    buildEmxTags,
    extractTagId,
    recodePackageVersionDateString
)
import yamlemxconvert
import yaml
import re

# pathToProfile='profiles/cosas.yaml'

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
        emx1 = yamlemxconvert.Convert(files=profile['modelFilePath'])
        emx1.convert()
        
        tags=emx1.tags
        tags.extend(buildEmxTags(emx1.packages))
        tags.extend(buildEmxTags(emx1.entities))
        tags.extend(buildEmxTags(emx1.attributes))
        emx1.tags=tags
        
        extractTagId(emx1.packages)
        extractTagId(emx1.entities)
        extractTagId(emx1.attributes)
        
        # override package-level labels
        if profile.get('setEmxLabels'):
            newPackageLabels=profile['setEmxLabels']
            if newPackageLabels.get('setUmdmLabel'):
                emx1.packages[0]['label']=newPackageLabels['setUmdmLabel']
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
        emx2=yamlemxconvert.Convert2(file=profile['modelFilePath'])
        emx2.convert()
        
        # rename refSchema
        if emx2options.get('splitLookups'):
            schemaOptions=profile['overrideEmxAttributes']['_all']['renameRefEntityToSchema']
            for row in emx2.model['molgenis']:
                if row.get('refTable'):
                    if schemaOptions['currentName'] in row['refTable']:
                        row['refTable']=schemaOptions['newName']
     


if __name__ == '__main__':
    run(buildModel)
