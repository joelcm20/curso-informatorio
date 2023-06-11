class Producto():
    def __init__(self, nombre, cantidad):
        self.nombre = nombre
        self.cantidad = cantidad
        self._sobrante = 0

    def calcular(self, cantidad_producto, cantidad_entidad):
        if cantidad_producto % cantidad_entidad == 0:
            print(
                f"para cada entidad hay {cantidad_producto/cantidad_entidad} {self.nombre}")
        else:
            self._sobrante = int(cantidad_producto % cantidad_entidad)
            print(
                f"- Para cada entidad hay {int(cantidad_producto / cantidad_entidad)} {self.nombre} y sobra {self._sobrante}")
        if hasattr(self, "dias_a_caducar"):
            if self.dias_a_caducar < 10:
                print("- La entrega debe hacerse este dia.")
            elif self.dias_a_caducar >= 10 and self.dias_a_caducar <= 20:
                print("- La entrega debe hacerse en los proximos dias.")
            else:
                print("- La entrega debe hacerse en el plazo de una semana.")
        if hasattr(self, "tipo"):
            print("- La entrega debe hacerse como maximo en los proximos 30 dias.")


class Perecedero(Producto):
    def __init__(self, nombre, cantidad, dias_a_caducar):
        Producto.__init__(self, nombre, cantidad)
        self.dias_a_caducar = dias_a_caducar


class No_perecedero(Producto):
    def __init__(self, nombre, cantidad, tipo):
        Producto.__init__(self, nombre, cantidad)
        self.tipo = tipo


p = No_perecedero("Lata sardina", 10, "lata")
p.calcular(p.cantidad, 3)