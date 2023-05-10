""" 7-Crea una función llamada imprimir_pares que tome un número entero como
parámetro y imprima todos los números pares desde 1 hasta ese número. """


def imprimir_pares(hasta):
    for numero in range(1, hasta+1):
        if numero % 2 == 0:
            print(numero, end=", ")

imprimir_pares(hasta=20)