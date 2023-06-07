from ejer1 import Vehiculo, Coche


class Camioneta(Coche):
    def __init__(self, color, ruedas, velocidad, cilindrada, carga):
        Coche.__init__(self, color, ruedas, velocidad, cilindrada)
        self.carga = carga


class Bicicleta(Vehiculo):
    def __init__(self, color, ruedas, tipo):
        Vehiculo.__init__(self, color, ruedas)
        self.tipo = tipo


class Motocicleta(Vehiculo):
    def __init__(self, color, ruedas, velocidad, cilindrada):
        Vehiculo.__init__(self, color, ruedas)
        self.velocidad = velocidad
        self.cilindrada = cilindrada


coche = Coche("rojo", 4, 200, 2000)
camioneta = Camioneta("azul", 4, 200, 2000, 100)
bicicleta = Bicicleta("verde", 2, "urbana")
motocicleta = Motocicleta("negro", 3, 200, 2000)

vehiculos = [coche, camioneta, bicicleta, motocicleta]


def catalogar(vehiculos):
    for vehiculo in vehiculos:
        print(f"{vehiculo.__class__.__name__}: {list(vehiculo.__dict__.keys())}")
    print("\n")


catalogar(vehiculos)

""" Modifica la función catalogar() para que reciba un argumento optativo
ruedas, haciendo que muestre únicamente los que su número de ruedas
concuerde con el valor del argumento. También debe mostrar un mensaje "Se
han encontrado {} vehículos con {} ruedas:" únicamente si se envía el
argumento ruedas. """


def catalogar2(vehiculos, ruedas=None):
    if not ruedas == None:
        encontrados = 0
        for vehiculo in vehiculos:
            if vehiculo.ruedas == ruedas:
                encontrados += 1
                print(
                    f"{vehiculo.__class__.__name__}: {list(vehiculo.__dict__.keys())}")
        print(
            f"Se han encontrado {encontrados} vehículos con {ruedas} ruedas\n")
    else:
        for vehiculo in vehiculos:
            print(f"{vehiculo.__class__.__name__}: {list(vehiculo.__dict__.keys())}")
        print("\n")


catalogar2(vehiculos)
