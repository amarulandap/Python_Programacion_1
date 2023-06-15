"""Programa para encontrar la mayor de 3 notas obtenidas por un estudiante
    nota1, nota2, nota3 = Notas obtenidas por el estudiante.
    mayor = nota mayor.
"""

from ValidacionDatos import validarDatoReal

nota1 = validarDatoReal("Nota 1: ")
nota2 = validarDatoReal("Nota 2: ")
nota3 = validarDatoReal("Nota 3: ")

if nota1 >= 0 and nota2 >= 0  and nota3 >= 0:
    if nota1 >= nota2:
       if nota1 >= nota3:
           mayor = nota1
       else:
           mayor = nota3
    elif nota2 >= nota3:
        mayor = nota2
    else:
        mayor = nota3

    print("La mayor nota es: ", mayor)
else:
    print("Recuerde que las notas deben ser mayores o iguales a 0")




