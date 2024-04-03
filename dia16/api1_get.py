import requests, json

url = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(url)

print("")
print(response)#<Response [200]>

if response.status_code == 200:#200 OK
    print(response.text) #convierte la respuesta en un string
    respuesta = json.loads(response.text)
    print(type(respuesta))#<class 'list'>
    for posicion, dicc in enumerate(respuesta):
        print(f"diccionario{posicion} {dicc}")
    
else:
    print("Error en la solicitud",response.status_code)