

from _typeshed import Self
import yaml
from datetime import datetime
from os import path
from src.molgenis.convert.utils import emxAttributes

#
# @name Convert
# @description Convert YAML-EMX markup into EMX- CSV/XLSX files
#
# @examples
# c = Convert(file = "path/to/my/file.yml")
# c.convert()
#
class Convert:
    def __init__(self, file):
        self.file = path.abspath(file)
        self.emx = False,
    #
    # @name __yaml__read__
    # @description read yaml file
    # @param file path to file (from self.file)
    # @return dictionary
    #
    def __yaml__read__(self, file):
        with open(path.abspath(file), 'r') as stream:
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
            pkgMeta = False
            if 'version' in keys:
                pkgMeta = "v" + str(data['version'])
            if 'date' in keys:
                date = str(datetime.strptime(str(data['date']), "%Y-%m-%d").date())
                if pkgMeta:
                    pkgMeta = pkgMeta + ', ' + date
                else:
                    pkgMeta = date
            if 'description' in keys:
                if pkgMeta:
                    pkg['description'] = pkg['description'] + ' (' + pkgMeta + ')'
            else:
                if pkgMeta:
                    pkg['description'] = pkgMeta
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
                emx['attributes'].append(d)
            
            # check for datasets and extract
            if 'data' in entity:
                name = self.package + '_' + entity['name']
                emx['data'][name] = entity['data']
        return emx
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

# tests
c = Convert(file = 'dev/birddata.yml')
c.convert()
c.emx