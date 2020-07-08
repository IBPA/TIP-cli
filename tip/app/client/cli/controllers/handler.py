# -*- coding: utf-8 -*-
"""cli/controllers/handler.py description

This module defines a class and methods for communicating with back end.

Author:
    Fangzhou Li: https://github.com/fangzhouli

Example:
    TODO

TODO:
    - Read method.

"""

from datetime import datetime
import requests

from models import convert_csv_to_json


class Handler:
    """A Handler class for sending requests and receiving responses.

    """

    def create(self, user, pw, fobj):
        """Send requests for creating new document on the database.

        Args:
            user (str): The user name.
            pw (str): The password associated with the user name.
            fobj (str or file object): The CSV file containing data.

        """
        data_json = convert_csv_to_json(fobj)
        data_json['uploader'] = user
        data_json['auth_key'] = pw
        data_json['upload_date'] = str(datetime.now())[:19]

        requests.post(url='http://localhost:3000/api/upload',
                      json=data_json)

    def read(self):
        """
        """
        pass

    def update(self):
        """
        """
        pass

    def delete(self):
        """
        """
        pass
