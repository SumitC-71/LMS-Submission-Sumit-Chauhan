import logging

try:
    x = 10 / 0
except Exception:
    logging.exception("Error occurred")