#'////////////////////////////////////////////////////////////////////////////
#' FILE: data_fairgenomes.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-10-19
#' MODIFIED: 2021-11-24
#' PURPOSE: fetch fairgenomes lookups for use in URDM
#' STATUS: working
#' PACKAGES: pandas; requests
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

import pandas as pd
import requests

# define class for listing metadata for public github repos
class github:
    def __init__(self):
        self.host = 'https://api.github.com/'
        self.headers = {
            'Accept': 'application/vnd.github.v3+json'
        }
        
    def _get(self, url, headers):
        try:
            r = requests.get(url, headers = headers)
            if not r.status_code // 100 == 2:
                return f'Error: unable to import data({r.status_code}): {r.content}'
                
            r.raise_for_status()
            return r.json()
        except requests.exceptions.HTTPError as error:
            raise SystemError('Unable to get contents:\n{}'.format(error))
        
    def contents(self, owner: str, repo: str, path: str):
        """List contents at Github Repo Path
        
        Attributes:
            owner (str) : username who owns repository
            repo  (str) : name of the repository
            path  (str) : location of the files within the repository
            
        """
        url = f'{self.host}repos/{owner}/{repo}/contents/{path}'
        raw = self._get(url, self.headers)
        return raw

#//////////////////////////////////////////////////////////////////////////////

# List files from FAIR Genomes Github repo:
# https://github.com/fairgenomes/fairgenomes-semantic-model/tree/main/lookups
gh = github()
repo = gh.contents(
    owner = 'fairgenomes',
    repo = 'fairgenomes-semantic-model',
    path = 'lookups'
)

# select files that are used in the URDM
filesToDownload = {
    'AnatomicalSources.txt' : 'anatomicalSource',
    'Ancestry.txt' : 'ancestry',
    'BiospecimenTypes.txt': 'biospecimenType',
    'Countries.txt': 'country',
    'Diseases.txt': 'diseases',
    'DataUseModifiers.txt': 'dataUseModifiers',
    'DataUsePermissions.txt': 'dataUsePermissions',
    'GenomeAccessions.txt': 'genomeAccessions',
    'GenotypicSex.txt' : 'genotypicSex',
    'InclusionStatus.txt' : 'subjectStatus',
    'InclusionCriteria.txt': 'inclusionCriteria',
    'NGSKits.txt': 'ngsKits',
    'PathologicalState.txt' : 'pathologicalState',
    'PhenotypicSex.txt': 'phenotypicSex',
    'SequencingMethods.txt': 'sequencingMethods',
    'SequencingPlatform.txt': 'sequencingPlatform',
    'SequencingInstrumentModels.txt': 'sequencingInstrumentModels'
}

# pull download URLs for files of interest
files = []
for file in repo:
    if file['name'] in filesToDownload:
        files.append({
            'name': file['name'],
            'download_url': file['download_url']
        })
        
# download null flavors
# nullFlavorsUrl = [x['download_url'] for x in repo if x['name'] == 'NullFlavors.txt'][0]
# nullFlavors = pd.read_csv(nullFlavorsUrl, sep='\t',dtype=str,keep_default_na=False)

# read files and save to `emx/lookups/`
for f in files:
    print('Downloading file: {}'.format(f['name']))
    raw = pd.read_csv(f['download_url'], sep='\t', dtype=str, keep_default_na=False)
    path = 'emx/lookups/umdm_lookups_{}.csv'.format(filesToDownload[f['name']])
    # if f['name'] not in ['Countries.txt']:
    #     raw = raw.append(pd.DataFrame(data = nullFlavors))
    raw.to_csv(path, index=False)

