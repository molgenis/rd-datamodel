#'////////////////////////////////////////////////////////////////////////////
#' FILE: index.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-10-19
#' MODIFIED: 2022-05-04
#' PURPOSE: compile and build EMX files
#' STATUS: stabe
#' PACKAGES: yamlemxconvert
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

from rd_datamodel.utils.emxtools import buildEmxTags
import yamlemxconvert
import yaml

# load emx config
with open('model.yaml', 'r') as stream:
    config=yaml.safe_load(stream)
    stream.close()

# for all models listed in the configuration file, build EMX1 and EMX2
# versions of the model
for model in config['models']:
    if model['active']:
        print('Building EMX Model:',model['name'])
        m = yamlemxconvert.Convert(files=model['files'])
        m.convert()
        
        tags=m.tags
        tags.extend(buildEmxTags(m.packages))
        tags.extend(buildEmxTags(m.entities))
        tags.extend(buildEmxTags(m.attributes))
        tags=list({ tag['identifier']: tag for tag in tags }.values() )
        m.tags=sorted(tags, key=lambda d:d['identifier'])
        
        m.write(model['name'], format='xlsx',outDir=config['outputPaths']['main'])
        m.write_schema(path=f"{config['outputPaths']['schemas']}/{model['name']}_schema.md")
        
        if model['name'] != 'umdm':
            for file in model['files']:
                print('Generating EMX2 Version')
                m2=yamlemxconvert.Convert2(file=file)
                m2.convert()
                m2.write(
                    name=f"{model['name']}_emx2",
                    outDir=config['outputPaths']['main']
                )


# ~ 2 ~
# Build EMX2 Version
# 
# Since the release of yamlemxconvert v1.0, the UMDM can be built for EMX2
# databases. It is recommended to convert the model and apply transformations
# using python (rather than editing the Excel file) until the EMX2 version of 
# the model becomes permanent. For now, this method is reproducible.
#
# For the implementation of the UMDM into real databases, I have decided to
# serparate the lookups into a new EMX2 schema so that it can act as a shared
# schema for other schemas.

umdm2 = yamlemxconvert.Convert2(file='model/umdm.yaml')
umdm2.convert()

# convert lookups as an EMX2 schema
umdmRefs2 = yamlemxconvert.Convert2(file='model/umdm_lookups.yaml')
umdmRefs2.convert()


# In the UMDM model, set the refSchema for all lookups that are defined in the
# lookups EMX model
tableNames = [x.get('tableName') for x in umdmRefs2.model.get('molgenis')]

for m in umdm2.model.get('molgenis'):
    if m.get('refTable') in tableNames:
        m['refSchema'] = 'umdmRefs'
        
# # write models
umdm2.write(name = 'umdm_emx2', format = 'xlsx', outDir = 'dist/')
umdmRefs2.write(name = 'umdm_emx2_refs', format = 'xlsx', outDir = 'dist/')
