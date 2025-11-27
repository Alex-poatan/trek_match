#Autor: Alexander_Valladares

""" 1: Primeros pasos en Python"""

import math # Importar el módulo math para operaciones matemáticas

# 1 Imprimir un mensaje inicial

saludo_inicial = "¡Hola! Este es mi primer programa en Python." # Mensaje de saludo inicial

print(saludo_inicial) # Imprimir el mensaje de saludo inicial

#=================================

# 2 Declarar variables simples

nombre = "Alexander" # Declarar variable nombre
edad = 32 # Declarar variable edad
ciudad = "Santiago" # Declarar variable ciudad

print("Nombre:", nombre, "Edad:", edad, "Ciudad:", ciudad)

#=================================

# 3 Realizar operaciones básicas

x = 10 # Declarar variable x
y = 5 # Declarar variable y

print("Suma:", x + y)
#=================================

# 4 Explorar un módulo integrado

x = 16

def raiz_de_numero(numero): # Función para calcular la raíz cuadrada
    return math.sqrt(numero) # Usar la función sqrt del módulo math

print("La raíz cuadrada de", x, "es", raiz_de_numero(x))

#=================================
