class Cuenta():
    def __init__(self, titular, cantidad=0.0):
        self.titular = titular
        self.cantidad = cantidad

    def mostrar(self):
        return f"Titular: {self.titular}, Cantidad: {self.cantidad}"

    def ingresar(self, cantidad):
        if cantidad >= 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        self.cantidad -= cantidad


cuenta1 = Cuenta("Juan", 1000)
print(cuenta1.mostrar())
cuenta1.retirar(500)
print(cuenta1.mostrar())
cuenta1.ingresar(50)
print(cuenta1.mostrar())
cuenta1.retirar(600)
print(cuenta1.mostrar())
cuenta1.ingresar(-100)
print(cuenta1.mostrar())