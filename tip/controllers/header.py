# -*- coding: utf-8 -*-
"""tip/controllers/header.py description.

This module defines a function that requests back end for the most up-to-date
database headers.

Author:
    Fangzhou Li: https://github.com/fangzhouli

TODO:
"""

import json
import logging
import requests
from tip.config import ConfigNetwork


def get_headers():
    """Send requests for getting the up-to-date database headers.

    Returns:
        header_compound, header_assay (tuple): Two lists of headers.

    """
    logging.info('Requesting to get headers...')
    res = requests.get(url=ConfigNetwork.get_address() + '/database/header')
    header_json = json.loads(res.text)
    header_compound = header_json['compound'].split(',')
    header_assay = header_json['assay'].split(',')
    return (header_compound, header_assay)
