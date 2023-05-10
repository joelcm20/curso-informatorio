""" 19-Crea una función llamada es_bisiesto que tome un año como parámetro y
devuelva Bisiesto si el año es bisiesto, o No es Bisiesto en caso contrario. Un año
es bisiesto si es divisible por 4, pero no por 100, a menos que también sea
divisible por 400. """


def es_bisiesto(year):
    if year % 4 == 0 and year % 100 == 0 and year % 400 == 0:
        return "Bisiesto"
    elif year % 4 == 0 and not year % 100 == 0:
        return "Bisiesto"
    else:
        return "No es bisiesto"

print(es_bisiesto(2016))