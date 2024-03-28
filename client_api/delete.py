import requests

id = input(' entre the id of product you want delete ')


endpoint = f"http://127.0.0.1:8000/product/{id}/delete"
response = requests.delete(endpoint)
#print(response.json())
print(response.status_code , response.status_code == 204 )
