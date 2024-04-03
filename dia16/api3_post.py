import requests

url = "https://jsonplaceholder.typicode.com/posts"

payload = {
    "userId": 1,
    "title": "titulo de ejemplo",
    "body": "esto es un ejemplo del body"
}

response = requests.post(url, json=payload)

if response.status_code == 201: #201 => created
    print("Insercion exitosa")
    print(response.text)
else:
    print("Error en la creacion de posts")