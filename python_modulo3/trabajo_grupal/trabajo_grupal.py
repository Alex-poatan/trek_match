"""Ejercicio 1"""

#Al ingresar un numero par cualquiera que sea del 2 al 100, este imprima en pantalla todos los
#números pares siguientes, y si ingreso un número impar cualquiera sea del 1 al 99 se imprima en
#pantalla todos los números impares siguientes hasta el 99.
#Si ingreso el 0 o un número menor y si ingreso un número mayor al 100, el programa debe enviar un
#mensaje de que no es posible realizarlo y volver a preguntar por el ingreso del número.

def imprimir_numeros():
    while True:
        try:
            numero = int(input("Ingrese un número entre 1 y 100 (0 o menor para salir): "))
            if numero <= 0 or numero > 100:
                print("Número no válido. Por favor, ingrese un número entre 1 y 100.")
                continue

            if numero % 2 == 0:  # Número par
                print("Números pares siguientes:")
                for i in range(numero, 101, 2):
                    print(i)
            else:  # Número impar
                print("Números impares siguientes:")
                for i in range(numero, 100, 2):
                    print(i)
            break
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

imprimir_numeros()

"""Ejercicio 2"""

#Realizar un programa que lea por teclado las 5 notas obtenidas por un alumno (comprendidas entre
#0 y 10). A continuación, debe mostrar todas las notas, la nota media, la nota más alta que ha sacado
#y la menor.

def procesar_notas():
    notas = []
    for i in range(5):
        while True:
            try:
                nota = float(input(f"Ingrese la nota {i+1} (entre 0 y 10): "))
                if 0 <= nota <= 10:
                    notas.append(nota)
                    break
                else:
                    print("Nota no válida. Debe estar entre 0 y 10.")
            except ValueError:
                print("Entrada no válida. Por favor, ingrese un número.")

    nota_media = sum(notas) / len(notas)
    nota_maxima = max(notas)
    nota_minima = min(notas)

    print("Notas ingresadas:", notas)
    print(f"Nota media: {nota_media}")
    print(f"Nota más alta: {nota_maxima}")
    print(f"Nota más baja: {nota_minima}")

procesar_notas()

"""Ejercicio 3"""

#Crea un programa que pida un número al usuario un número de mes (por ejemplo, el 4) y diga
#cuántos días tiene (por ejemplo, 30) y el nombre del mes. Debes usar listas. Para simplificarlo vamos
#a suponer que febrero tiene 28 días.

def dias_del_mes():
    meses = [
        ("Enero", 31),
        ("Febrero", 28),
        ("Marzo", 31),
        ("Abril", 30),
        ("Mayo", 31),
        ("Junio", 30),
        ("Julio", 31),
        ("Agosto", 31),
        ("Septiembre", 30),
        ("Octubre", 31),
        ("Noviembre", 30),
        ("Diciembre", 31)
    ]

    while True:
        try:
            numero_mes = int(input("Ingrese un número de mes (1-12): "))
            if 1 <= numero_mes <= 12:
                nombre_mes, dias = meses[numero_mes - 1]
                print(f"{nombre_mes} tiene {dias} días.")
                break
            else:
                print("Número no válido. Por favor, ingrese un número entre 1 y 12.")
        except ValueError:
            print("Entrada no válida. Por favor, ingrese un número entero.")

dias_del_mes()





