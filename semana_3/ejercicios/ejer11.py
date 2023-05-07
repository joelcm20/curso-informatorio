""" 11-Escribe un programa que pida al usuario un número y calcule su factorial.
Un factorial es el producto que resulta de multiplicar un número entero positivo
dado por todos los enteros inferiores a él hasta el uno. Por ejemplo, el factorial
de 4 es 4! = 4 x 3 x 2 x 1 = 24. """

numero = int(input("Ingresar un numero: "))
lista_numero = range(1, numero+1)
factorial = 0


i = 0
while i < len(lista_numero)-1:
    if factorial < 1:
        factorial = lista_numero[i]*lista_numero[i+1]
    else:
        factorial = factorial * lista_numero[i+1]
    i += 1

print(f"Factorial de {numero} es: {factorial}")
