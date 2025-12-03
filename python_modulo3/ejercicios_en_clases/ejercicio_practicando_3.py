# #suma = 10 + 5
# #resta = 10 - 5
# #multiplicacion = 10 * 5
# #division = 10 / 5
# #potencia = 2**3
# #modulo = 10 % 3

# #print(f"""Suma: {suma}
# #Resta: {resta}
# #Multiplicacion: {multiplicacion}
# #Division: {division}
# #Potencia: {potencia}
# #Modulo: {modulo}""")

# #nombre = "Ana"
# #apellido = "Gomez"
# #nombre_completo = nombre + " " + apellido
# #print(nombre_completo)

# #risa = "ja" * 4
# #print(risa)
# #================

# #nombre = input("¿Cómo te llamas?")
# #print("Hola " + nombre + ", bienvenido a Python!")

# #edad_texto = input("¿Cuántos años tienes?")

# #edad_numero = int(edad_texto)
# #print("El proximo año tendrás", edad_numero + 1, "años.")

# #=====================
# #Crear una lista
# #frutas = ["manzana", "banana", "cereza"]
# #numeros = [1, 2, 3, 4, 5]
# #mezclado = ["texto", 42, True, 3.14]

# #Acceder a elemtnos (comienaza en 0)
# #print(frutas[0])  # manzana
# #print(frutas[1])  # banana
# #print(frutas[-1])  # True

# #Modificar
# #frutas[0] = "pera"
# #print(frutas)

# #Añadir elementos
# #frutas.extend(["coca", "mariwana", "luna"])
# #print(frutas)

# #Cuántos elementos tiene
# #print(len(frutas))

# #=====================

# #Condicionales

# #edad = 18

# #if edad >= 18:
# #    print("Eres mayor de edad.")
# #else:
# #    print("Eres menor de edad.")

# #Con multiples condiciones

# #nota = input("Introduce tu nota (1.0 - 7.0): ")
# #nota = float(nota)

# #if nota >= 7.0:
# #    print("Sobresaliente")
# #elif nota >= 3.9:
# #    print("Aprobado")
# #else:
# #    print("Suspenso")

# #=========================

# #Ciclos

# #FOR  - cuando sabes cuántas veces repetir
# #for i in range(5):  # 0, 1, 2, 3, 4
# #    print("Iteración número:", i)


# #WHILE - mientras una condición sea verdadera

# #contador = 0
# #while contador < 10:
# #    print("Contador es:", contador)
# #    contador = contador + 2

# #=========================

# #Funciones

# #definir una función

# #def saludar():
# #    print("Hola, bienvenido a la función de saludo.")

# #usar la funcion

# #saludar()

# #funcion con parámetros
# #def saludar_persona(nombre):
# #    print(f"Hola {nombre}, bienvenido.")

# #saludar_persona("Carlos")

# #Función que devuelve un valor

# #def sumar(a, b):
# #    resultado = a + b
# #    return resultado

# #suma_total = sumar(5, 7)
# #print("La suma es:", suma_total)
# #=========================

# #def sumar(a, b):
# #    return a + b

# #resultado = sumar(3, 4)
# #print("El resultado de la suma es:", resultado)

# #==========================

# class Estudiante: #Clase_el_molde

#     institucion = "Universidad Autónoma de Chile" #Atributo de clase


#     def __init__(self, nombre, edad, carrera): #Método constructor

#         #atributos de instancia
#         self.nombre = nombre
#         self.edad = edad
#         self.carrera = carrera
#         self.notas = []  #lista vacía para almacenar notas


#     #metodo (acciones que puede hacer)

#     def agregar_nota(self, nota):
#         self.notas.append(nota)
#         return f"Nota {nota} agregada para {self.nombre}."

#     def calcular_promedio(self):
#         if len(self.notas) == 0:
#             return 0
#         return sum(self.notas) / len(self.notas)

# #crear una instancia de la clase Estudiante

# estudiante1 = Estudiante("Alex", 32, "Ingeniería civil industrial")


# #usar atributos

# print(estudiante1.nombre)  # Alex


# #usar métodos

# print(estudiante1.agregar_nota(6.5),
# estudiante1.agregar_nota(5.0),
# estudiante1.agregar_nota(4.5))
# print(f"Promedio de {estudiante1.nombre}: {estudiante1.calcular_promedio()}")











