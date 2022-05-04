#'////////////////////////////////////////////////////////////////////////////
#' FILE: data_fairgenomes.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-10-19
#' MODIFIED: 2022-05-04
#' PURPOSE: fetch fairgenomes lookups for use in URDM
#' STATUS: stable
#' PACKAGES: pandas; requests
#' COMMENTS: Download files from fairgenomes/fairgenomes-semantic-model
#' https://github.com/fairgenomes/fairgenomes-semantic-model/tree/main/lookups
#'////////////////////////////////////////////////////////////////////////////

from rd_datamodel.api.github import github
import pandas as pd


gh = github()
repositoryFiles=gh.listContents(
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
for file in repositoryFiles:
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
