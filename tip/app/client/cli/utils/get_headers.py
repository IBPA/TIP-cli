# -*- coding: utf-8 -*-
"""cli/utils/get_headers.py description

This module contains a utility function that get database headers from the back
end.

Author:
    Fangzhou Li: https://github.com/fangzhouli

Example:
    TODO

TODO:
    - TBD

"""

import json
import requests


def get_headers():
    """
    """
    req = requests.get(url='http://localhost:3000/api/schema')
    header_json = json.loads(req.text)
    header_compound = header_json['compound'].split(',')
    header_assay = header_json['assay'].split(',')
    return (header_compound, header_assay)
