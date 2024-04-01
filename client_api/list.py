import requests
from getpass import getpass

endpoint = 'http://127.0.0.1:8000/api_prod/auth/'
username = input(' Entre votre username: \n')
password = getpass('Entre votre passsword: \n')

auth_response = requests.post(endpoint, json={'username':username,'password':password})
print(auth_response.json())
print(auth_response.status_code)


if auth_response.status_code == 200:
    
    endpoint = "http://127.0.0.1:8000/product/create-list/"
    headers = {
        'authorization':'Bearer 8ca41bc968c34a56a86dda0f0efed56a93e3a725'
    }
    response = requests.get(endpoint, headers=headers)
    print(response.json())
    print(response.status_code)
