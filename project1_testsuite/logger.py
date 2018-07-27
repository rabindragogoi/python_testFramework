""" Create a logger for general-purpose use throughout the code. """
import logging
from os import getcwd
from os.path import join


def generate_logger(module_name, log_path=None, log_level=logging.INFO):
    if log_path is None:
        log_path = join(getcwd(), module_name + '.log')

    # Returns the logging variable
    logger = logging.getLogger(__name__)

    if logger.handlers:
        logger.handlers = []

    handler = logging.FileHandler(log_path, )
    formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    handler.setFormatter(formatter)

    logging.basicConfig(level=log_level)
    logger.addHandler(handler)

    return logger


def get_logging():
    logger = logging.getLogger(__name__)
    logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
    logging.basicConfig(level=logging.INFO)
    return logger
