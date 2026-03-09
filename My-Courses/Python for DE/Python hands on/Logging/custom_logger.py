import logging

logger = logging.getLogger("my_logger")
logger.setLevel(logging.INFO)

console_handler = logging.StreamHandler()   # console output
file_handler = logging.FileHandler('log.log') # File handler

console_handler.setLevel(logging.WARNING)
file_handler.setLevel(logging.DEBUG)

formatter = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(message)s - %(name)s - %(filename)s - %(lineno)d - %(funcName)s'
)

console_handler.setFormatter(formatter)
file_handler.setFormatter(formatter)

logger.addHandler(console_handler)
logger.addHandler(file_handler)

logger.info("INFO message")
logger.error("ERROR message")
