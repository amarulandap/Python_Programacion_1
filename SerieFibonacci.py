"""Programa para generar n cantidad de terminos de la serie y sumarlos
    n: Numero de terminos de la serie.
    suma: Sumatoria de los n terminos.
"""

# Importar el programa para validar los datos enteros.
from ValidacionDatos import validarDatoEntero

# Ingresar la cantidad de terminos de la serie.
n = validarDatoEntero("Ingrese la cantidad de terminos a generar: ")

if n > 0:                  # Numero de terminos sea superior a cero.
    listaFibonacci = []    # Lista para almacenar los terminos generados y luego sumarlos.
    suma = 0

    if n == 1:
        listaFibonacci.append(1)  # Agregar un termino al final de la lista.
        suma = 1      # Variable donde almacenamos la sumatoria de los terminos.
    elif n == 2:
        listaFibonacci.extend([1, 1])       # Agregar una nueva lista al final de la existente.
        suma = 2
    else:
        listaFibonacci.extend([1, 1])
        contador = 2

        while contador < n:
            nuevoTermino = listaFibonacci[contador - 2] + listaFibonacci[contador - 1]
            listaFibonacci.append(nuevoTermino)

            contador += 1

        for i in range (n):
            suma += listaFibonacci[i]

    print("Serie Fibonacci con", n, "termino(s): ", listaFibonacci)
    print("la suma de los terminos es = ", suma)

else:
    print("Error, ingrese un valor mayor que cero.")


