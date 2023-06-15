"""Programa para calcular el mayor valor de los pesos de los paquetes que se encuentran en una bodega
    n = Número de paquetes.
    pesoMayor = paquete de mayor peso.
    pesoPaquete = peso de cada paquete.
"""

import ValidacionDatos

# Validamos que el cliente este ingresando un número entero.
n = ValidacionDatos.validarDatoEntero("Número de paquetes en bodega: ")

pesoMayor = 0       # Asignar un valor inicial a peso mqyor para poderlo comparar con los datos ingresados por el usuario.

if n > 0:
    contador = 0
    while contador < n:
        pesoPaquete = ValidacionDatos.validarDatoReal("Peso del paquete (Kgs): ")      # Validamos que el peso es un dato numerico.
        if pesoPaquete > 0:
            if pesoPaquete > pesoMayor:
                pesoMayor = pesoPaquete
        else:
            print("Error, el peso del paquete debe ser mayor que 0")
            contador -= 1

        contador += 1

    print("El peso mayor es: ", pesoMayor)
else:
    print("Ingrese un valor mayor a 0.")
