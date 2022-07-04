from configparser import ConfigParser

'''
Example case:
from lib.config_lib import configu

c=configu()
c.read(r"Y:\python\image_proj\setting.ini")

output_folder = c['folders']['output_folder']
formats = c['misc'].getlist('image_formats')
'''

class configu(ConfigParser):

    def __init__(self):
        super().__init__()

    #so can get list from configuration file
    #returns numbers as nos, and not strings
    def getlist(self, section, option, *, raw=False, vars=None,
                 fallback=None, **kwargs):        
        try:
            self.temp_list = self.get(section,option).split(',')
            self.output_list = []
            for _ in self.temp_list:
                #try to convert to int, then float, if can't add string
                try:
                    output=int(_)
                    self.output_list.append(output)
                except:
                    try:
                        output=float(_)
                        self.output_list.append(output)
                    except:
                        self.output_list.append(_)
            return self.output_list
        except Exception as e:
            print('*** EXCEPTION TRYING TO EXTRACT LIST FROM CONFIG FILE ***')
            raise
            

