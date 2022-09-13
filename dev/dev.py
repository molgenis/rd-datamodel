
from yamlemxconvert.convert2 import Convert2
import re

emx2 = Convert2(file = 'model/umdm.yaml')
emx2.convert(keepModelPackage=True)

for row in emx2.model['molgenis']:
  tag = row.get('semantics')
  if bool(tag):
    if re.search(r'^([0-9a-zA-Z]{1,}([:_])[0-9a-zA-Z]{1,}\s+([a-zA-Z0-9.]{1,}))', tag):
      row['semantics'] = re.split(r'\s+', tag)[1]

# subjects = [row for row in emx2.model['molgenis'] if row['tableName'] == 'subjects']

for row in emx2.model['molgenis']:
  if row.get('refSchema') == 'umdm_lookups':
    row['refSchema'] = 'umdmLookups'
  if row.get('refSchema') == 'umdm':
    row['refSchema'] = None
    
    
[row for row in emx2.model['molgenis'] if row['columnType'] == 'ref']