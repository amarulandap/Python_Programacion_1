"""Calcular el área y el volumen de un cilindro
    r = radio del cilindro. float.
    h = altura del cilindro. float.
"""
import sys

r = 0
h = 0
PI = 3.1416

try:
    r = float(input("Ingrese el valor del radio del cilindro: "))
    h = float(input("Ingrese el valor de la altura del cilindro: "))
except:
    print("valor erroneo", file=sys.stderr)
    r = 0
    h = 0
else:
    area = 2 * PI * r * (h + r)
    volumen = PI * h * pow(r, 2)

    print("El área del cilindro es: ", area)
    print("El volumen del cilindro es: ", volumen)