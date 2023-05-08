from random import randint

print("""
Juego de adivina el numero.
Dato: El programa elige un numero al azar entre 1 y 100, y deberas adivinarlo.
Aviso: ¡Solo tienes 8 intentos!
""")

numero_azar = randint(1, 100)
intentos = 1

print(numero_azar)
while intentos <= 8: # mientras los intentos sean menor o igual que 8
    if intentos == 8: # y si el intento es el ultimo
        print("¡Atencion, este es tu ultimo intento!")
    numero = input("Ingresa un numero: ")
    if numero.isdigit(): # y numero sea un digito valido
        numero = int(numero)
        if numero < 1 or numero > 100: # y si el numero esta fuera del rango de 1 y 100
            print("¡El numero debe estar entre 1 y 100!")
        else:  # si es un digito y esta entre 1 y 100
            if numero == numero_azar:  # si adivino el numero
                print(f"¡Muy bien! El numero es el correcto.\nLo hiciste con un total de {intentos} intentos.")
                break
            else:  # si no adivino el numero
                if intentos == 8:  # y es el ultimo intento
                    print("¡Se termino el juego, mejor suerte la proxima vez!")
                else:  # y todavia quedan intentos
                    print(f"¡Ups! intentalo de nuevo, este fue tu intento numero {intentos}.")
                intentos += 1
    else: # y si el numero no es un digito valido
        print("¡Asegurate de ingresar un numero!")
