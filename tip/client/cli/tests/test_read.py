import requests


def send_read_request():
    res = requests.get(url='http://128.120.143.184:8001/compound/Water')
    print(res.text)


if __name__ == '__main__':
    send_read_request()
