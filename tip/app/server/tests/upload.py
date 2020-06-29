import csv
import json
import numpy as np
import pandas as pd

cols_compound   = open('compound.txt', 'r').read().split('\n')
cols_assay      = open('assay.txt', 'r').read().split('\n')

def convert(fobj_or_path):
    """convert the filled CSV template file into JSON format
    input:
        fobj_or_path    : (file object or str) file
    output:
        data            : (pd.DataFrame)"""

    def convert_row(se, n_assay):
        """convert a row of dataframe into organized JSON format
        input:
            se          : (pd.Series) a row of dataframe
            n_assay     : (int) amount of assays associated with the compound
        output:
            row         : (dict) JSON-fied row"""

        row = {}
        assays = []

        for col in cols_compound:
            val = se[col]
            if type(val) is not float or not np.isnan(val):
                row[col] = val
        for i in range(n_assay):
            assay = {}
            for col in cols_assay:
                val = se[col + str(i + 1)]
                if type(val) is not float or not np.isnan(val):
                    assay[col] = val
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
    """generate a template CSV file to the given path
    input:
        path            : (str) location
        n_assay         : (int) amount of assays associated with the compound
    output:
        (None)"""

    cols = cols_compound
    for i in range(n_assay):
        cols_assay_batch = [s + str(i + 1) for s in cols_assay]
        cols += cols_assay_batch

    writer = csv.writer(open(path, 'w'))
    writer.writerow(cols)

if __name__ == '__main__':

    # generate_template('template.csv', 2)
    convert('data_dummy.csv')