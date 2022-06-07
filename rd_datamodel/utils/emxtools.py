#'////////////////////////////////////////////////////////////////////////////
#' FILE: emxtools.py
#' AUTHOR: David Ruvolo
#' CREATED: 2022-05-04
#' MODIFIED: 2022-06-07
#' PURPOSE: misc functions to help build a yaml-emx model
#' STATUS: stable
#' PACKAGES: NA
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

import re

def buildEmxTags(data: list=[]):
    """Build Emx Tags
    Collate all tags defined in the `tags` property and transform into EMX
    format.
    
    @param data (list) : converted emx object (packages, entities, attributes)
    
    @return record set
    """
    rawTags=list(set([row['tags'] for row in data if 'tags' in row]))
    tagsToProcess=[
        {'label': tag.split(' ')[0], 'iri': tag.split(' ')[1]}
        for tag in rawTags
    ]

    builtTags=[]
    for tag in tagsToProcess:
        builtTags.append({
            'identifier': tag['label'],
            'label': tag['label'],
            'objectIRI': tag['iri'],
            'codeSystem': tag['label'].split('_')[0],
            'relationLabel': 'isAssociatedWith',
            'relationIRI': 'http://molgenis.org#isAssociatedWith'
        })
        
    return builtTags


def extractTagId(data: list=[]):
    """Extract Tag Identifier
    @param data input dataset from yamlemxconvert.convert (packages, entities, etc.)
    """
    for row in data:
        if row.get('tags'):
            row['tags']=row['tags'].split(' ')[0]
            
            
def recodePackageVersionDateString(string, version, date):
    """Recode Package Version Data String
    Rename <version:date> in the description of a package if using
    
    @pattern string string to check
    @param version version number to insert
    @param date date to insert
    """
    match = re.search(r'<version:date>', string)
    if match:
        return re.sub(r'<version:date>', f"({version}, {date})", string)