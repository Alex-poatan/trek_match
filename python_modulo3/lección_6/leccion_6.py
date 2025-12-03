"""programa para ingresar notas de los alumnos, ¿cuantos datos ingresará?,
    ingresar datos uno por uno,
    mostrar resultado cantidad de notas mayores que el promedio"""


def main():
    cantidad_notas = int(input("¿Cuántas notas va a ingresar? ")) # Pedir cantidad de notas
    notas = [] # Lista para almacenar las notas

    # Ingresar las notas una por una
    for i in range(cantidad_notas): # Bucle para ingresar cada nota
        nota = float(input(f"Ingrese la nota {i + 1}: ")) # Pedir la nota
        notas.append(nota) # Agregar la nota a la lista

    promedio = sum(notas) / cantidad_notas # Calcular el promedio
    print(f"El promedio de las notas es: {promedio:.2f}") # Mostrar el promedio

    notas_mayores_promedio = [nota for nota in notas if nota > promedio] # Filtrar notas mayores que el promedio
    cantidad_mayores = len(notas_mayores_promedio)  # Contar notas mayores que el promedio

    print(f"La cantidad de notas mayores que el promedio es: {cantidad_mayores}") # Mostrar la cantidad
    if cantidad_mayores > 0: # Si hay notas mayores que el promedio
        print("Las notas mayores que el promedio son:")     # Mostrar las notas mayores que el promedio
        for nota in notas_mayores_promedio:               # Bucle para mostrar cada nota
            print(nota) # Mostrar la nota

if __name__ == "__main__": # Ejecutar la función principal
    main() # Llamar a la función main


