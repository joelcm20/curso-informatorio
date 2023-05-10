""" 18-Crea una función llamada calcular_mayor_diferencia que tome una lista de
números como parámetro y devuelva la mayor diferencia entre el numero mas
alto y el numero mas bajo en la lista. """


def calcular_mayor_diferencia(lista):
    return max(lista) - min(lista)


print(calcular_mayor_diferencia([19, 45, 33, 12, 21, 43, 6, 1, 22]))
