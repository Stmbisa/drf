import requests 
from getpass import getpass
import json

auth_endpoint = "http://localhost:8000/api/auth/"
username = input("what is your Username?:\n")
password = getpass("What is your Password?\n")


auth_response = requests.post(auth_endpoint,json={'username': username, 'password': password})
print(auth_response)


if auth_response.content:
    try:
        print(auth_response.json())
    except ValueError:
        # print(json.dumps(auth_response))
        print("Response is not in JSON format")
        print("Raw Response Content:", auth_response.content)
else:
    print("response is empty")

if auth_response.status_code == 200:
    token = auth_response.json()['token'] # we extract the token from the response dictionary
    if token:
        headers = {
            'Authorization': f"Bearer {token}"  # Add a space after 'Token' or bearer
        }
        endpoint = "http://localhost:8000/api/products/"


        get_response = requests.get(endpoint, headers=headers) 
        print(get_response.json())