import random

class Carta:
    def __init__(self, valor, palo):
        self.valor = valor
        self.palo = palo

class Baraja:
    def __init__(self):
        self.monton = []
        self.cartas = [
            Carta(1, 'espada'),
            Carta(1, 'basto'),
            Carta(1, 'oro'),
            Carta(1, 'copa'),
            Carta(2, 'espada'),
            Carta(2, 'basto'),
            Carta(2, 'oro'),
            Carta(2, 'copa'),
            Carta(3, 'espada'),
            Carta(3, 'basto'),
            Carta(3, 'oro'),
            Carta(3, 'copa'),
            Carta(4, 'espada'),
            Carta(4, 'basto'),
            Carta(4, 'oro'),
            Carta(4, 'copa'),
            Carta(5, 'espada'),
            Carta(5, 'basto'),
            Carta(5, 'oro'),
            Carta(5, 'copa'),
            Carta(6, 'espada'),
            Carta(6, 'basto'),
            Carta(6, 'oro'),
            Carta(6, 'copa'),
            Carta(7, 'espada'),
            Carta(7, 'basto'),
            Carta(7, 'oro'),
            Carta(7, 'copa'),
            Carta(10, 'espada'),
            Carta(10, 'basto'),
            Carta(10, 'oro'),
            Carta(10, 'copa'),
            Carta(11, 'espada'),
            Carta(11, 'basto'),
            Carta(11, 'oro'),
            Carta(11, 'copa'),
            Carta(12, 'espada'),
            Carta(12, 'basto'),
            Carta(12, 'oro'),
            Carta(12, 'copa')
        ]
    
    def barajar(self):
        random.shuffle(self.cartas)
    
    def siguiente_carta(self):
        if len(self.cartas) == 0:
            raise ValueError('no hay mas cartas')
        carta = self.cartas[0]
        self.cartas = self.cartas[1:]
        self.monton.append(carta)
        return carta
    
    def cartas_disponibles(self):
        return len(self.cartas)
    
    def dar_cartas(self, cantidad):
        if cantidad > self.cartas_disponibles():
            raise ValueError('no hay suficientes cartas')
        cartas = self.cartas[:cantidad]
        self.cartas = self.cartas[cantidad:]
        self.monton.extend(cartas)
        return cartas
    
    def cartas_monton(self):
        if len(self.monton) == 0:
            raise ValueError('no ha salido ninguna carta')
        for carta in self.monton:
            print(carta.valor, carta.palo)
    
    def mostrar_baraja(self):
        for carta in self.cartas:
            print(carta.valor, carta.palo)

def opciones():
    print()
    print('============= Opciones Baraja =============')
    print('1. Barajar                                 |')
    print('2. Siguiente carta                         |')
    print('3. Dar cartas                              |')
    print('4. Cartas disponibles                      |')
    print('5. Cartas monton                           |')
    print('6. Mostrar baraja                          |')
    print('0. Salir                                   |')
    print('===========================================')
    print()
baraja = Baraja()
while True:
    opciones()
    try:
        opcion = int(input("Ingrese una opcion: "))
    except ValueError:
        print()
        print("============= ERROR =============")
        print('Ingrese una opcion valida        |')
        print('=================================')
        print()
        continue
    if opcion == 0:
        break
    if opcion == 1:
        baraja.barajar()
    if opcion == 2:
        try:
            carta = baraja.siguiente_carta()
            print(carta.valor, carta.palo)
        except ValueError as e:
            print()
            print("============= ERROR =============")
            print(f'{e}                |')
            print('=================================')
            print()
            continue
    if opcion == 3:
        while True:
            try:
                cantidad = int(input('Ingrese la cantidad de cartas: '))
                break
            except ValueError:
                print()
                print("============= ERROR =============")
                print('Ingrese una opcion valida        |')
                print('=================================')
                print()
                continue
        try:
            cartas = baraja.dar_cartas(cantidad)
        except ValueError as e:
            print()
            print("============= ERROR =============")
            print(f'{e}        |')
            print('=================================')
            print()
            continue
        for carta in cartas:
            print(carta.valor, carta.palo)
    if opcion == 4:
        print(baraja.cartas_disponibles())
    if opcion == 5:
        try:
            baraja.cartas_monton()
        except ValueError as e:
            print()
            print("============= ERROR =============")
            print(f'{e}        |')
            print('=================================')
            print()
            continue
    if opcion == 6:
        baraja.mostrar_baraja()

