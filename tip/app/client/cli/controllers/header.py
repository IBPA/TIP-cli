# -*- coding: utf-8 -*-
"""cli/controllers/header.py description.

This module defines a function that requests back end for the most up-to-date
database headers.

Author:
    Fangzhou Li: https://github.com/fangzhouli

TODO:
"""

import json
import logging
import requests


def get_headers():
    """Send requests for getting the up-to-date database headers.

    Returns:
        header_compound, header_assay (tuple): Two lists of headers.

    """
    logging.info('Requesting to get headers...')
    req = requests.get(url='http://localhost:3000/api/schema')
    header_json = json.loads(req.text)
    header_compound = header_json['compound'].split(',')
    header_assay = header_json['assay'].split(',')
    return (header_compound, header_assay)
