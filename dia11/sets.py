"""
SETS
conjunto de datos,  que no permite duplicados
no es ordenado, se escriben con {}, 

"""

muchos_animales = {'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Gato', 'Perro', 'Tortuga',
'Hurón', 'Hamster', 'Erizo de Tierra'}

print(muchos_animales)
#{'Erizo de Tierra', 'Perro', 'Hamster', 'Gato', 'Hurón', 'Tortuga'}
for elemento in muchos_animales:
    print(elemento)
    
    
muchos_animales.add("Chancho")
print(muchos_animales)
#print(muchos_animales["Gato"])
muchos_animales.remove("Gato")#
#muchos_animales.remove("Leon")#KeyError: 'Leon'
print(muchos_animales)
muchos_animales.discard("Leon")
print(muchos_animales)
muchos_animales.pop()#Elimina un elemento al azar
print(muchos_animales)
muchos_animales.clear()
print(muchos_animales)#set()

print(muchos_animales.__dir__())
print("")
print(dir(muchos_animales))