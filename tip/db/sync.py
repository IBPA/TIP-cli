# -*- encoding: utf-8 -*-
"""

This module defines functions for synchronizing the necessary configuration on
local machines and that on the TIP server.

Author:
    Fangzhou Li: https://github.com/fangzhouli

Attributes:
    PATH_DIR_CURR (str): The path of the current directory.
    PATH_DIR_TEMPLATE (str): The path of the template directory.
    PATH_FILE_TEMPLATE_ASSAY (str): The path of the assay template.
    PATH_FILE_TEMPLATE_COMPOUND (str): The path of the compound template.

"""

from os import mkdir, path
import json
import pickle
import logging
import requests
from tip.config import ConfigNetwork

PATH_DIR_CURR = path.abspath(path.dirname(__file__))
PATH_DIR_TEMPLATE = path.join(PATH_DIR_CURR, 'template')
PATH_FILE_TEMPLATE_ASSAY = path.join(PATH_DIR_TEMPLATE, 'assay.pickle')
PATH_FILE_TEMPLATE_COMPOUND = path.join(PATH_DIR_TEMPLATE, 'compound.pickle')


def sync_template():
    """Send requests for getting the up-to-date data template.

    Generates:
        $PATH_DIR_TEMPLATE/assay.txt (file): The template of assay data.
        $PATH_DIR_TEMPLATE/compound.txt (file): The template of compound data.

    """
    logging.info("Synchronizing the data template...")

    if not path.exists(PATH_DIR_TEMPLATE):
        mkdir(PATH_DIR_TEMPLATE)

    res = requests.get(url=ConfigNetwork.get_address() + "/database/header")
    header_json = json.loads(res.text)
    header_compound = header_json['compound'].split(',')
    header_assay = header_json['assay'].split(',')

    logging.debug("Compound header: {}; Assay header: {}".format(
        ' '.join(header_compound), ' '.join(header_assay)))

    with open(PATH_FILE_TEMPLATE_ASSAY, 'wb') as f:
        pickle.dump(header_assay, f)
    with open(PATH_FILE_TEMPLATE_COMPOUND, 'wb') as f:
        pickle.dump(header_compound, f)

    logging.info("Synchronized the data template successfully!")
