import logging
from logging.handlers import RotatingFileHandler
import os
import glob

for file in glob.glob("backup.log*"):
    os.remove(file)

handler = RotatingFileHandler(
    filename='backup.log'
    , maxBytes=24
    , backupCount=2
)
handler.setLevel(logging.DEBUG)

logger = logging.getLogger('my_logger')
logger.setLevel(logging.INFO)

logger.addHandler(handler)


# logger.info('1234567890')
# logger.info('1234567890')

# logger.info('1234567890')
# logger.info('1234567890')

# logger.info('1234567890')
# logger.info('1234567890')

# logger.info('Roll over....')
