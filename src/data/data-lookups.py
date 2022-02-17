#'////////////////////////////////////////////////////////////////////////////
#' FILE: data-lookups.py
#' AUTHOR: David Ruvolo
#' CREATED: 2022-02-04
#' MODIFIED: 2022-02-14
#' PURPOSE: script for collating data for reference tables
#' STATUS: stable
#' PACKAGES: datatable, requests
#' COMMENTS: Built for extracting ontology terms from EBI Ontology search.
#'  1. Navigate to https://www.ebi.ac.uk/ols/index
#'  2. Search and click a term to navigation to the term page
#'  3. Click the json button
#'  4. Copy the URL and paste it below (see block 1)
#   5. Run blocks 2-4
#'////////////////////////////////////////////////////////////////////////////

from datatable import dt
from os import path
import requests

def GET(url):
    """Get JSON
    @param url (str) : URL of json data
    """
    print(f'Fetching data from {url}')
    try:
        response = requests.get(url = url)
        response.raise_for_status()
        json = response.json().get('_embedded').get('terms')
        if type(json) is list and len(json) > 1:
            return json
        elif type(json) is list and len(json) == 1:
            return json[0]
        else:
            return json
    except requests.exceptions.HTTPError as error:
        print(error)


def getTermRecord(data: dict = {}):
    """Extract Term Metadata
    @param data (dict) : object containing the metadata of a term
    """
    return {
        'value': data.get('label'),
        'description': ' '.join(data.get('description')),
        'codesystem': data.get('ontology_name').upper(),
        'code': path.basename(data.get('iri')).split('_')[-1],
        'iri': data.get('iri')
    }
    
def getChildEndpoint(data):
    """Extract Children Term Url
    If a term has children, extract the API endpoint to the term's children
    @param data (dict) : json object containing metadata of a term
    """
    return data.get('_links').get('children').get('href')


#//////////////////////////////////////

# ~ 1 ~
# Get metadata for ontology term
#
url='https://www.ebi.ac.uk/ols/api/ontologies/edam/terms?iri=http://edamontology.org/operation_2409'


# ~ 2 ~
# Extract Ontology term's metadata
# Use `getTermRecord(data = parentMeta)` to extract the parent term if needed

parentMeta = GET(url = url)


# ~ 3 ~
# Get child and grandchild terms
#
data = []
if parentMeta.get('has_children'):
    print('Pulling children terms...')
    children = GET(url = getChildEndpoint(data = parentMeta))
    for child in children:
        data.append(getTermRecord(data = child))
        if child.get('has_children'):
            print('Pulling grandchild terms...')
            grandchildren = GET(url = getChildEndpoint(data = child))
            if type(grandchildren) is dict:
                data.append(getTermRecord(data = grandchildren))
            else:
                for grandchild in grandchildren:
                    data.append(getTermRecord(data = grandchild))
    
       
# ~ 4 ~         
# write to csv
path = '~/Desktop/datahandling.csv'
dt.Frame(data).to_csv(path)