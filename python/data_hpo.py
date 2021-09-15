#'////////////////////////////////////////////////////////////////////////////
#' FILE: data_hpo.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-09-09
#' MODIFIED: 2021-09-09
#' PURPOSE: pull latest HPO ontology release and process
#' STATUS: in.progress
#' PACKAGES: 
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

import json
import os
import re
import pandas as pd

# @name __hpo__unpack__node__
# @description Extract relevant HPO metadata per node
# @param node a dictionary
# @return dictionary aligned with Fairgenomes structure
def __hpo__unpack__node__(node):
    return {
        'value': node.get('lbl'),
        'definition': node.get('meta', {}).get('definition',{}).get('val', None),
        'codesystem': re.sub(r'([0-9\_])', '', os.path.basename(node['id'])),
        'code': re.sub('_', ':', os.path.basename(node['id'])),
        'iri': node.get('id')
    }
    
#//////////////////////////////////////

tag_name = 'v2021-08-02'

# ~ 0 ~ 
# Download Compressed Ontology
# Use the `ghReleaseDownloader` to download the latest release
# from python.ghReleaseDownloader import ghReleaseDownloader
# gh = ghReleaseDownloader(owner = 'obophenotype', repo = 'human-phenotype-ontology')
# gh.listReleases()
# gh.downloadRelease(outDir = 'downloads', tag_name = tag_name)


# ~ 1 ~
# HPO => EMX
# process data here

# load raw data and extract nodes
file = open('downloads/obophenotype-human-phenotype-ontology-d3394d2/hp.json', 'r')
raw = json.load(file)
file.close()

# extract HPO nodeset and parse
nodeset = raw['graphs'][0]['nodes']
hpo = []
for node in nodeset:
    hpo.append(__hpo__unpack__node__(node))
    

# write to csv
filename = 'data/hpo_release_{}.csv'.format(tag_name)
hpoData = pd.DataFrame(hpo)
hpoData.to_csv('data/hpo_release_v2021-08-02.csv', index = False)