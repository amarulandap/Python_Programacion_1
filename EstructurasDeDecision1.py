"""Construir un programa que según el valor del radio y la altura de un cilindro, calcule el área o el
    volumen del mismo.
"""

"""Importar las funciones para validación de datos"""
import ValidacionDatos

PI = 3.1416

"""Ingresar el valor del radio y de la altura"""
radioCilindro = ValidacionDatos.validarDatoReal("Ingrese el radio de la base del cilindro: ")

alturaCilindro = ValidacionDatos.validarDatoReal("Ingrese la altura del cilindro: ")

if radioCilindro > 0 and alturaCilindro > 0:
    if radioCilindro < alturaCilindro:
        volumenCilindro = PI * alturaCilindro * pow(radioCilindro, 2)
        print("El volumen del cilindro es: ", volumenCilindro)

    elif alturaCilindro < radioCilindro:
        areaCilindro = 2 * PI * radioCilindro * (alturaCilindro + radioCilindro)
        print("El area del cilindro es: ", areaCilindro)

    else:
        print("la altura y el radio son iguales")
else:
    print("Error, el radio y la altura deben ser valores positivos")

