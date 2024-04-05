import api_get, template


def crear_html(url):
    response = api_get.obtener_aves(url)
    #print(response[0])
    cadena = "" 
    for dicc in response:
        #titulo_esp = dicc["name"]["spanish"]
        #titulo_en = dicc["name"]["english"]
        #url_img = dicc["images"]["full"]
        #print(titulo_esp,titulo_en, url_img)
        cadena = cadena + template.aves.substitute(titulo_esp = dicc["name"]["spanish"], 
                                titulo_en = dicc["name"]["english"],
                                url_img = dicc["images"]["full"])

    return template.html.substitute(contenido = cadena)

if __name__ == "__main__":
    url= "https://aves.ninjas.cl/api/birds"
    
    html = crear_html(url)
    print(type(template.html))#<class 'string.Template'>
    
    archivo = open("prueba/index2.html","w")
    archivo.write(html)
