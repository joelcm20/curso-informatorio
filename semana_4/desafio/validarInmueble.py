def ValidarAnio(anio):
    anio = str(anio)
    if not anio.isdigit():
        return True, "ERROR: El año ingresado debe ser in digito"
    if int(anio) < 2000:
        return True, "ERROR: El año ingresado debe ser mayor a 2000"
    return False, None


def ValidarMetros(metros):
    metros = str(metros)
    if not metros.isdigit():
        return True, "ERROR: Los metros ingresados debe ser in digito"
    if int(metros) < 60:
        return True, "ERROR: Los metros ingresados debe ser mayor o 59"
    return False, None


def ValidarHabitaciones(habitaciones):
    habitaciones = str(habitaciones)
    if not habitaciones.isdigit():
        return True, "ERROR: Las habitaciones ingresadas deben ser un digito"
    if int(habitaciones) < 2:
        return True, "ERROR: Las habitaciones deben ser mayor a 1"
    return False, None


def ValidarZonas(opcion):
    opcionesZona = {"1": "A", "2": "B", "3": "C"}
    if not opcion in opcionesZona.keys():
        return True, "ERROR: La opcion no es valida."
    return False, opcionesZona[opcion]

def ValidarEstado(opcion):
    opcionesEstado = {"1": "Disponible", "2": "Reservado", "3": "Vendido"}
    if not opcion in opcionesEstado.keys():
        return True, "ERROR: La opcion no es valida."
    return False, opcionesEstado[opcion]