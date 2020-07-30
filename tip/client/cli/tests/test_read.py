import requests


def send_read_request():
    res = requests.get(url='http://192.168.218.128:8001/compound/Water')
    print(res.text)


if __name__ == '__main__':
    send_read_request()
