

from models import convert_csv_to_json


def test_converter():
    """
    """

    data = convert_csv_to_json('data_dummy.csv')
    print(data)


if __name__ == '__main__':
    test_converter()
