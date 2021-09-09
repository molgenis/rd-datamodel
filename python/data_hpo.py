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

import requests
import datatable as dt
from datatable import f
from datetime import datetime

# @name ghReleaseDownloader
# @description Find releases and download them
class ghReleaseDownloader:
    def __init__(self, owner: str = None, repo: str = None):
        self.releases = []
        self.gh_host = 'https://api.github.com'
        self.gh_owner = owner
        self.gh_repo = repo
        self.gh_release_endpoint = None
        self.__build__release__url__()
        
    def __build__release__url__(self):
        self.gh_release_endpoint = '{}/repos/{}/{}/releases'.format(
            self.gh_host,
            self.gh_owner,
            self.gh_repo
        )

    def __print__releases(self):
        print(self.releases[:, ['id', 'name', 'tag_name', 'published_at']])
        
    def __format__date(self, date):
        if not date:
            return None
        
        return datetime.strptime(str(date), '%Y-%m-%dT%H:%M:%SZ').date()
    
    #' @name listReleases
    #' @description List current HPO releases (tagged as an release)
    #' @param per_page number of results per page (default: 30)
    #' @param page page number of results to fetch (default: 1)
    #' @reference
    #' \url{https://docs.github.com/en/rest/reference/repos#releases}
    #' @return response code or json object
    def listReleases(self, per_page: int = 30, page: int = 1):
        
        # if releases dataset has not been built, then fetch information
        if not self.releases:
            headers = {'Accept': 'application/vnd.github.v3+json'}
            if per_page: headers['per_page'] = str(per_page)
            if page: headers['page'] = str(page)

            try:
                resp = requests.get(url = self.gh_release_endpoint, headers = headers)
                resp.raise_for_status()
            except requests.exceptions.HTTPError as e:
                raise SystemError(e)
                
            data = resp.json()
            releases = []
            for d in data:
                releases.append({
                    'id' : d.get('id', None),
                    'name': d.get('name', None),
                    'tag_name': d.get('tag_name', None),
                    'created_at': self.__format__date(d.get('created_at', None)),
                    'published_at': self.__format__date(d.get('published_at', None)),
                    'tarball_url': d.get('tarball_url', None),
                    'zipball_url': d.get('zipball_url', None)
                })
            print('Found {} releases'.format(len([d['id'] for d in data])))
            self.releases = dt.Frame(releases)
        
        # otherwise print dataset
        self.__print__releases()
        

# start 
gh = ghReleaseDownloader(owner = 'obophenotype', repo = 'human-phenotype-ontology')
gh.listReleases()
