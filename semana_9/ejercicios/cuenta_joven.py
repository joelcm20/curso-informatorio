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

class CuentaJoven(Cuenta):
    def __init__(self, titular, bonificacion, edad, cantidad=0.0):
        Cuenta.__init__(self, titular, cantidad)
        self.bonificacion = bonificacion
        self.edad = edad

    def esTitularValido(self):
        return self.edad >= 18 and self.edad < 25
    
    def retirar(self, cantidad):
        if not self.esTitularValido():
            raise ValueError("El titular no es valido para retirar dinero")
        Cuenta.retirar(self, cantidad)
    
    def mostrar(self):
        return f"Cuenta Jovem\n{Cuenta.mostrar(self)}, Bonificacion: {self.bonificacion}%"


cuenta1 = CuentaJoven("Juan", 25, 17)
cuenta1.ingresar(100)
try:
    cuenta1.retirar(50)
except ValueError as e:
    print(e)
print(cuenta1.mostrar())