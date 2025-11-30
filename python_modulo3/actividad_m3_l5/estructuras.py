"""Actividad n° 5"""

#Autor: Alexander Valladares

#1. Crear estructuras
#Declara una variable de cada una de las siguientes estructuras de datos con al menos 3 elementos cada una:
#• Lista (list)
#• Tupla (tuple)
#• Conjunto (set)
#• Diccionario (dict)

mi_lista = [1, 2, 3]
mi_tupla = (4, 5, 6)
mi_conjunto = {7, 8, 9}

mi_diccionario = {'a': 10, 'b': 11, 'c': 12}



#Muestra cada estructura usando print() y comenta brevemente su diferencia principal.

#2. Acceder a elementos
#• Imprime el segundo elemento de la lista.
#• Imprime una clave y su valor desde el diccionario.
#• Explica con comentarios por qué no puedes acceder por índice a un set.

print("Lista:", mi_lista)
print("Tupla:", mi_tupla)
print("Conjunto:", mi_conjunto)
print("Diccionario:", mi_diccionario)
print("Segundo elemento de la lista:", mi_lista[1])
print("Valor de la clave 'b' en el diccionario:", mi_diccionario['b'])
# No se puede acceder por índice a un set porque los conjuntos son estructuras de datos no ordenadas,
# lo que significa que no mantienen un orden fijo de los elementos y no permiten acceso por posición

#3. Contar e iterar
#• Usa len() para mostrar la cantidad de elementos en cada estructura.
#• Itera sobre cada estructura usando un for y muestra cada elemento por pantalla.

print("Cantidad de elementos en la lista:", len(mi_lista))
print("Cantidad de elementos en la tupla:", len(mi_tupla))
print("Cantidad de elementos en el conjunto:", len(mi_conjunto))
print("Cantidad de elementos en el diccionario:", len(mi_diccionario))
print("Elementos en la lista:")
for elemento in mi_lista:
    print(elemento)
print("Elementos en la tupla:")
for elemento in mi_tupla:
    print(elemento)
print("Elementos en el conjunto:")
for elemento in mi_conjunto:
    print(elemento)

print("Elementos en el diccionario:")
for clave, valor in mi_diccionario.items():
    print(f"{clave}: {valor}")

#4. Modificar estructuras
#• Agrega un nuevo elemento a la lista y al conjunto.
#• Borra un elemento de la lista.
#• Agrega una nueva clave al diccionario.
#• Intenta modificar la tupla y comenta qué ocurre.

mi_lista.append(4)
mi_conjunto.add(10)
mi_lista.remove(2)
mi_diccionario['d'] = 13
# Las tuplas son inmutables, por lo que no se pueden modificar después de su creación.
# Cualquier intento de modificar una tupla resultará en un error.
print("Lista modificada:", mi_lista)
print("Conjunto modificado:", mi_conjunto)
print("Diccionario modificado:", mi_diccionario)
# Intento de modificar la tupla (esto generará un error si se descomenta)
# mi_tupla[0] = 100  # Esto no es posible y causará un TypeError
print("Tupla (inmutable):", mi_tupla)
print("Intentar modificar la tupla resultará en un error porque las tuplas son inmutables.")
