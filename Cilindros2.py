"""Calcular el diametro del cilindro
    v = volumen. float.
    h = altura. float.
    d = Diametro. float.
"""

import math

PI = 3.1416

"""Invocar una funcion que nos permita validar que los datos ingresados son correctos"""
from ValidacionDatos import validarDatoReal


"""Invocamos la función de validación para pedir los valores del volumen y de la altura"""


v = validarDatoReal("Ingrese el volumen del cilindro: ")

h = validarDatoReal("Ingrese la altura del cilindro: ")

if h != 0:
    resul = v / (PI * h)
    d = 2 * math.sqrt(resul)
else:
   d = 0

print("El diametro del cilindro es: ", d)