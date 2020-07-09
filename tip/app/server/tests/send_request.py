# import json
import requests

URL = 'http://localhost:3000/api/gen'


def test_create():
    r = requests.post(url=URL, files={'file': open('data_dummy.csv', 'rb')})
    print(r.text)


def test_gen_tmp():
    r = requests.get(url=URL)
    print(r.text)


if __name__ == '__main__':
    test_gen_tmp()
