"""Calculadora"""

print("Calculadora")

# pedir datos

nombre = input("Ingresa tu nombre: ")
edad_actual = input("Ingresa tu edad actual: ")
edad_actual = int(edad_actual)

# calcular

edad_en_10_anos = edad_actual + 10
edad_en_20_anos = edad_actual + 20

# mostrar resultados

print("\nHola", nombre)
print("Actualmente tienes", edad_actual, "años.")
print("En 10 años tendrás", edad_en_10_anos, "años.")
print("En 20 años tendrás", edad_en_20_anos, "años.")

# condicional
if edad_actual < 18:
    print("Eres menor de edad.")
else:
    print("Eres mayor de edad.")

