#THIRD PARTY APP TO COMMUNICATE WITH YOUR API WITHOUT POSTMAN

import requests
import json

URL = "http://127.0.0.1:8000/student/info/"

def get_data(id = None):
    data = {}
    if id is not None:
        data = {'id':id}
    json_data = json.dumps(data)
    r = requests.get(url = URL, data = json_data)
    data = r.json()
    print(data)


get_data()


