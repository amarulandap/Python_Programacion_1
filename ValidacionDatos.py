"""Este archivo solo contendrá funciones para validar datos númericos"""

import sys

def validarDatoReal(invitacion):

    try:
        valor = float(input(invitacion))
    except ValueError as e:
        print("valor erroneo", file=sys.stderr)
        sys.exit()

    return valor

def validarDatoEntero(invitacion):

    try:
        valor=int(input(invitacion))
    except ValueError as e:
        print("Valor Erroneo", file=sys.stderr)
        sys.exit()

    return valor

