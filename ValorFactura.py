"""Programa para calcular al valor de una factura, según la cantidad de Kw consumidos por una familia"""

# Importar las funciones para la validación de los datos.
from ValidacionDatos import validarDatoReal

# Solicitar se ingrese el valor del kilovatioHora.
valorKilovatio = validarDatoReal("Ingrese el valor del Kilovatio / Hora: ")

# Solicitar se ingrese la cantidad de kilovatios consumidos.
kilovatioHora = validarDatoReal("Ingrese la cantidad de kilovatios consumidos: ")


if kilovatioHora >= 0:
    if kilovatioHora > 700:
        valorKilovatio += (0.05 * valorKilovatio)               # Calculamos el incremento dado el consumo superior a 700.

    valorFactura = valorKilovatio * kilovatioHora               # Almacenamos el valor de la factura.
    print("El valor de la factura es: " + str(valorFactura))    # Casteo o conversión explicita.
else:
    print("Error, ingrese una cantidad de kilovatios consumidos positiva.")



