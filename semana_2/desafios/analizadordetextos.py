'''
Desafío 2: Analizador de textos
Requisitos técnicos:
Se te pide crear un programa que le pida al usuario que ingresar un texto
cualquiera, por ejemplo, un artículo o una frase.
Luego el programa le va a pedir al usuario que también ingrese 3 letras a su
elección.
Nuestro código va a procesar esa información para realizar los análisis
necesarios para devolverle al usuario la siguiente información:
1- Cantidad de veces que aparece cada una de letras que eligió.
Tip 1: almacenar las letras en una lista para usar algún método de contar un substring en un
string
Tip 2: al buscar las letras puede haber mayúscula y minúsculas. Para asegurar que se
encuentren todas las letras, pasa tanto el texto original como las letras a buscar a
minúscula.
2- Cuantas palabras hay en total en todo el texto.
Tip 3: usa métodos para transformar el texto en lista de palabras y para calcular su longitud.
3- Cual es la primera letra y cuál es la última. (Indexación)
4- Mostrar el texto en orden inverso.
5- Decir si la palabra "python" aparece en el texto.
Tip 4: usa bool para verificar si se encuentra, y un diccionario para asociar el booleano con un
string para mostrar al usuario.
'''

frase = input('ingrese una frase:').lower().strip()
letra1 = input ('Ingrese una letra:').lower()
letra2 = input ('Ingrese una letra:').lower()
letra3 = input ('Ingrese la ultima letra:').lower()

count_letra1 = frase.count(letra1)
count_letra2 = frase.count(letra2)
count_letra3 = frase.count(letra3)

count_palabras = len(frase.split(" "))
primera_letra = frase[0]
ultima_letra = frase[-1]
texto_inverso = frase [::-1]
texto_orden_inverso = frase.split(" ")[::-1]
texto_orden_inverso2= " ".join (texto_orden_inverso)

print("el numero de veces que tu letra aparece en la frase es: ","\n", letra1,"=", count_letra1,"\n", letra2,"=", count_letra2,"\n", letra3,"=", count_letra3)
print("En el texto hay un total de: ",count_palabras,"palabras")
print("la primera letra de la frase es:",primera_letra,"y la ultima es",ultima_letra)
print("su texto en forma inversa es:",texto_inverso)
print (texto_orden_inverso2)

if "python" in frase:
    print("la palabra python se encuentra en la frase")
else:
    print ("la pabla python no se encuntra en la frase")


#Los integrantes del grupo son: Joel Chavez, Renzo Arrieta, Pablo Acevedo, Serial Trachta Matías Gastón, Lugo Mauro Rodrigo, Julio R. Escanciano Gonzalez, Facundo Vicedo, Gabriel Leiva, Maximiliano Imanol Aguer, Salto Cristian J.














