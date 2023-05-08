import requests 
endpoint = "http://localhost:8000/api/products/565367576/"


# get_response = requests.post(endpoint, params= {"abc":123},json={"title":"hello python",}) # HTTP Request
get_response = requests.get(endpoint) 
# print(get_response.headers)
print(get_response.json())