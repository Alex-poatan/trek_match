""" Ejercicios de condicionales """
# Autor: Alexander_Valladares

# 1: Decisiones simples

edad = 18

if edad >= 18:
    print("Eres mayor de edad")

else:
    print("Eres menor de edad")

# 2: Decisión múltilple con elif

nota = input("Introduce tu nota (1-7): ")

if nota == "7":
    print("Excelente")

elif nota == "6":
    print("Muy bien")

elif nota == "5":
    print("Bien")

elif nota == "4":
    print("Suficiente")

else:
    print("Insuficiente")

#3. Condiciones anidadas

numero = int(input("Introduce un número entero: "))
if numero >= 0:
    if numero == 0:
        print("Es cero")
    else:
        print("Número positivo")
else:
        print("Número negativo")

#4. Condición de borde

numero = int(input("Introduce un valor entre 1 y 100: "))

if numero == 1 or numero == 100:
    print("Estás en un límite permitido")

elif numero > 1 and numero < 100:
    print("Dentro del rango")

else:
    print("Valor fuera de rango")







