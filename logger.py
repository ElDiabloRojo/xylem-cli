import logging

logging.basicConfig(level=logging.INFO,
                    format='%(asctime)s %(process)d %(levelname)s'
                    '%(message)s',
                    datefmt='%m/%d/%Y %I:%M:%S %p',
                    filename='xylem.log',
                    filemode='a')
