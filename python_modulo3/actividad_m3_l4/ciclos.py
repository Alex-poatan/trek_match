""" Actividad n° 4"""
#Autor: Alexander Valladares

#1. Uso básico de while
#Escribe un programa que imprima los números del 1 al 5 usando un ciclo while.

contador = 1  # Inicializa el contador en 1
while contador <= 5:  # Condición para que el ciclo continúe mientras el contador sea menor o igual a 5
    print(contador)  # Imprime el valor actual del contador
    contador += 1  # Incrementa el contador en 1 para evitar un ciclo infinito


#2. Uso básico de for
#Escribe un ciclo for que recorra una lista de frutas (["manzana", "plátano", "naranja"]) y las imprima en pantalla.

frutas = ["manzana", "plátano", "naranja"]  # Lista de frutas
for fruta in frutas:  # Recorre cada fruta en la lista
    print(fruta)  # Imprime la fruta actual


#3. Condición en un ciclo
#Crea un ciclo for que recorra los números del 1 al 10. Si encuentra un número par, imprime "Par", si es impar, imprime "Impar".

for numero in range(1, 11):  # Recorre los números del 1 al 10
    if numero % 2 == 0:  # Verifica si el número es par
        print(f"{numero} es Par")  # Imprime que el número es par
    else:
        print(f"{numero} es Impar")  # Imprime que el número es impar

#4. Ciclo infinito controlado con break
#Escribe un ciclo while True que solicite ingresar un número. El ciclo debe terminar si el número ingresado es 0. Usa break para salir.

while True:  # Inicia un ciclo infinito
    numero = int(input("Ingresa un número (0 para salir): "))  # Solicita al usuario ingresar un número
    if numero == 0:  # Verifica si el número es 0
        break  # Sale del ciclo si el número es 0
    print(f"Número ingresado: {numero}")  # Imprime el número ingresado

#5. Ciclo anidado
#Escribe un programa que imprima una tabla de multiplicar del 1 al 3, usando un ciclo for dentro de otro for.

for i in range(1, 4):  # Recorre los números del 1 al 3 para la tabla de multiplicar
    print(f"Tabla de multiplicar del {i}:")  # Imprime el encabezado de la tabla
    for j in range(1, 11):  # Recorre los números del 1 al 10 para multiplicar
        print(f"{i} x {j} = {i * j}")  # Imprime el resultado de la multiplicación
    print()  # Imprime una línea en blanco para separar las tablas

#6. Uso de continue
#Recorre una lista de nombres. Si el nombre es "Juan", omítelo usando continue. Imprime todos los demás.

nombres = ["Ana", "Juan", "Pedro", "María"]  # Lista de nombres
for nombre in nombres:  # Recorre cada nombre en la lista
    if nombre == "Juan":  # Verifica si el nombre es "Juan"
        continue  # Omite el nombre "Juan" y pasa a la siguiente iteración
    print(nombre)  # Imprime el nombre actual
