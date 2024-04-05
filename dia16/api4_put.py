import requests

url = "https://jsonplaceholder.typicode.com/posts/10"

payload = {
    "userId": 1,
    "title": "titulo de ejemplo 2 ",
    "body": "esto es un ejemplo del body 2"
}

response = requests.put(url, json=payload)

if response.status_code == 200: #200 => ok
    print("Actualizacion exitosa")
    print(response.text)
else:
    print("Error en la actualizacion del posts")