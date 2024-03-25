"""
Diccionarios {}

estructura datos de pares clave:valor
se accede a los elementos a traves de la clave, no importa la posición
las claves no se generan automaticamente, no hay un orden
las claves pueden ser String, numerico, incluso Boolean
los valores pueden ser: String, numerico, boolean, listas, diccionario u otro tipo de datos
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
    "Vicente": 1,
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
