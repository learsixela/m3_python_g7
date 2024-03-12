#esto es un comentario de una linea
""" 
                        comentario
    de mas de 
    una
    linea 
"""
print("texto a imprimir por consola")
print(2 + 2)
print(12 - 2)
print(2 * 2)
#print(20/0) #ZeroDivisionError: division by zero
print(20 / 10)#el resultado siempre sera un float

numero = 23
print(numero)

#Limitantes 
#No esta permitido la suma de letras y numeros
# print("texto"+12) #TypeError: can only concatenate str (not "int") to str
print("texto",12) 
#concatenar = "texto"+12
print("texto"+"34")

#INTERPOLACION
print(f"el numero es {numero}")
