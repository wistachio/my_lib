import sys
import configparser
import lib.filelib as fl



default = r"/python/settings.ini"

class Settings(configparser.ConfigParser):
    '''
    Based on existing config parser
    2 Additions:
    1. Pass file on startup, there is a default file value
    2. contains platform attribute


    Example usage:

    import lib.config_settings as cs #import lib

    setting = cs.Settings()
    settings._get('file_loc') #will retrieve "file_loc" setting info in platform section

    or can use for object initialisation:
    settings = cs.Settings(r"/media/veracrypt1/python/settings.ini") #settings file
    '''
    
    def __init__(self,file=default):
        super().__init__()
        if fl.exists(file):
            self.read(file)
        else:
            raise Exception(f'No such file: {file}')
        self.platform = sys.platform

    def _get(self, name):
        '''retrieves value in the platform section
        eg if linux, settings._get(name)
        will be equivalent to settings['linux'].get(name)'''
        return self[self.platform].get(name)


