import requests

endpoint = "http://127.0.0.1:8000/product/2/update"
response = requests.put(endpoint , json={'name':'pomme' , 'content':'' , 'prix':25})
print(response.json())
print(response.status_code)
