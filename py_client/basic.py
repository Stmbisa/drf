import requests 
# endpoint = "https://httpbin.org/status/200/"
# endpoint = "https://httpbin.org/"
endpoint = "http://localhost:8000/api/"


get_response = requests.get(endpoint, data={'query':'Hello World'}) # HTTP Request
# print(get_response.text)

print(get_response.json()['message'])
print(get_response.status_code)
