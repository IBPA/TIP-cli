# -*- coding: utf-8 -*-
"""cli/models/convert.py description.

This module defines functions that help data format conversion, i.e.,
CSV to JSON.

Author:
    Fangzhou Li: https://github.com/fangzhouli
    Jason Youn: https://github.com/jasonyoun

Example:
    See '__main__'.

TODO:
    * update doc string
    * Examples.
    * commented comments removal
    * should I consistently add prefix for all assay columns?
"""

import numpy as np
import pandas as pd
import logging
from controllers import get_headers


HEADER_COMPOUND, HEADER_ASSAY = get_headers()


def _convert_compound_df_to_json(df_compound):
    """Convert a DataFrame of compound into dict-like JSON format.

    Args:
        df (pd.DataFrame): A DataFrame contains exactly one compound info.

    Returns:
        compound_dict (dict): A dict of converted compound DataFrame.

    """
    # Compound info only exists on the first row.
    compound_dict = df_compound.iloc[0][HEADER_COMPOUND].dropna().to_dict()

    assays = []
    # TODO
    df_compound[HEADER_ASSAY].rename(columns={'comment2': 'comment'}).apply(
        lambda se: assays.append(se.dropna().to_dict()), axis=1)
    compound_dict['assays'] = assays
    return compound_dict


def convert_csv_to_json(fobj):
    """Convert a filled CSV template file into JSON format.

    Args:
        fobj (file object or str): A file object or a file path.

    Returns:
        data_converted (dict): A converted JSON format data.

    """
    logging.info('Converting uploaded CSV file into JSON data format...')
    # Split the dataframe by each compound.
    df = pd.read_csv(fobj, dtype=str)
    idx_split = df[~df[HEADER_COMPOUND].isnull().all(axis=1)
                   ].index[1:]  # Skip the first split point, 0.
    df_compound_list = np.split(df, idx_split)

    data_converted = {}
    compounds = [_convert_compound_df_to_json(
        df_compound) for df_compound in df_compound_list]
    data_converted = dict(
        count=len(compounds),
        compounds=compounds)
    return data_converted
