import requests

endpoint = "http://127.0.0.1:8000/product/"
response = requests.post(endpoint , json={'name':'pasteque' , 'content':'just pasteque' , 'prix':20})
print(response.json())
print(response.status_code)

# HTTP RESQUEST ==> HTML
# REST API HTTP ==> JSON JS OBJECT


# how api  et c'est un client 