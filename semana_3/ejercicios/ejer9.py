""" 9-Escribe un programa que pida al usuario un número y luego imprima la
secuencia de Fibonacci correspondiente a ese número. """

numero = int(input("Ingresa un numero: "))
secuencia_fibonacci = [0, 1]
i = 2
while len(secuencia_fibonacci) < numero:
    len_fibonacci = len(secuencia_fibonacci)
    ultimo = secuencia_fibonacci[len_fibonacci-1]
    ante_ultimo = secuencia_fibonacci[len_fibonacci-2]
    siguiente = ultimo + ante_ultimo
    secuencia_fibonacci.append(siguiente)
print(f"Secuenia fibonacci de {numero}: ")
print(secuencia_fibonacci)