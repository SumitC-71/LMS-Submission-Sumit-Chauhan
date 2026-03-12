import logging

def get_logger():
    filename = 'api_errors.log'
    logger = logging.getLogger('error_logger')
    logger.setLevel(logging.INFO)

    # Check if handlers already exist to avoid duplicates
    if logger.hasHandlers():
        return logger

    formatter = logging.Formatter(
        '%(asctime)s | %(levelname)s | %(funcName)s | line %(lineno)d | %(message)s'
    )
    # console handler
    console_handler = logging.StreamHandler()
    # set level to info so that info shown in console
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    file_handler = logging.FileHandler(filename)
    # set level to warning so only errors are shown in api_errors.log
    file_handler.setLevel(logging.WARNING)
    file_handler.setFormatter(formatter)

    logger.addHandler(console_handler)
    logger.addHandler(file_handler)
    return logger

