#'////////////////////////////////////////////////////////////////////////////
#' FILE: data_fairgenomes.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-10-19
#' MODIFIED: 2021-10-19
#' PURPOSE: fetch fairgenomes attribute files and write to csv
#' STATUS: in.progress
#' PACKAGES: NA
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////


from datatable import dt, f, fread
import requests
import re

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


# get repo contents
gh = github()
files = gh.contents(
    owner = 'fairgenomes',
    repo = 'fairgenomes-semantic-model',
    path = 'generated/molgenis-emx'
)

# reduce data
data = []
for file in files:
    if re.search(r'(_attributes.tsv)$', file['name']):
        data.append({
            'name': file.get('name'),
            'download_url': file.get('download_url')
        })

# read attributes
attribs = dt.Frame()
for d in data:
    raw = fread(url = d['download_url'])
    raw[:,dt.update(
        file = d['name'].replace('_attributes.tsv', '')
    )]
    if not bool(attribs):
        attribs = raw
    else:
        attribs = dt.rbind(attribs, raw, force = True)

# del attribs, d, raw
attribs.to_pandas().to_excel('data/mapped_attributes.xlsx', index = False)