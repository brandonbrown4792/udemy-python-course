import logging

logging.basicConfig(
    format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d %(message)s',
    datefmt='%d-%m-%Y %H:%M:%S',
    level=logging.DEBUG,
    filename='logs.txt'
)
logger = logging.getLogger('__name__')  # Stores logger name as the module it is in

logger.info('This will not show up')
logger.warning('This will.')
logger.debug('This is a debug message')
logger.critical('A critical error occured')

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
