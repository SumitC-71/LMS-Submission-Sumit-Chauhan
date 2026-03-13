'''

built-in and custom logs

info logs, warning logs, error logs

levels: 
| Level    | Value |
| -------- | ----- |
| DEBUG    | 10    |
| INFO     | 20    |
| WARNING  | 30    |
| ERROR    | 40    |
| CRITICAL | 50    |

by default logger shows levels like warning or above
for showing console output for other levels you need to configure

Common fields for formating: 
| Format          | Meaning       |
| --------------- | ------------- |
| `%(asctime)s`   | timestamp     |
| `%(levelname)s` | log level     |
| `%(message)s`   | log message   |
| `%(name)s`      | logger name   |
| `%(filename)s`  | file name     |
| `%(lineno)d`    | line number   |
| `%(funcName)s`  | function name |



log_level >= logger_level
AND
log_level >= handler_level


'''

# import logging


# logging.debug("debug")
# logging.info("info")
# logging.warning("warning")
# logging.error("error")
# logging.critical("critical")

# x = 2
# logging.info(f'The value of x: {x}')



'''
console output: 
WARNING:root:warning
ERROR:root:error
CRITICAL:root:critical

format: LEVEL:root:message

here root stands for what logger we are using
here root logger
'''



# try:
#     1/0
# except ZeroDivisionError as e:
#     logging.info('Zero division error', exc_info=True)


import logging

logging.basicConfig(level=logging.INFO, filename='log.log', filemode='w', format="%(asctime)s - %(levelname)s - %(message)s")

logger = logging.getLogger(__name__)

handler = logging.FileHandler('test.log')

formatter = logging.Formatter('%(asctime)s - %(levelname)s - %(message)s - %(lineno)s - %(filename)s')

handler.setFormatter(formatter)

logger.addHandler(handler)

# logger.info('test the custom logger')

# logger.info('hello world')

logging.debug('Debug statement')
