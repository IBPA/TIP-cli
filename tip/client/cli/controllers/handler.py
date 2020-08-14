# -*- coding: utf-8 -*-
"""cli/controllers/handler.py description

This module defines functions for communicating with back end.

Author:
    Fangzhou Li: https://github.com/fangzhouli

TODO:
    - Read method.

"""

import shlex
import logging
import requests
from config import ConfigNetwork
from models import convert_csv_to_json


def create(fobj):
    """Send requests for creating new document on the database.

    Args:
        user (str): The user name.
        pw (str): The password associated with the user name.
        fobj (str or file object): The CSV file containing data.

    """
    logging.info('Requesting to create data...')
    data_json = convert_csv_to_json(fobj)
    # data_json['user'] = user
    # data_json['pw'] = pw
    # 192.168.218.128
    res = requests.post(url=ConfigNetwork.get_address() + '/compound',
                        json=data_json)
    if res.status_code == 400:
        logging.error(res.text)


def read(keywords):
    """Send requests for reading existing documents on the database.

    Args:
        keywords (list of str): A list of keywords to nevigate search result.

    """
    logging.info('Requesting to read data...')
    keywords_str = '+'.join(keywords)
    res = requests.get(
        url=ConfigNetwork.get_address() + '/compound/' + keywords_str)
    if res.status_code == 400:
        logging.error(res.text)
    print(res.text)


def update(tid, query):
    """Send requests for updating existing documents on the database.

    Args:
        user (str): The user name.
        pw (str): The password associated with the user name.
        fobj (str or file object): The CSV file containing data.
    """
    logging.info('Requesting to update data...')
    # data = dict(
    #     tid=tid,
    #     )
    data = {}
    splitter = shlex.shlex(query[0], posix=True)
    splitter.whitespace = ','
    splitter.whitespace_split = True
    params = list(splitter)
    # Check data type
    data_type = params[0]
    type_key, type_value = data_type.split(':')
    if type_key != 'type' or type_value not in ['compound', 'assay']:
        raise SyntaxError("The first parameter of query must be data type.")

    for param in params[1:]:
        key, value = param.split(':')
        data[key] = value
    res = requests.put(
        url=ConfigNetwork.get_address() + '/' + type_value +'/' + tid,
        json=data)

    if res.status_code == 400:
        logging.error(res.text)
    elif res.status_code == 200:
        print(res.text)

def delete():
    """
    """
    pass
