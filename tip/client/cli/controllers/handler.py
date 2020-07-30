# -*- coding: utf-8 -*-
"""cli/controllers/handler.py description

This module defines functions for communicating with back end.

Author:
    Fangzhou Li: https://github.com/fangzhouli

TODO:
    - Read method.

"""

import logging
import requests
from models import convert_csv_to_json


def create(user, pw, fobj):
    """Send requests for creating new document on the database.

    Args:
        user (str): The user name.
        pw (str): The password associated with the user name.
        fobj (str or file object): The CSV file containing data.

    """
    logging.info('Requesting to create data...')
    data_json = convert_csv_to_json(fobj)
    data_json['user'] = user
    data_json['pw'] = pw
    res = requests.post(url='http://128.120.143.184:8001/compound',
                        json=data_json)
    if res.status_code == 400:
        logging.error(res.text)


def read(keywords):
    """
    """
    logging.info('Requesting to read data...')
    keywords_str = '+'.join(keywords)
    res = requests.get(
        url='http://128.120.143.184:8001/compound/' + keywords_str)
    if res.status_code == 400:
        logging.error(res.text)

    print(res.text)


def update():
    """
    """
    pass


def delete():
    """
    """
    pass
