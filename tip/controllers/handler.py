# -*- coding: utf-8 -*-
"""tip/controllers/handler.py description

This module defines functions for communicating with back end.

Author:
    Fangzhou Li: https://github.com/fangzhouli

TODO:
    - Read method.
    - refactor: shlex
    - read cli and restful different?
    - logging: create - send info from server.
    - Error definition?
"""

import shlex
import logging
import requests
from tip.config import ConfigNetwork
from tip.models import convert_csv_to_json


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
    res = requests.post(url=ConfigNetwork.get_address() + '/compound',
                        json=data_json)

    if res.status_code == 200:
        logging.info('Creating data is finished.')
        return res.text
    else:
        logging.error(res.text)
        raise RuntimeError("Data creating has failed.")


def read(query):
    """Send requests for reading existing documents on the database.

    Args:
        query (str): The fields and values for updating. The format of query:
            - Each parameter is a pair of a field and a value.
            - A field and a value are separated by exactly a colon.
            - The first parameter must be 'type:compound' or 'type:assay',
                indicating the data type you are updating.
            - Each parameter is separated by exactly a comma.
            - Use quotes for strings containing whitespace(s),
                (e.g., comments.)
            - Use semicolons for strings containing multiple values,
                (e.g., pmid.)

    """
    logging.info('Requesting to read data...')
    splitter = shlex.shlex(query[0], posix=True)
    splitter.whitespace = ','
    splitter.whitespace_split = True
    params = list(splitter)
    # Check data type
    type_key, type_value = params[0].split(':')
    if type_key != 'type' or type_value not in ['compound', 'assay']:
        raise SyntaxError("The first parameter of query must be data type.")

    # let's put a log here that logs the type_key, type_value

    req_query_list = []
    for param in params[1:]:
        key, value = param.split(':')
        req_query_list.append(key + '=' + value)
    req_query = '&'.join(req_query_list)

    # also put a log on what this req_query is.
    # btw, all these logs should be set to level debug.

    res = requests.get(
        url=ConfigNetwork.get_address() + '/' + type_value + '?' + req_query)

    # put logging about the return code even if the code was not 400.
    # It's always good practice to put these for debudding purpose.

    if res.status_code == 200:
        logging.info(res.text)
        return res.text
    else:
        logging.error(res.text)
        raise RuntimeError("Data reading has failed.")


def update(tid, query):
    """Send requests for updating existing documents on the database.

    Args:
        tid (str): The TIP Id of updating data.
        query (str): The fields and values for updating. The format of query:
            - Each parameter is a pair of a field and a value.
            - A field and a value are separated by exactly a colon.
            - The first parameter must be 'type:compound' or 'type:assay',
                indicating the data type you are updating.
            - Each parameter is separated by exactly a comma.
            - Use quotes for strings containing whitespace(s),
                (e.g., comments.)
            - Use semicolons for strings containing multiple values,
                (e.g., pmid.)

    """
    logging.info('Requesting to update data...')
    data = {}
    splitter = shlex.shlex(query[0], posix=True)
    splitter.whitespace = ','
    splitter.whitespace_split = True
    params = list(splitter)
    # Check data type
    type_key, type_value = params[0].split(':')
    if type_key != 'type' or type_value not in ['compound', 'assay']:
        raise SyntaxError("The first parameter of query must be data type.")

    for param in params[1:]:
        key, value = param.split(':')
        data[key] = value
    res = requests.put(
        url=ConfigNetwork.get_address() + '/' + type_value + '/' + tid,
        json=data)

    # similar to above, put log in every possible step (debug)
    # Also put log for the return code.

    if res.status_code == 200:
        logging.info(res.text)
        return res.text
    else:
        logging.error(res.text)
        raise RuntimeError("Data updating has failed.")


def delete(tid, query):
    """Send requests for deleting and returning existing documents on the
    database.

    Args:
        tid (str): The TIP Id of deleting data.
        query (str): Similar to query of updating, but only requires the data
            type field.

    """
    logging.info('Requesting to delete data...')
    splitter = shlex.shlex(query[0], posix=True)
    splitter.whitespace = ','
    splitter.whitespace_split = True
    params = list(splitter)
    type_value = params[0].split(':')[1]
    res = requests.delete(
        url=ConfigNetwork.get_address() + '/' + type_value + '/' + tid)

    # similar to above, put log in every possible step (debug)
    # Also put log for the return code.

    if res.status_code == 200:
        logging.info(res.text)
        return res.text
    else:
        logging.error(res.text)
        raise RuntimeError("Data deleting has failed.")
