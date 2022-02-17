#'////////////////////////////////////////////////////////////////////////////
#' FILE: index.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-10-19
#' MODIFIED: 2022-02-17
#' PURPOSE: compile and build EMX files
#' STATUS: stabe
#' PACKAGES: yamlemxconvert
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

# pip install yamlemxconvert
import yamlemxconvert
from os import path
import re

def __emptyEmxTagTemplate__():
    """Empty Emx Tag Template
    Generate a blank dict for tag metadata
    """
    return {
        'identifier': None,
        'label': None,
        'objectIRI': None,
        'codeSystem': None,
        'relationLabel': 'isAssociatedWith',
        'relationIRI': 'http://molgenis.org#isAssociatedWith'
    }

def buildEmxTags(attributes: list = []):
    """Build Emx Tags
    At the attribute level, collate all tags from the `tags` property and
    transform into EMX format.
    @param attributes (list) : the post-converted emx object `attributes` 
    """
    rawTags = []
    for attr in attributes:
        if 'tags' in attr:
                if attr['tags'].split(','):
                    for t in attr['tags'].split(','):
                        rawTags.append(t.strip())
                else:
                    rawTags.append(attr['tags'])
    
    data = []
    tags = list(set(rawTags))
    
    # set known tags that do not follow the default
    # pattern: [a-zA-Z]{1,}_[a-zA-Z0-9]{1,}
    knownDcmiTags = ['http://purl.org/dc/terms/valid']
    knownW3Tags = ['https://w3id.org/reproduceme#wasUpdatedBy']
    knownDcatTags = {
        'https://www.w3.org/TR/vocab-dcat-3/#Property:catalog_dataset' : {
            'label': 'dcat:Dataset' 
        },
        'https://www.w3.org/TR/vocab-dcat-3/#Class:Catalog': {
            'label': 'dcat:Catalog' 
        }
    }
    
    for tag in tags:
        if bool(tag):
            d = __emptyEmxTagTemplate__()
            name = path.basename(tag)
            
            # codes that are split with a forward slash rather than a hyphen
            knownIriVariations = re.search(r'(/(HL7|SNOMEDCT|MESH)/)', tag)
            if knownIriVariations:
                d['identifier'] = tag
                d['label'] = f"{knownIriVariations.group().replace('/','')}:{name}"
                d['codeSystem'] = knownIriVariations.group().replace('/','')
            
            # for other Iri variations
            elif re.search(r'^([a-zA-Z]{1,}#[a-zA-Z]{1,}_[a-zA-Z0-9]{1,})', name):
                d['identifier'] = tag
                d['label'] = name.split('#')[1].replace('_',':')
                d['codeSystem'] = name.split('#')[1].split('_')[0]
                
            # process DCMI tags manually
            elif tag in knownDcmiTags:
                d['identifier'] = tag
                d['label'] = f'DCMI:{name}'
                d['codeSystem'] = 'DCMI'
                
            # tags from w3id.org
            elif tag in knownW3Tags:  
                d['identifier'] = tag
                d['label'] = f"W3ID:{name.split('#')[1]}"
                d['codeSystem'] = 'W3ID'
        
            # dcat tags
            elif tag in knownDcatTags:
                d['identifier'] = tag
                d['label'] = knownDcatTags[tag]['label']
                d['codeSystem'] = 'DCAT'
                
            # set EDAM
            elif re.search(r'^(data_)', name):
                d['identifier'] = tag
                d['codeSystem'] = 'EDAM'

            # default formats
            elif re.search(r'^([a-zA-Z]{1,}_[a-zA-Z0-9]{1,})$', name):
                d['identifier'] = tag
            
            else:
                print(f"Unable to process tag: {d['identifier']}")
                                
            if bool(d['identifier']):
                d['objectIRI'] = tag
                if not bool(d['label']):
                    d['label'] = name.replace('_', ':')
                if not bool(d['codeSystem']): 
                    d['codeSystem'] = name.split('_')[0]
                data.append(d)
    return data

#//////////////////////////////////////

# ~ 1 ~
# BUILD EMX1 MODEL
# render model for EMX v1 Molgenis instances

# build: main data model
umdm = yamlemxconvert.Convert(
    files = [
        'src/emx-umdm/umdm_emx1.yaml',
        'src/emx-umdm/umdm_lookups_emx1.yaml'
    ]
)

umdm.convert()

# rebuild build tags
builtTags = umdm.tags
builtTags.extend(buildEmxTags(umdm.packages))
builtTags.extend(buildEmxTags(umdm.entities))
builtTags.extend(buildEmxTags(umdm.attributes))
builtTags = list({d['identifier']: d for d in builtTags}.values())
umdm.tags = sorted(builtTags, key = lambda d: d['identifier'])

umdm.write('umdm', format = 'xlsx', outDir = 'dist/umdm-emx1/')
umdm.write_schema('dist/umdm_schema.md')

# ~ a ~
# build: user management module
# usersModule = yamlemxconvert.Convert(files = ['emx/src/module_approved_users.yaml'])
# usersModule.convert()
# usersModule.write('users', format = 'xlsx', outDir = 'emx/dist/')
# usersModule.write_schema('emx/schemas/users_module_schema.md')

# ~ b ~
# build: jobs module
# jobsModule = yamlemxconvert.Convert(
#     files = [
#         'emx/src/module_jobs.yaml',
#         'emx/src/module_jobs_results.yaml'
#     ]
# )
# jobsModule.convert()
# jobsModule.write('jobs', format = 'xlsx', outDir = 'emx/dist')
# jobsModule.write_schema('emx/schemas/jobs_module_schema.md')


#?/////////////////////////////////////////////////////////////////////////////

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

# import the convert2 and convert
# from yamlemxconvert import Convert2

# umdm2 = Convert2(file = 'src/emx-umdm/umdm_emx1.yaml')
# umdm2.convert()

# # convert lookups as an EMX2 schema
# umdmRefs2 = Convert2(file = 'src/emx-umdm/umdm_lookups_emx1.yaml')
# umdmRefs2.convert()


# # In the UMDM model, set the refSchema for all lookups that are defined in the
# # lookups EMX model
# tableNames = [x.get('tableName') for x in umdmRefs2.model.get('molgenis')]

# for m in umdm2.model.get('molgenis'):
#     if m.get('refTable') in tableNames:
#         m['refSchema'] = 'umdmRefs'
        
# # write models
# umdm2.write(name = 'umdm2', format = 'xlsx', outDir = 'dist/')
# umdmRefs2.write(name = 'umdm2_refs', format = 'xlsx', outDir = 'dist/')