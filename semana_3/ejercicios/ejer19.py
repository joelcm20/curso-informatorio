""" 19-Escribe un programa que pida al usuario un número y luego imprima si ese
número es un número perfecto o no. Un número perfecto es aquel que es igual a
la suma de sus divisores propios (excluyendo el propio número).
Los números perfectos son aquellos iguales a la suma de sus divisores: 6 se
puede dividir por 1, 2 y 3, y cuando sumas esos números, el resultado es 6 """

numero = int(input("Ingresar numero: "))
divisores = []
perfecto = False

for n in range(1, numero):
    if numero % n == 0:
        divisores.append(n)

if sum(divisores) == numero:
    perfecto = True

print(f"El numero {numero} es perfecto: {perfecto}")