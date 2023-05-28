import requests 
headers = {'Authorization': 'Bearer 41138cc7ff6927116a82d2a798a37d517ec44f2f' }
endpoint = "http://localhost:8000/api/products/"

data = {
    'title': 'an ending cool title',
}

get_response = requests.post(endpoint, json=data, headers=headers) 
print(get_response.json())