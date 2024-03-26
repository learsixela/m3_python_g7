"""
Diccionarios {}

estructura datos de pares clave:valor
se accede a los elementos a traves de la clave, no importa la posición
las claves no se generan automaticamente, no hay un orden
las claves pueden ser String, numerico, incluso Boolean
los valores pueden ser: String, numerico, boolean, listas, diccionario u otro tipo de datos
Si la clave existe,modifico su valor, si no existe se agrega el par clave:valor

"""
from os import system
diccionario = {
    1: "uno",
    "dos": 2,
    3: ["a","b","c"], # lista dentro de diccionario
    "dicc": {"A":"A Mayuscula"},
    }

#Diccionario vacio
notas = {}
print(len(notas))#cero

notas = {
    "Camila": 7,
    "Antonio": 5,
    "Felipe": 6,
    "Daniela": 5,
    "Vicente": 7,
    "FELIPE": 2,
    "Vicente": None,
}
system("clear")
print(len(notas))#
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 7}

#Acceso a los elementos(valores)
print(notas["Camila"]) #7
print(notas["Antonio"])#5
print(notas["Felipe"]) #6
print(notas["Daniela"])#5
print(notas["Vicente"])#1 reemplaza a 7
#print(notas["felipe"])#KeyError: 'felipe'

print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'FELIPE': 2}
notas["Julio"] = 4
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'FELIPE': 2, 'Julio': 4}

#julio = {"nota1":7,"nota2":4}

#Modificar par clave:valor
notas["Julio"] = 5
print(notas)#

#eliminar par clave:valor
del notas["FELIPE"]
print(notas)#{'Camila': 7, 'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'Julio': 5}

#2 forma pop()-> al eliminar, capturamos el valor
eliminado = notas.pop("Camila") #notas["Camila"]
print("valor eliminado : ",eliminado)#7
print(notas)#{'Antonio': 5, 'Felipe': 6, 'Daniela': 5, 'Vicente': 1, 'Julio': 5}
print("")
notas2 = {
    "Mijail":2,
    "Israel":1,
    "Felipe": 7,
    }

#notas.update(notas2)
#print(notas)#
notas2.update(notas)
print(notas2)#
#COLISIONES: al existir duplicidad de claves, se conserva el valor del dicionario anexado



