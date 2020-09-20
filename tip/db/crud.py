# -*- coding: utf-8 -*-
"""

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

import logging
import requests
from tip.utils import convert_csv_to_json, convert_json_to_csv, split_values
from tip.config import ConfigNetwork


def create(fobj, header_compound, header_assay):
    """Send requests for creating new document on the database.

    Args:
        fobj (str or file object): The CSV file containing data.
        header_compound (list of str): The header of compound template.
        header_assay (list of str) : The header of assay template.
    Returns:
        (str): The response from the server.

    """
    logging.info("Requesting to create data...")

    data_json = convert_csv_to_json(fobj, header_compound, header_assay)
    res = requests.post(url=ConfigNetwork.get_address() + '/compound',
                        json=data_json)
    if res.status_code == 200:
        logging.debug("Status: 200, " + res.text)
        return res.text
    else:
        logging.error(res.text)
        raise RuntimeError("Data creating has failed.")

    logging.info("Created successfully!")


def read(fobj, table, values):
    """Send requests for reading existing documents on the database.

    Args:
        fobj (str or file object): The file storing the output.
        table (str): A table the data belongs to.
        values (str): A string to indicate fields and values for updating.

    Returns:
        (str): The response from the server.

    """
    logging.info("Requesting to read data...")
    logging.debug("Table: " + table + ', values: ' + values)

    # Parse cli values
    params = split_values(values)

    # Construct database values.
    req_query_list = []
    for param in params:
        key, value = param.split(':')
        req_query_list.append(key + '=' + value)
    req_query = '&'.join(req_query_list)
    logging.debug("Requested values: " + req_query)

    # Retrieve the response.
    res = requests.get(
        url=ConfigNetwork.get_address() + '/' + table + '?' + req_query)
    if res.status_code == 200:
        logging.debug("Status: 200, " + res.text)

        with open(fobj, 'w') as f:
            f.write(res.text)
        return res.text
    else:
        logging.error("Status: " + str(res.status_code) + ", " + res.text)

        raise RuntimeError("Data reading has failed.")

    logging.info("Read successfully!")


def update(table, id_, values):
    """Send requests for updating existing documents on the database.

    Args:
        table (str): A table the data belongs to.
        id_ (str): The TIP Id of updating data.
        values (str): A string to indicate fields and values for updating.

    Returns:
        (str): The response from the server.

    """
    logging.info("Requesting to update data...")
    logging.debug("Table: " + table + ', values: ' + values)

    data = {}

    # Parse cli values.
    params = split_values(values)

    # Construct database values and retrieve.
    for param in params:
        key, value = param.split(':')
        data[key] = value
    res = requests.put(
        url=ConfigNetwork.get_address() + '/' + table + '/' + id_,
        json=data)
    if res.status_code == 200:
        logging.debug("Status: 200, " + res.text)
        return res.text
    else:
        logging.error("Status: " + str(res.status_code) + ", " + res.text)
        raise RuntimeError("Data updating has failed.")

    logging.info("Updated successfully!")


def delete(table, id_):
    """Send requests for deleting and returning existing documents on the
    database.

    Args:
        table (str): A table the data belongs to.
        id_ (str): The TIP Id of deleting data.

    Returns:
        (str): The response from the server.

    """
    logging.info('Requesting to delete data...')
    logging.debug("Table: " + table)

    # Parse cli values and request.
    res = requests.delete(
        url=ConfigNetwork.get_address() + '/' + table + '/' + id_)
    if res.status_code == 200:
        logging.debug('Status: 200, ' + res.text)
        return res.text
    else:
        logging.error('Status: ' + str(res.status_code) + ', ' + res.text)
        raise RuntimeError('Data deleting has failed.')

    logging.info("Deleted successfully!")
