# file header should go here
# what does this file do?
# who are the authors?
# any to-dos?
# please find a good file docstring format and use it for all files

import csv
import numpy as np
import pandas as pd

cols_compound = open('compound.txt', 'r').read().split('\n')
cols_assay = open('assay.txt', 'r').read().split('\n')


def convert(fobj_or_path):
    """Convert the filled CSV template file into JSON format.

    Args:
        fobj_or_path (file object or str): SOME MEANINGFUL DESCRIPTION.

    Returns:
        data (pd.DataFrame) : SOME MEANINGFUL DESCRIPTION.
    """

    def convert_row(se, n_assay):
        """Convert a row of dataframe into organized JSON format.

        Args:
            se (pd.Series): A row of dataframe.
            n_assay (int): Amount of assays associated with the compound.

        Returns:
            row (dict): JSON-fied row.
        """
        row = {}
        assays = []

        for col in cols_compound:
            val = se[col]
            if type(val) is not float or not np.isnan(val):
                row[col] = val
        for i in range(n_assay):
            assay = {}
            for col in cols_assay:
                if type(val) is not float or not np.isnan(se[col + str(i + 1)]):
                    assay[col] = se[col + str(i + 1)]
            if assay:
                assays.append(assay)
        row['assays'] = assays

        return row

    data = pd.read_csv(fobj_or_path, dtype=str)
    n_assay = int(data.columns.tolist()[-1][-1])
    data = data.apply(lambda se: convert_row(se, n_assay), axis=1)

    return data


def generate_template(path, n_assay):
    """Generate a template CSV file to the given path.

    Args:
        path (str): Location.
        n_assay (int): Amount of assays associated with the compound.

    Returns:
        None
    """
    cols = cols_compound
    for i in range(n_assay):
        cols_assay_batch = [s + str(i + 1) for s in cols_assay]
        cols += cols_assay_batch

    writer = csv.writer(open(path, 'w'))
    writer.writerow(cols)


if __name__ == '__main__':
    generate_template('template.csv', 2)
    convert('template.csv')
