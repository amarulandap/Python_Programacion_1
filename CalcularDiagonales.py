"""Programa para calcular las diagonales de un bloque rectangular"""

"""Importar las funciones para validación de datos"""
from ValidacionDatos import validarDatoEntero

"""Importar el paquete math para la raiz cuadrada"""
import math

"""Solicitar el valor de los lados"""
mensajelado1 = "Ingrese la longitud del lado 1 en cms: "
lado1 = validarDatoEntero(mensajelado1)
mensajelado2 = "Ingrese la longitud del lado 2 en cms: "
lado2 = validarDatoEntero(mensajelado2)
mensajelado3 = "Ingrese la longitud del lado 3 en cms: "
lado3 = validarDatoEntero(mensajelado3)

if lado1 > 0 and lado2 > 0 and lado3 > 0:
    # calcular la diagonal principal
    diagonal = math.sqrt(pow(lado1, 2) + pow(lado2, 2) + pow(lado3, 2))
    print("Diagonal =", diagonal, "cms")

    # calcular la primera diagonal.
    d1 = math.sqrt(pow(lado1, 2) + pow(lado2, 2))
    print("d1 =", d1, "cms")

    # calcular la segunda diagonal
    d2 = math.sqrt(pow(lado1, 2) + pow(lado3, 2))
    print("d2 =", d2, "cms")

    # calcular la tercera diagonal
    d3 = math.sqrt(pow(lado2, 2) + pow(lado3, 2))
    print("d3 =", d3, "cms")
else:
    print("Error, ingrese valores mayores que cero para las longitudes de los lados.")




