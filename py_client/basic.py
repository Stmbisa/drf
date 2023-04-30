import requests 
endpoint = "https://httpbin.org/status/200/"
endpoint = "https://httpbin.org/"


get_response = requests.get(endpoint) # HTTP Request
print(get_response.text)


git remote add origin https://github.com/Stmbisa/drf.git