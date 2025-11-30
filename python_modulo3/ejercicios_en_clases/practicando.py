#suma = 10 + 5
#resta = 10 - 5
#multiplicacion = 10 * 5
#division = 10 / 5
#potencia = 2**3
#modulo = 10 % 3

#print(f"""Suma: {suma}
#Resta: {resta}
#Multiplicacion: {multiplicacion}
#Division: {division}
#Potencia: {potencia}
#Modulo: {modulo}""")

#nombre = "Ana"
#apellido = "Gomez"
#nombre_completo = nombre + " " + apellido
#print(nombre_completo)

#risa = "ja" * 4
#print(risa)
#================

#nombre = input("¿Cómo te llamas?")
#print("Hola " + nombre + ", bienvenido a Python!")

#edad_texto = input("¿Cuántos años tienes?")

#edad_numero = int(edad_texto)
#print("El proximo año tendrás", edad_numero + 1, "años.")

#=====================
#Crear una lista
#frutas = ["manzana", "banana", "cereza"]
#numeros = [1, 2, 3, 4, 5]
#mezclado = ["texto", 42, True, 3.14]

#Acceder a elemtnos (comienaza en 0)
#print(frutas[0])  # manzana
#print(frutas[1])  # banana
#print(frutas[-1])  # True

#Modificar
#frutas[0] = "pera"
#print(frutas)

#Añadir elementos
#frutas.extend(["coca", "mariwana", "luna"])
#print(frutas)

#Cuántos elementos tiene
#print(len(frutas))

#=====================

#Condicionales

#edad = 18

#if edad >= 18:
#    print("Eres mayor de edad.")
#else:
#    print("Eres menor de edad.")

#Con multiples condiciones

#nota = input("Introduce tu nota (1.0 - 7.0): ")
#nota = float(nota)

#if nota >= 7.0:
#    print("Sobresaliente")
#elif nota >= 3.9:
#    print("Aprobado")
#else:
#    print("Suspenso")

#=========================

#Ciclos

#FOR  - cuando sabes cuántas veces repetir
#for i in range(5):  # 0, 1, 2, 3, 4
#    print("Iteración número:", i)


#WHILE - mientras una condición sea verdadera

#contador = 0
#while contador < 10:
#    print("Contador es:", contador)
#    contador = contador + 2

#=========================

#Funciones

#definir una función

def saludar():
    print("Hola, bienvenido a la función de saludo.")

#usar la funcion

saludar()

#funcion con parámetros
def saludar_persona(nombre):
    print(f"Hola {nombre}, bienvenido.")

saludar_persona("Carlos")

#Función que devuelve un valor

def sumar(a, b):
    resultado = a + b
    return resultado

suma_total = sumar(5, 7)
print("La suma es:", suma_total)






