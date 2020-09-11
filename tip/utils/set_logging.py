# -*- coding: utf-8 -*-
"""tip/utils/logger.py description

This module simplifies the built-in logging module

Author:
    Jason Youn: https://github.com/jasonyoun

"""

import logging
from tip.config import ConfigLogger


def set_logging(log_file=None, log_level=ConfigLogger.LEVEL):
    """Configure logging. By default, log to the console. If requested, log to
    a file specified by the user.

    Args:
        log_file (str): Path to save the log file.
        log_level (log.level): Log level.

    """
    # create logger
    logger = logging.getLogger()
    logger.setLevel(log_level)

    # create formatter
    formatter = logging.Formatter(
        '%(asctime)s %(levelname)s %(filename)s: %(message)s')

    # create and set file handler if requested
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setLevel(log_level)
        file_handler.setFormatter(formatter)
        logger.addHandler(file_handler)

    # create and set console handler
    stream_handler = logging.StreamHandler()
    stream_handler.setLevel(log_level)
    stream_handler.setFormatter(formatter)
    logger.addHandler(stream_handler)
