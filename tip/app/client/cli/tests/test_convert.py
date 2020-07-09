from models import Converter


def test_converter():
    """
    """

    # hc = ['cid', 'cas', 'common_names', 'iupac_name', 'inchikey', 'smiles',
    #       'mw (g/mol)', 'comment']
    # ha = ['protein', 'gene', 'ahr_type', 'species', 'conc_substrate (μM)',
    #       'conc_tested (μM)', 'inhibition (%)', 'ec50 (nM)', 'pmid', 'comment']
    cvtr = Converter()
    print(cvtr.convert('data_dummy.csv'))


if __name__ == '__main__':
    test_converter()
