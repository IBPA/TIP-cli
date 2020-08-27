# -*- coding: utf-8 -*-
"""tip/config.py description.

This is a script that initialize the configuration of TIP.

"""


import logging


class ConfigNetwork:
    """
    """
    HOST = '18.221.84.133'  # IP address of the server on AWS EC2.

    @staticmethod
    def get_address():
        return 'http://' + ConfigNetwork.HOST


class ConfigLogger:
    """
    """
    LEVEL = logging.WARNING
