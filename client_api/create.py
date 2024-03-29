import requests

endpoint = "http://127.0.0.1:8000/product/create/"
response = requests.post(endpoint , json={'name':' TEST 01' , 'content':'' , 'prix':300})
print(response.json())
print(response.status_code)
