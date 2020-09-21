# -*- coding: utf-8 -*-
"""tip/utils/convert.py description.

This module defines functions that help data format conversion, i.e.,
CSV to JSON.

Author:
    Fangzhou Li: https://github.com/fangzhouli
    Jason Youn: https://github.com/jasonyoun

"""

import logging
import numpy as np
import pandas as pd


def _convert_compound_df_to_json(df_compound, header_compound, header_assay):
    """Convert a DataFrame of compound into dict-like JSON format.

    Args:
        df (pd.DataFrame): A DataFrame contains exactly one compound info.

    Returns:
        compound_dict (dict): A dict of converted compound DataFrame.

    """
    # Compound info only exists on the first row.
    compound_dict = df_compound.iloc[0][header_compound].dropna().to_dict()

    assays = []
    df_compound[header_assay].rename(columns={'comment2': 'comment'}).apply(
        lambda se: assays.append(se.dropna().to_dict()), axis=1)
    compound_dict['assays'] = assays

    return compound_dict


def convert_csv_to_json(fobj, header_compound, header_assay):
    """Convert a filled CSV template file into JSON format.

    Args:
        fobj (file object or str): A file object or a file path.

    Returns:
        data_converted (dict): A converted JSON format data.

    """
    logging.info('Converting uploaded CSV file into JSON data format...')

    # Split the dataframe by each compound.
    df = pd.read_csv(fobj, dtype=str)
    idx_split = df[~df[header_compound].isnull().all(axis=1)
                   ].index[1:]  # Skip the first split point, 0.
    df_compound_list = np.split(df, idx_split)

    data_converted = {}
    compounds = [_convert_compound_df_to_json(
        df_compound, header_compound, header_assay)
        for df_compound in df_compound_list]
    data_converted = dict(
        count=len(compounds),
        compounds=compounds)

    logging.debug('Converted data: %s', data_converted)

    return data_converted
