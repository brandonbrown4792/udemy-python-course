import logging

# Configure logger as time then levl then message
# -8 adds four spaces
# Then print out file name and line number
logging.basicConfig(format='%(asctime)s %(levelname)-8s [%(filename)s:%(lineno)d] %(message)s', level=logging.DEBUG)
logger = logging.getLogger('test_logger')

logger.info('This will not show up')
logger.warning('This will.')
logger.debug('This is a debug message.')
logger.critical('A critical error occured.')

"""
DEBUG
INFO
WARNING
ERROR
CRITICAL
"""
