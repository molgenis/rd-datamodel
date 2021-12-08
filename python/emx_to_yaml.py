#'////////////////////////////////////////////////////////////////////////////
#' FILE: emx_to_yaml.py
#' AUTHOR: David Ruvolo
#' CREATED: 2021-12-08
#' MODIFIED: 2021-12-08
#' PURPOSE: convert EMX to yaml format
#' STATUS: in.progress
#' PACKAGES: NA
#' COMMENTS: NA
#'////////////////////////////////////////////////////////////////////////////

import pandas as pd
import numpy as np
# import re

class emxToYaml:
    def __init__(self, file: str):
        """Convert Excel EMX file to YAML
        @param file (str) : path to excel file
        """
        self.file = file
        self.emx = {}
        self.yaml = []
        self.indentStyles = {
            'entities': {'key': ' '*2, 'default': ' '*4},
            'attributes': {'key': ' '*6, 'default': ' '*8},
            'tags': {'key': ' '*2, 'default': ' '*4},
        }
        self.__readFileContents__()
        
    def __dictToYaml__(self, data, ignoreAttribs, indentType=None):
        yaml = []
        for index,key in enumerate(data.keys()):
            if not (key.startswith(ignoreAttribs)) and (data[key] is not None):
                #  generate yaml for attribute
                if indentType == 'package':
                    txt = f"{key}: {data[key]}\n"
                else:
                    if index == 0:
                        space = f'{self.indentStyles[indentType].get("key")}- '
                    else:
                        space = self.indentStyles[indentType].get('default')
                    # quote values based on value types
                    value = data[key]
                    if key in ['expression', 'validationExpression']: value = f'"{ value }"'
                    # if re.search(':', value) in value: value = f'"{value}"'
                    
                    txt = '{}{}: {}\n'.format(space, key, value)
                yaml.append(txt)
        return yaml
    
    def __sheetRowsToYamlBlocks__(self, data, ignoreAttribs, indentType=None):
        """Convert rows in xlsx sheet to yaml blocks
        @param data (list) : data to convert
        """
        yaml = []
        for d in data:
            yaml = yaml + self.__dictToYaml__(
                data = d,
                ignoreAttribs = ignoreAttribs,
                indentType = indentType
            )
            yaml.append('\n')
        yaml.append('\n')
        return yaml
        
    def __readFileContents__(self):
        print(f'Reading file "{self.file}"')
        wb = pd.ExcelFile(self.file)
        for sheet in wb.sheet_names:
            if sheet in ['packages','entities','attributes','tags']:
                print(f'Importing contents from sheet: {sheet}')
                self.emx[sheet] = pd.read_excel(wb, sheet).replace({np.nan:None}).to_dict('records')
        
    def convert(self, ignoreAttribs=('label-','description-','backend')):
        yaml = ['\n']
        if 'packages' in self.emx.keys():
            print('Building Yaml for packages...')
            yaml.extend(self.__sheetRowsToYamlBlocks__(
                data = self.emx['packages'],
                ignoreAttribs = ignoreAttribs,
                indentType = 'package'
            ))
            yaml.append('\n')
        
        if 'tags' in self.emx.keys():
            print('Building Yaml for tags...')
            yaml.append('tagDefinitions:\n')
            yaml.extend(self.__sheetRowsToYamlBlocks__(
                data = self.emx['tags'],
                ignoreAttribs = ignoreAttribs,
                indentType = 'tags'
            ))
            yaml.append('\n')
           
        if 'entities' in self.emx.keys():
            print('Building Yaml for Entities and Attributes...')
            yaml.append('entities:\n')
            for entity in self.emx['entities']:
                pkgEntity = f"{entity['package']}_{entity['name']}"
                entityAttribs = [
                    x for x in self.emx['attributes'] if x['entity'] == pkgEntity
                ]
                # prepare yaml for the current entity
                yaml.extend(self.__dictToYaml__(
                    data = entity,
                    ignoreAttribs = ignoreAttribs,
                    indentType = 'entities'
                ))
                # prepare attributes for the current entity
                yaml.append('    attributes:\n')
                yaml.extend(self.__sheetRowsToYamlBlocks__(
                    data = entityAttribs,
                    ignoreAttribs = ignoreAttribs,
                    indentType = 'attributes'
                ))
            yaml.append('\n')
        self.yaml = yaml
        
    def write(self, path):
        with open(path, 'w') as stream:
            stream.writelines(self.yaml)
        stream.close()


c = emxToYaml('_exclude/Copy of variantDB.xlsx')
c.convert()
c.write('_exclude/variantDB.yaml')

