# -*- coding: utf-8 -*-
"""config.py description.

This is a script that initialize the configuration of TIP.

"""


import logging as log

class ConfigNetwork:
    """
    """
    HOST = '192.168.218.128'
    PORT = '8001'

    @staticmethod
    def get_address():
        return 'http://' + ConfigNetwork.HOST + ':' + ConfigNetwork.PORT

class ConfigLogger:
    """
    """
    LEVEL = log.WARNING
