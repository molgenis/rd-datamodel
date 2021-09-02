

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
    #
    # @name __yaml__read__
    # @description read yaml file
    # @param self required parameter
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
    # @param self required parameter
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
    # @param self required parameter
    # @param data parsed yaml object
    # @return list of dictionaries
    #
    def __exm__extract__entities__(self, data):
        emx = []
        for entity in data['entities']:
            keys = list(entity.keys())

            if 'name' not in keys:
                raise ValueError('Error in entity: missing required attribute "name"')
            
            e = {}
            for k in keys:
                if k in emxAttributes['entities'] or k.startswith(('label-', 'description-')):
                    e[k] = entity[k]
            
            if 'package' not in keys:
                e['package'] = data['name']

            emx.append(e)
        return emx
    #
    # @name convert
    # @description
    # @param self required parameter
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
        
        emx = {
            'packages': self.__emx__extract__package__(yaml, include_pkg_meta),
            'entities': self.__exm__extract__entities__(yaml),
            'attributes': [],
            'name': yaml['name']
        }

        return emx


# tests
c = Convert(file = 'dev/birddata.yml')
c.convert()


x = c.__yaml__read__('dev/birddata.yml')
c.__emx__extract__package__(x, True)
c.__exm__extract__entities__(x)
