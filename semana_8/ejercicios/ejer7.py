class Bebida():
    def __init__(self, id, litros, precio, marca):
        self.id = id
        self.litros = litros
        self.precio = precio
        self.marca = marca


class AguaMineral(Bebida):
    def __init__(self, id, litros, precio, marca, manantial, ciudad):
        Bebida.__init__(self, id, litros, precio, marca)
        self.manantial = manantial
        self.ciudad = ciudad


class Gaseosa(Bebida):
    def __init__(self, id, litros, precio, marca, porcentaje_azuar, promocion):
        Bebida.__init__(self, id, litros, precio, marca)
        self.porcentaje_azuar = porcentaje_azuar
        self.promocion = promocion


class Almacen():
    def __init__(self):
        self.deposito = []
    
    def calcular_precio(self):
        total = 0
        for bebida in self.deposito:
            if isinstance(bebida, Gaseosa):
                if bebida.promocion:
                    total += bebida.precio * 0.90
                    continue
            total += bebida.precio
        return total
    
    def calcular_precio_marca(self, marca):
        total = 0
        for bebida in self.deposito:
            if bebida.marca == marca:
                if isinstance(bebida, Gaseosa):
                    if bebida.promocion:
                        total += bebida.precio * 0.90
                        continue
                total += bebida.precio
        return total
    
    def agregar_bebida(self, bebida):
        existe = False
        for b in self.deposito:
            if b.id == bebida.id:
                existe = True
                break
        if not existe:
            self.deposito.append(bebida)
    
    def eliminar_bebida(self, id):
        for b in self.deposito:
            if b.id == id:
                self.deposito.remove(b)
                break
    
    def mostrar_informacion(self):
        for b in self.deposito:
            print(b.__dict__)

almacen = Almacen()
almacen.agregar_bebida(AguaMineral(1, 10, 10, "Coca Cola", True, "Cali"))
almacen.agregar_bebida(AguaMineral(2, 20, 20, "Fanta", True, "Cali"))
almacen.agregar_bebida(AguaMineral(3, 30, 30, "Sprite", True, "Cali"))
almacen.agregar_bebida(Gaseosa(4, 40, 40, "Coca Cola", 10, False))
almacen.agregar_bebida(Gaseosa(5, 50, 50, "Fanta", 20, True))
almacen.agregar_bebida(Gaseosa(6, 60, 60, "Sprite", 30, True))
print(almacen.calcular_precio())
almacen.eliminar_bebida(1)
print(almacen.calcular_precio())
almacen.mostrar_informacion()