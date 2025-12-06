# import requests
# import json

# URL = "http://127.0.0.1:8000/stucreate/"

# data = {
#     'name' : "Anshif",
#     'roll' : 104,
#     'city' : 'Kalikav'
# }

# json_data = json.dumps(data)

# r = requests.post(url= URL, data= json_data)
# print("Status:", r.status_code)
# print("Text:", r.text)


# data = r.json()

# print(data)



# crud

import requests
import json

URL = "http://127.0.0.1:8000/studentapi/"

def get_data(id = None):
    data ={}
    if id is not None:
        data = {'id': id}

    json_data = json.dumps(data)
    r = requests.get(url= URL, data= json_data)
    data = r.json()
    print(data)

# get_data()

# create

def post_data():
    data = {
        'name' : "Fahis",
        'roll' : 105,
        'city' : 'Malappuram'
    }

    json_data = json.dumps(data)
    r = requests.post(url= URL, data= json_data)
    data = r.json()
    print(data)

# post_data()


#UPDATE

def update_data():
    data = {
        'id': 5,
        'name':'Salman',
        'city' : 'kakkanchery'
    }

    json_data = json.dumps(data)
    r = requests.put(url= URL, data= json_data)
    data = r.json()
    print(data)

# update_data()

#DELETE

def delete_data():
    data = {'id': 5}

    json_data = json.dumps(data)
    r = requests.delete(url= URL, data= json_data)
    data = r.json()
    print(data)

delete_data()