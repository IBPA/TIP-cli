# -*- encoding: utf-8-*-
"""
"""

from ast import literal_eval
import pandas as pd


def convert_json_to_csv(data, header_compound, header_assay):
    """
    """
    df_data = pd.DataFrame(index=range(len(data)),
                           columns=header_compound + header_assay)
    print(literal_eval(data))
    pass
