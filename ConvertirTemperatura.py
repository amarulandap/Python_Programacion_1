"""Programa para pasar grados centigrados a farenheit y viceversa"""

"""Importar las funciones de validación de datos"""
import ValidacionDatos

"""Pedirle al usuario que seleccione la opción de conversión"""
# \indicamos que es un único mensaje
mensajeOpcion = "Seleccione una opción:\n" \
                "1. Convertir a grados Centigrados.\n" \
                "2. Convertir a grados Farenheit.\n" \
                ": "


codigo = ValidacionDatos.validarDatoEntero(mensajeOpcion)       # validamos que se ingresa un dato entero

mensajeTemperatura = "Ingrese el valor de la temperatura: "
temperatura = ValidacionDatos.validarDatoReal(mensajeTemperatura)   # validamos que se ingresa un dato numerico.

if codigo == 1:
    temp = (5 / 9) * (temperatura - 32)
    print("Temperatura = " + str(temp) + " grados celsius")
elif codigo == 2:
    temp = 32 + (9 * temperatura) / 5
    print("Temperatura = " + str(temp) + " grados farenheit")
else:
    print("Error, seleccione una de las dos opciones")





