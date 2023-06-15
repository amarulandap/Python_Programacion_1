"""Programa para calcular la nota definitiva de un alumno
    nota examenes = 70%.
    nota lecciones = 20%.
    nota tareas = 10%.

    Semestre: 3 exámenes, 2 lecciones, 3 tareas.
"""

"""Importar las funciones para validar los datos númericos"""
import ValidacionDatos

"""Crear la función para calcular el promedio de cada una de las notas"""
def promedios(numeroNotas, mensaje):

    nota = 0                                        # acumulador para las notas ingresadas por el usuario.
    contador = 0
    while contador < numeroNotas:                   # cantidad de notas para promediar.
        nota += ValidacionDatos.validarDatoReal(mensaje)
        contador += 1

    promedio = nota / numeroNotas                   # calcular el promedio obtenido para cada tipo de notas.

    return promedio

"""Crear una función para calcular el aporte de cada item a la nota final"""
def pesoItem():

    invitacion = "Ingrese el porcentaje de peso de la nota: "  # Ingresar el peso en la nota final.
    porcentaje = ValidacionDatos.validarDatoEntero(invitacion)

    porcentajeItem = porcentaje / 100                          # Peso de cada item en la nota final.

    return porcentajeItem


mensajeExamenes = "Ingrese la nota del examen: "    # Para pedir el ingreso de cada una de las notas.
numeroNotas = ValidacionDatos.validarDatoEntero("Ingrese la cantidad de notas: ")  # Número de examenes.
promedioExamenes = promedios(numeroNotas, mensajeExamenes)
porcentajeExamenes = pesoItem()


mensajeLecciones = "Ingrese la nota de la lección: "    # Para pedir el ingreso de cada una de las notas de las lecciones.
numeroNotas = ValidacionDatos.validarDatoEntero("Ingrese la cantidad de notas: ")  # Número de lecciones.
promedioLecciones = promedios(numeroNotas, mensajeLecciones)
porcentajeLecciones = pesoItem()

mensajeTareas = "Ingrese la nota de la tarea: "         # Para pedir cada una de las notas de las tareas.
numeroNotas = ValidacionDatos.validarDatoEntero("Ingrese la cantidad de notas: ")   # Número de tareas.
promedioTareas = promedios(numeroNotas, mensajeTareas)
porcentajetareas = pesoItem()

notaDefinitiva = promedioExamenes * porcentajeExamenes + promedioLecciones * porcentajeLecciones + promedioTareas * porcentajetareas
print("la definitiva del alumno es: ", notaDefinitiva)

