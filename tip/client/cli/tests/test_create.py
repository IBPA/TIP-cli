from os import path

from controllers.handler import create


def create_dummy_data():
    data_filename = 'data_dummy.csv'
    data_path = path.abspath(path.dirname(__file__) + data_filename)

    user = 'lfz'
    pw = 'fakepassword123'
    fobj = open(data_path, 'r')
    create(user, pw, fobj)


if __name__ == '__main__':
    create_dummy_data()
