import requests


def send_read_request():
    res = requests.get(url='http://localhost:3000/compound/Water')
    print(res.text)


if __name__ == '__main__':
    send_read_request()
