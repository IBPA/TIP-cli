# -*- coding: utf-8 -*-
"""tip/db/crud.py description

This module defines functions for sending RESTful requests to the TIP server.

Author:
    Fangzhou Li: https://github.com/fangzhouli

TODO:
    - Read method.
    - refactor: shlex
    - read cli and restful different?
    - logging: create - send info from server.
    - Error definition?

"""

import json
import logging
import requests
from tip.config import ConfigNetwork
from tip.utils import convert_csv_to_json, split_values


def create(fobj, header_compound, header_assay):
    """Send requests for creating new document on the database.

    Args:
        fobj (str or file object): The CSV file containing data.

    Returns:
        (str): The response from the server.

    """
    logging.info('Requesting to create data...')
    data_json = convert_csv_to_json(fobj, header_compound, header_assay)
    res = requests.post(url=ConfigNetwork.get_address() + '/compound',
                        json=data_json)
    if res.status_code == 200:
        logging.debug('Status: 200, ' + res.text)
        return res.text
    else:
        logging.error(res.text)
        raise RuntimeError('Data creating has failed.')


def read(values):
    """Send requests for reading existing documents on the database.

    Args:
        values (str): A string to indicate fields and values for updating.

    Returns:
        (str): The response from the server.

    """
    logging.info('Requesting to read data...')

    # Parse cli values
    params = split_values(values)
    type_key, type_value = params[0].split(':')
    if type_key != 'type' or type_value not in ['compound', 'assay']:
        raise SyntaxError('The first parameter of values must be data type.')
    logging.debug('Key: ' + type_key + ', Value: ' + type_value)

    # Construct database values.
    req_query_list = []
    for param in params[1:]:
        key, value = param.split(':')
        req_query_list.append(key + '=' + value)
    req_query = '&'.join(req_query_list)
    logging.debug('Requested values: ' + req_query)

    # Retrieve the response.
    res = requests.get(
        url=ConfigNetwork.get_address() + '/' + type_value + '?' + req_query)
    if res.status_code == 200:
        logging.debug('Status: 200, ' + res.text)
        return res.text
    else:
        logging.error('Status: ' + str(res.status_code) + ', ' + res.text)
        raise RuntimeError('Data reading has failed.')


def read_headers():
    """Send requests for getting the up-to-date database headers.

    Returns:
        header_compound, header_assay (tuple): Two lists of headers.

    """
    logging.info('Requesting to get headers...')
    res = requests.get(url=ConfigNetwork.get_address() + '/database/header')
    header_json = json.loads(res.text)
    header_compound = header_json['compound'].split(',')
    header_assay = header_json['assay'].split(',')
    logging.debug('Compound header: {}; Assay header: {}'.format(
        ' '.join(header_compound), ' '.join(header_assay)))
    return (header_compound, header_assay)


def update(tid, values):
    """Send requests for updating existing documents on the database.

    Args:
        tid (str): The TIP Id of updating data.
        values (str): A string to indicate fields and values for updating.

    Returns:
        (str): The response from the server.

    """
    logging.info('Requesting to update data...')

    data = {}

    # Parse cli values.
    params = split_values(values)
    type_key, type_value = params[0].split(':')
    if type_key != 'type' or type_value not in ['compound', 'assay']:
        raise SyntaxError('The first parameter of values must be data type.')
    logging.debug('Key: ' + type_key + ', Value: ' + type_value)

    # Construct database values and retrieve.
    for param in params[1:]:
        key, value = param.split(':')
        data[key] = value
    res = requests.put(
        url=ConfigNetwork.get_address() + '/' + type_value + '/' + tid,
        json=data)
    if res.status_code == 200:
        logging.debug('Status: 200, ' + res.text)
        return res.text
    else:
        logging.error('Status: ' + str(res.status_code) + ', ' + res.text)
        raise RuntimeError('Data updating has failed.')


def delete(tid, values):
    """Send requests for deleting and returning existing documents on the
    database.

    Args:
        tid (str): The TIP Id of deleting data.
        values (str): A string to indicate fields and values for updating.

    Returns:
        (str): The response from the server.

    """
    logging.info('Requesting to delete data...')

    # Parse cli values and request.
    params = split_values(values)
    type_value = params[0].split(':')[1]
    res = requests.delete(
        url=ConfigNetwork.get_address() + '/' + type_value + '/' + tid)
    if res.status_code == 200:
        logging.debug('Status: 200, ' + res.text)
        return res.text
    else:
        logging.error('Status: ' + str(res.status_code) + ', ' + res.text)
        raise RuntimeError('Data deleting has failed.')
