# -*- coding: utf-8 -*-
"""Helper functions for data uploading.

This module provides helper functions to connect CLI and backend. It generates
a template CSV file to users to guide them fill data correctly, and it then
accept and convert the CSV file to JSON file.

Author:
    Fangzhou Li: https://github.com/fangzhouli
    Jason Youn: https://github.com/jasonyoun

Example:
    See '__main__'.

Attributes:
    cols_compound (list of str): Column names of compound data.
    cols_assay (list of str): Column names of assay data.

TODO:
    * Modularize the code OOP.
    * Integrate with back end (JavaScript?)
    * function convert can be more elegant.
"""

import csv
import json
import numpy as np
import pandas as pd

cols_compound   = open('compound.txt', 'r').read().split('\n')
cols_assay      = open('assay.txt', 'r').read().split('\n')

def convert(fobj_or_path):
    """Convert the filled CSV template file into JSON format.

    Args:
        fobj_or_path (file object or str): A file object or a file path.

    Generates:
        A converted JSON file named by '{$fobj_or_path}.json'.

    """
    def convert_row(se, n_assay):
        """Convert a series into organized JSON format.

        Args:
            se (pd.Series): A row of dataframe.
            n_assay (int): The amount of assays associated with the compound.

        Returns:
            row (dict): A converted row.

        """
        row = {}
        assays = []

        for col in cols_compound:
            val = se[col]
            if type(val) is not float or not np.isnan(val):
                row[col] = val

        # Removing numerical suffix of columns.
        for i in range(n_assay):
            assay = {}
            for col in cols_assay:
                val = se[col + str(i + 1)]
                if type(val) is not float or not np.isnan(val):
                    assay[col] = val

            # Skipping empty assay.
            if assay:
                assays.append(assay)
        row['assays'] = assays
        return row

    data = pd.read_csv(fobj_or_path, dtype = str)
    n_assay = int(data.columns.tolist()[-1][-1])
    compounds = data.apply(
        lambda se: convert_row(se, n_assay), axis = 1).to_numpy().tolist()
    data_json = dict(
        count = len(compounds),
        compounds = compounds)
    json.dump(data_json, open(fobj_or_path + '.json', 'w'))

def generate_template(path, n_assay):
    """Generate a template CSV file to the given path.

    Args:
        path (str): A file path.
        n_assay (int): The maximum amount of assays associated with any compound

    Generates:
        A empty CSV file with specified header

    """
    cols = [] + cols_compound
    for i in range(n_assay):
        cols_assay_batch = [s + str(i + 1) for s in cols_assay]
        cols += cols_assay_batch

    writer = csv.writer(open(path, 'w'))
    writer.writerow(cols)

if __name__ == '__main__':

    # generate_template('template.csv', 2)
    convert('data_dummy.csv')