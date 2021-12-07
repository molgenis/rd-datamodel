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
import csv

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
with open('downloads/obophenotype-human-phenotype-ontology-d3394d2/hp.json', 'r') as file:
    nodeset = json.load(file)['graphs'][0]['nodes']
    file.close()


# extract HPO nodeset and parse
hpo = []
for node in nodeset:
    if node['type'] == 'CLASS':
        hpo.append({
            'value': node.get('lbl'),
            'description': node.get('meta', {}).get('definition',{}).get('val', None),
            'codesystem': re.sub(r'([0-9\_])', '', os.path.basename(node['id'])),
            'code': re.sub('_', ':', os.path.basename(node['id'])),
            'iri': node.get('id')
        })
    

# write to csv
with open('data/hpo_release_{}.csv'.format(tag_name), 'w', newline='') as output:
    writer = csv.DictWriter(output,hpo[0].keys())
    writer.writeheader()
    writer.writerows(hpo)