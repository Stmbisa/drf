import requests 
# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/"
endpoint = "http://localhost:8000/api/"


get_response = requests.post(endpoint, params= {"abc":123},json={"title":"hello python",}) # HTTP Request
print(get_response.headers)
print(get_response.json())

# print(get_response.json())
# print(get_response.status_code)
