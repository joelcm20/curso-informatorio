""" 18-Escribe un programa que pida al usuario un número y luego imprima un
triángulo de números como el siguiente:
1
2 3
4 5 6
7 8 9 10 """

numero = int(input("Ingresar numero: "))
triangulo = ""

count1 = 1  # salto de linea cuando es == n
count2 = 0  # contador de saltos de linea
for n in range(1, numero+1):
    triangulo += str(n)+" "
    if count1 == n:
        triangulo += "\n"
        count2 += 1
        count1 += count2+1

print(triangulo)