#'////////////////////////////////////////////////////////////////////////////
#' FILE: convert.py
#' AUTHOR: d.c.ruvolo
#' CREATED: 2021-09-01
#' MODIFIED: 2021-09-06
#' PURPOSE: convert yaml to emx format
#' STATUS: working; ongoing
#' PACKAGES: see below
#' COMMENTS: see below
#'////////////////////////////////////////////////////////////////////////////

import os
import yaml
import pandas as pd
from datetime import datetime
from src.molgenis.convert.utils import emxAttributes

# Convert
# @description Convert YAML-EMX markup into EMX- CSV or XLSX file format
#
# @section Instructions
#
# The purpose of the the class `Convert` is to give users the option to write
# Molgenis EMX markup in YAML, and then convert (or compile) into the desired
# file format (csv, excel).
#
# The structure of the yaml file (i.e., property names, syntax, etc.), is very
# similar to the Excel method. There are a few additional features that make
# the process a bit simpler.
#
# You can...
#
# 1.) define default attribute options and apply them globally,
# 2.) define datasets within the YAML (might be useful for smaller entities), and
# 3.) compile file into many formats (csv, xlsx)
#
# @section The YAML Format
#
# You can write your data model using Molgenis EMX attribute names. Each yaml file
# should be considered a package with one or more entities. The name of the YAML
# file should be the name of the Molgenis package and all entities should be
# written using the <package>_<entity> format. Define the package at the top of
# the file. In addition to the normal EMX package attributes, you can also use
# `version` and `date`
#
# ```yaml
# name: mypackage
# label: My Package
# description: some description about this package
# version: 0.0.9000
# date: 2021-09-01
# ```
#
# @examples
# c = Convert(file = "path/to/my/file.yml")
# c.convert()
#
class Convert:
    def __init__(self, file):
        self.file = file
        self.emx = False
    #
    # @name __yaml__read__
    # @description read yaml file
    # @param file path to file (from self.file)
    # @return dictionary
    #
    def __yaml__read__(self, file):
        with open(file, 'r') as stream:
            try:
                return yaml.safe_load(stream)
            except yaml.YAMLError as err:
                print("Unable to read yaml:\n" + repr(err))
            stream.close()
    #
    # @name __emx__extract__package__
    # @description extract known EMX package attributes
    # @param data parsed yaml object
    # @param include_pkg_meta if TRUE, version and date will be added to description
    # @return ...
    #
    def __emx__extract__package__(self, data, include_pkg_meta):
        pkg = {}
        keys = list(data.keys())
        for k in keys:
            if k in emxAttributes['packages'] or k.startswith(('label-', 'description-')):
                pkg[k] = data[k]
        
        if include_pkg_meta:
            pkgMeta = {}
            if 'version' in keys:
                pkgMeta['version'] = "v" + str(data['version'])
            if 'date' in keys:
                pkgMeta['date'] = str(datetime.strptime(str(data['date']), "%Y-%m-%d").date())
            if pkgMeta:
                if 'description' in keys:
                    pkg['description'] = pkg['description'] + ' (' + ', '.join(pkgMeta.values()) + ')'
                else:
                    pkg['description'] = ', '.join(pkgMeta.values())
        return pkg
    #
    # @name __emx__extract__entities
    # @description extract known EMX entity attributes
    # @param data parsed yaml object
    # @return list of dictionaries
    #
    def __emx__extract__entities__(self, data):
        emx = {'entities': [], 'attributes': [], 'data': {}}
        langAttrs = ('label-', 'description-')
        for entity in data['entities']:
            entityKeys = list(entity.keys())

            # validate required emx properties
            if 'name' not in entityKeys:
                raise ValueError('Error in entity: missing required attribute "name"')
            
            if 'attributes' not in entityKeys:
                raise ValueError('Error in entity: missing required attribute "attributes"')
            

            # extract entity attributes and append package name automatically
            e = {'package': self.package}
            for ekey in entityKeys:
                if ekey in emxAttributes['entities'] or ekey.startswith(langAttrs):
                    e[ekey] = entity[ekey]
            emx['entities'].append(e)
            
            # check for attributes and extract
            attributes = entity['attributes']
            for attr in attributes:
                attrKeys = list(attr.keys())
                d = {'entity': entity['name']}
                for aKey in attrKeys:
                    if aKey in emxAttributes['attributes'] or aKey.startswith(langAttrs):
                        d[aKey] = attr[aKey]

                # apply default settings if specified
                if data['defaults']:
                    defaultKeys = list(data['defaults'].keys())
                    for dKey in defaultKeys:
                        if dKey not in attrKeys:
                            d[dKey] = data['defaults'][dKey]

                emx['attributes'].append(d)
            
            # check for datasets and extract
            if 'data' in entity:
                name = self.package + '_' + entity['name']
                emx['data'][name] = entity['data']

        return emx
    #
    #
    def ___xlsx__headers__(self, wb, columns, name):
        sheet = wb.sheets[name]
        format = wb.book.add_format({'bold': False, 'border': False})
        for col, value in enumerate(columns):
            sheet.write(0, col, value, format)
    #
    # @name __write__xlsx__
    # @description write emx to xlsx
    # @param path output path
    #
    def __write__xlsx__(self, path, includeData):
        wb = pd.ExcelWriter(path, engine = 'xlsxwriter')

        pkgs = pd.DataFrame(self.emx['packages'], index=[0])
        enty = pd.DataFrame(
            self.emx['entities'],
            index = list(range(0, len(self.emx['entities'])))
        )
        attr = pd.DataFrame(
            self.emx['attributes'],
            index = list(range(0, len(self.emx['attributes'])))
        )
        
        
        pkgs.to_excel(wb, sheet_name = 'packages', startrow = 1, header = False, index = False)
        enty.to_excel(wb, sheet_name = 'entities', startrow = 1, header = False, index = False)
        attr.to_excel(wb, sheet_name = 'attributes', startrow = 1, header = False, index = False)
        
        self.___xlsx__headers__(wb, pkgs.columns.values, 'packages')
        self.___xlsx__headers__(wb, enty.columns.values, 'entities')
        self.___xlsx__headers__(wb, attr.columns.values, 'attributes')
        
        # process each dataset individually
        if 'data' in self.emx and includeData:
            for dataset in self.emx['data']:
                i = list(range(0, len(self.emx['data'][dataset])))
                df = pd.DataFrame(self.emx['data'][dataset], index = i,)
                df.to_excel(wb, sheet_name = dataset, startrow = 1, header = False, index = False)
                self.___xlsx__headers__(wb, df.columns.values, dataset)

        wb.save()
    #
    # @name convert
    # @description convert yaml file into EMX structure
    # @param include_pkg_meta if TRUE, version and date will be added to description
    # @return ...
    #
    def convert(self, include_pkg_meta = True):
        yaml = self.__yaml__read__(self.file)
        
        keys = list(yaml.keys())
        if 'name' not in keys:
            raise ValueError('Error in convert: missing required attribute "name"')
        
        if 'entities' not in keys:
            raise ValueError('Error in convert: missing "entities"')

        self.package = yaml['name']
        self.emx = {
            'packages': self.__emx__extract__package__(yaml, include_pkg_meta),
            **self.__emx__extract__entities__(yaml)
        }   
    #
    # @name write
    # @description write EMX files
    # @param format write as csv or xlsx (default)
    # @param outDir output directory (defaults to ".")
    # @param includeData If True (default), any datasets defined in the yaml
    #       will be written to file
    # @return None
    def write(self, format = 'xlsx', outDir = '.', includeData = True):
        if format not in ['csv', 'xlsx']:
            raise ValueError('Error in write: unexpected format ', str(format))
        
        if format == 'xlsx':
            file = outDir + '/' + self.package + '.' + str(format)
            if os.path.exists(file):
                print('file exists deleting...')
                os.remove(file)
            self.__write__xlsx__(file, includeData)
        
        # if format == 'csv':
        #     self.__write__csv__(file)


# tests
c = Convert(file = 'dev/birddata.yml')
c.convert()
c.write(outDir = 'dev')
c.emx
