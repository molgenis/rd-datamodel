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

from python.ghReleaseDownloader import ghReleaseDownloader

# start 
gh = ghReleaseDownloader(owner = 'obophenotype', repo = 'human-phenotype-ontology')
gh.listReleases()
gh.downloadRelease(outDir = 'downloads')

# process data here