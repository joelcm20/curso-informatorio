""" Desarrollar un programa que cargue los datos de un triángulo.
Implementar una clase con los métodos para inicializar los atributos, imprimir el
valor del lado con un tamaño mayor y el tipo de triángulo que es (equilátero,
isósceles o escaleno). """

class Triangulo:
    def __init__(self, lado1, lado2, lado3):
        self.lado1 = lado1
        self.lado2 = lado2
        self.lado3 = lado3
    
    def tipo_triangulo(self):
        if self.lado1 == self.lado2 == self.lado3:
            return "equilatero"
        elif (self.lado1 == self.lado2) or (self.lado1 == self.lado3) or (self.lado2 == self.lado3):
            return "isosceles"
        else:
            return "escaleno"
    

    def lado_mayor(self):
        if self.lado1 > self.lado2 and self.lado1 > self.lado3:
            return self.lado1
        elif self.lado2 > self.lado1 and self.lado2 > self.lado3:
            return self.lado2
        else:
            return self.lado3
    
triangulo = Triangulo(5, 10, 3)
print(triangulo.tipo_triangulo())
print(triangulo.lado_mayor())