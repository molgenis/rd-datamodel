#'////////////////////////////////////////////////////////////////////////////
#' FILE: module_approved_users.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-10-21
#' MODIFIED: 2021-10-21
#' PURPOSE: populate approved users reference entities
#' STATUS: working
#' PACKAGES: molgenis.client
#' COMMENTS: designed to run inside a molgenis database
#'////////////////////////////////////////////////////////////////////////////


import molgenis.client as molgenis
from urllib.parse import quote_plus
import requests
import json
import re

    
# extend molgenis.Session class
class molgenis(molgenis.Session):
    """molgenis
    An extension of the molgenis.client class
    """
    
    # update_table
    def update_table(self, entity: str, data: list):
        """Update Table
        
        When importing data into a new table using the client, there is a 1000
        row limit. This method allows you push data without having to worry
        about the limits.
        
        @param entity (str) : name of the entity to import data into
        @param data (list) : data to import
        
        @return a status message
        """
        props = list(self.__dict__.keys())
        if '_url' in props: url = self._url
        if '_api_url' in props: url = self._api_url
        url = f'{url}v2/{quote_plus(entity)}'
        
        # single push
        if len(data) < 1000:
            try:
                response = self._session.post(
                    url = url,
                    headers = self._get_token_header_with_content_type(),
                    data = json.dumps({'entities' : data})
                )
                if not response.status_code // 100 == 2:
                    return f'Error: unable to import data({response.status_code}): {response.content}'
                
                return f'Imported {len(data)} entities into {str(entity)}'
            except requests.exceptions.HTTPError as err:
                raise SystemError(err)
        
        # batch push
        if len(data) >= 1000:    
            for d in range(0, len(data), 1000):
                try:
                    response = self._session.post(
                        url = url,
                        headers = self._get_token_header_with_content_type(),
                        data = json.dumps({'entities': data[d:d+1000] })
                    )
                    if not response.status_code // 100 == 2:
                        raise response.raise_for_status()

                    return f'Batch {d}: Imported {len(data)} entities into {str(entity)}'
                except requests.exceptions.HTTPError as err:
                    raise SystemError(f'Batch {d} Error: unable to import data:\n{str(err)}')


#//////////////////////////////////////

print('Initializing connection with Molgenis and pulling data...')

# pull data
m = molgenis(url = 'http://localhost/api/', token = '${molgenisToken}')
pkgs = m.get('sys_md_Package')
roles = m.get('sys_sec_Role')

print('Building reference entities...')

# process packages
users_packages = []
for p in pkgs:
    if not (re.match(r'^(sys([_])?)', p['id'])):
        users_packages.append({
            'id': p['id'],
            'label': p['label'],
            'description': p['description']
        })

# process roles
users_roles = []
for r in roles:
    if (re.search(r'((_MANAGER)|(_EDITOR)|(_VIEWER))$', r['name'])) or (r['name'] == 'SU'):
        users_roles.append({
            'id': r['name'],
            'label': r['name'] if r['name'] == 'SU' else r['name'].replace('_', ' ').title(),
            'description': r['description']
        })
        
# push data
print('Importing data...')
m.update_table(entity = 'users_packages', data = users_packages)
m.update_table(entity = 'users_roles', data = users_roles)