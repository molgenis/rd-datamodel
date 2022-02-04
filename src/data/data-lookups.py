#'////////////////////////////////////////////////////////////////////////////
#' FILE: data-lookups.py
#' AUTHOR: David Ruvolo
#' CREATED: 2022-02-04
#' MODIFIED: 2022-02-04
#' PURPOSE: script for collating data for reference tables
#' STATUS: stable
#' PACKAGES: datatable, requests
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

from datatable import dt
import requests

def GET(url):
    try:
        response = requests.get(url = url)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.HTTPError as error:
        print(error)


# pull parent ontology
url = 'https://www.ebi.ac.uk/ols/api/ontologies/ncit/terms?iri=http://purl.obolibrary.org/obo/NCIT_C17357'
resp = GET(url = url)


# extract link to children
childrenLinks = (
    resp.get('_embedded',{})
    .get('terms')[0]
    .get('_links')
    .get('children')
    .get('href')
)

# get child terms
children = GET(url = childrenLinks)
childTerms = children.get('_embedded', {}).get('terms')

# shape reference table
terms = []
for child in childTerms:
    print(child.get('iri'), child.get('label'))
    terms.append({
        'value': child.get('label'),
        'description': child.get('description')[0],
        'codesystem': child.get('ontology_prefix'),
        'code': child.get('annotation', {}).get('code')[0],
        'iri': child.get('iri')
    })


# write to file or apply additional transformations
dt.Frame(terms).to_csv('dist/umdm_lookups_gender.csv')