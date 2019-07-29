import logging
from typing import NamedTuple


def get_logger(config: NamedTuple) -> logging.Logger:
    """
    Create instance of a logger and configure it using the variables from yaml config variables
    :return:
    """
    try:
        # create logger with app name
        logger: logging.Logger = logging.getLogger(config.general.app)
        logger.setLevel(logging.DEBUG)
        # create file handler which logs even debug messages
        fh = logging.FileHandler(config.general.log)
        fh.setLevel(logging.DEBUG)
        # create formatter and add it to the handlers
        formatter = logging.Formatter('%(asctime)s - %(name)s - %(levelname)s - %(message)s')
        fh.setFormatter(formatter)
        # add the handlers to the logger
        logger.addHandler(fh)
        # returns a configured instance of logger
        return logger

    except Exception as error:
        print(error)
