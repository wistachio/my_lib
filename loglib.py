import logging

class _log():
    def __init__(self,filename,level=logging.INFO):
        logging.basicConfig(filename=filename, level=level,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

    def log_info(self,msg):
        logging.info(msg)

    def log_error(self,msg):
        logging.error(msg)

    def log_critcal(self,msg):
        logging.critical(msg)

'''
Example:

log_file=r'Y:\python\logs\voda.txt'
logging.basicConfig(filename=log_file, level=logging.INFO,
                    format='%(asctime)s %(message)s', datefmt='%m/%d/%Y %I:%M:%S %p')

logging.info(f'Success! Name:{name} {surname}\n')
logging.critical(f'Error: {e}\n')
'''
