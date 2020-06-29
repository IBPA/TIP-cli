import json
import requests

if __name__ == '__main__':

    url = 'http://localhost:3000/api/upload'
    headers = {
        'Content-Type'  : 'application/json',
        'Accept'        : 'application/json'}
    data = json.load(open('data_dummy.csv.json', 'r'))

    r = requests.post(url = url, json = data)
    print(r.text)