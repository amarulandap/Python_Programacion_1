"""Programa para contar la cantidad de personas que votaron a favor y en contra de una consulta
    n = Número de personas que votaron la consulta
"""

from ValidacionDatos import validarDatoEntero

n = validarDatoEntero("Número de votantes: ")

contador = 0
votosAFavor = 0         # Almacenar la cantida de votos a favor.
votosEnContra = 0       # Alamcenar la cantidad de votos en contra.

if n > 0:
    while contador < n:
        mensajeOpcion = "\nSeleccione una opcion:\n" \
                        "1. A favor. \n" \
                        "2. En contra \n" \
                        ": "

        opcion = validarDatoEntero(mensajeOpcion)
        if opcion == 1:
            votosAFavor += 1
        elif opcion == 2:
            votosEnContra += 1
        else:
            print("\nError, seleccione una de las dos opciones")
            contador -= 1

        contador += 1

    print("Votantes: ", n)
    print("A favor: ", votosAFavor)
    print("En contra: ", votosEnContra)
else:
    print("La cantidad de votantes debe ser mayor que cero.")


