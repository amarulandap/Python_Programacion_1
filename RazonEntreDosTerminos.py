"""Calcular la razón entre dos terminos consecutivos de una progresión aritmética"""

"""Importar la función para validar los datos ingresados por los usuarios"""
from ValidacionDatos import validarDatoEntero

u = validarDatoEntero("Ingrese el enésimo término de la progresión: ")

a = validarDatoEntero("Ingrese el primer término de la progresión: ")

n = validarDatoEntero("Ingrese la cantidad de terminos de la progresión: ")

"""Calcular la razón"""
if n != 1:
    razon = (u - a) / (n - 1)
    print("Razón = ",razon)
else:
    print("Error, la progresión solo tiene un término")

