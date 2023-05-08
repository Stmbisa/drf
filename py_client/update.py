import requests 
endpoint = "http://localhost:8000/api/products/1/update/"

data = {
    'title':'Hello my old freind',
    'price':166.8
}
get_response = requests.put(endpoint, json=data) 
# print(get_response.headers)
print(get_response.json())