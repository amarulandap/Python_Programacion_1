"""Calcular el área y el volumen de un prisma rectangular
    area = 2 * lado1 * lado2 + 2 * lado1 * lado3 + 2 * lado2 * lado3
    volumen = areaBase * altura

    lado1 + lado2 = base.
    lado3 = altura.
"""

"""Importar la función para la validación de los datos"""
from ValidacionDatos import validarDatoReal


lado1 = validarDatoReal("Ingrese el valor del lado1 de la base: ")

lado2 = validarDatoReal("Ingrese el valor del lado2 de la base: ")

"""Calcular el área de la base"""
areaBase = lado1 * lado2

altura = validarDatoReal("Ingrese el valor de la altura del prisma rectangular: ")

"""Calcular el volumen del prisma rectangular"""
volumen = areaBase * altura

print("El volumen del prisma rectangular es: ", volumen)

"""Calcular el área total del prisma"""
area = 2 * (lado1 * lado2 + lado1 * altura + lado2 * altura)

print("El área total del prisma rectangular es: ", area)







