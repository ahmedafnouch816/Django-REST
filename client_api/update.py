import requests

endpoint = "http://127.0.0.1:8000/product/1/update"
response = requests.put(endpoint , json={'name':'Avocat' , 'content':'' , 'prix':15})
print(response.json())
print(response.status_code)
