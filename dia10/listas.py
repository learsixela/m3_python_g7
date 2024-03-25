""" 
LISTAS 
[]->listas
()->tuplas
{}->diccionarios
Son contenedores de datos
Son mutable
conjunto de datos,separados por coma,ordenado segun su ingreso
la primera posicion(INDICE) es cero
"""
from os import system

lista_pares= [2,4,6,8,10]
#tamaño de la lista es 5
print(len(lista_pares)) #imprime el tamaño

print(lista_pares)
print([2,4,6,8,10])
#indice o posicion
print(lista_pares[0])#2
print(lista_pares[1])#4
print(lista_pares[2])#6
print(lista_pares[3])#8
print(lista_pares[4])#10
#print(lista_pares[5])#IndexError: list index out of range
print("")
print(lista_pares[-1])#5
print(lista_pares[-2])#

lista_vacia=[]#tamaño es cero

#METODOS
print(lista_pares.__dir__)#<built-in method __dir__ of list object at 0x108008900
print(lista_pares.__dir__())
print("")
#append(dato)=>agregar un elemento al final de la lista
lista_vacia.append("Lunes")
lista_pares.append(13)
print(lista_vacia)
lista_vacia.append("Martes")
lista_vacia.append("Miercoles")
print(lista_vacia)
system("clear")# o system("cls") para windows
#insert(indice,elemento) => inserta un elemento en una posicion especifica
lista_vacia.insert(3,"Jueves")
print(lista_vacia)#['Lunes', 'Martes', 'Miercoles', 'Jueves']
lista_vacia.insert(3,"Viernes")
print(lista_vacia)#['Lunes', 'Martes', 'Miercoles', 'Viernes', 'Jueves']
lista_vacia[3]="Jueves"#Reemplazar el elemento en esa posicion
#lista_vacia[6]="Jueves"#IndexError: list assignment index out of range

print(lista_vacia)#['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Jueves']
lista_vacia.insert(10,"Sabado")
print(lista_vacia)#['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Jueves', 'Sabado']

system("clear")
#pop()=> saca el ultimo elemento dentro de la lista, si no se pasa un indice
lista_vacia.pop()
print(lista_vacia)#['Lunes', 'Martes', 'Miercoles', 'Jueves', 'Jueves']
lista_vacia.pop(4)
print(lista_vacia)#['Lunes', 'Martes', 'Miercoles', 'Jueves']

lista_eliminados = []
eliminado=lista_vacia.pop(0)#Lunes
lista_eliminados.append(eliminado)
print(f"El elemento eliminado {eliminado}")
print(lista_vacia)#['Martes', 'Miercoles', 'Jueves']
print(lista_eliminados)#['Lunes']

system("clear")
#remove(valor) => elimina un valor
lista_vacia.remove("Martes")
print(lista_vacia)#['Miercoles', 'Jueves']
#lista_vacia.remove("Viernes")#ValueError: list.remove(x): x not in list
lista_vacia.append("Jueves")
print(lista_vacia)#['Miercoles', 'Jueves', 'Jueves']
lista_vacia.remove("Jueves")#elimina la primera coincidencia, de izq a derecha
print(lista_vacia)#['Miercoles', 'Jueves']
system("clear")
lista_vacia.insert(0,"Martes")
lista_vacia.insert(0,"Lunes")
lista_vacia.append("Viernes")
lista_vacia.append("Sabado")
lista_vacia.append("Domingo")

#reverse()=>  invierte los elementos de la lista, el cambio es permanente
lista_vacia.reverse()
print(lista_vacia)#['Domingo', 'Sabado', 'Viernes', 'Jueves', 'Miercoles', 'Martes', 'Lunes']

#sort()=> Ordena los elementos de forma ascendente/alfabeticamente
lista_vacia.sort()
print(lista_vacia)#['Domingo', 'Jueves', 'Lunes', 'Martes', 'Miercoles', 'Sabado', 'Viernes']

lista_pares.sort()
print(lista_pares)#[2, 4, 6, 8, 10, 13]
print(lista_vacia)#