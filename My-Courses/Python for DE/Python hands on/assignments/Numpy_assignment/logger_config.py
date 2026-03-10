import logging
import os

def setup_logger():
    os.makedirs("logs", exist_ok=True)  # if already exists then do nothing

    logger = logging.getLogger("pipeline_logger")
    logger.setLevel(logging.INFO)
    

    # prevent multiple handlers
    if logger.hasHandlers():
        return logger
    
    # formatter
    formatter = logging.Formatter(
        '%(asctime)s | %(name)s | %(filename)s | function %(funcName)s | line %(lineno)d | %(levelname)s | %(message)s'
    )

    # file handler
    filename = "logs/app.log"
    file_handler = logging.FileHandler(filename,mode='w')
    file_handler.setLevel(logging.INFO)
    file_handler.setFormatter(formatter)

    # console handler
    console_handler = logging.StreamHandler()
    console_handler.setLevel(logging.INFO)
    console_handler.setFormatter(formatter)

    # setting up handlers
    logger.addHandler(file_handler)
    logger.addHandler(console_handler)

    return logger

def task_logger(task_name, status):
    logger = setup_logger()

    if status not in ["start", "end"]:
        logger.error("Invalid status passed to task_logger: %s", status)
        return

    if status == "start":
        logger.info("======== Task %s started ========\n", task_name)
    else:
        logger.info("======== Task %s completed ========\n", task_name)