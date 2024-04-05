import requests, json

def obtener_aves(url):
    #response = requests.get(url)
    #respuesta = json.loads(response.text)
    #return respuesta
    return json.loads(requests.get(url).text)



if __name__ == "__main__":
    url="https://pokeapi.co/api/v2/pokemon/1"
    respuesta = obtener_aves(url)
    print(len(respuesta))
    print(respuesta)

