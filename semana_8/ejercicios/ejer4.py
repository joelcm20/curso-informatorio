class Tiempo():
    def __init__(self, hora, minuto=0, segundo=0):
        self._hora = hora
        self._minuto = minuto
        self._segundo = segundo

    def __str__(self):
        return f"{self._hora}:{self._minuto}:{self._segundo}"

    def modificar(self, hora, minuto, segundo):
        self._hora = hora
        self._minuto = minuto
        self._segundo = segundo


class prueba_tiempo():
    def __init__(self):
        self.tiempo = Tiempo(15, 30, 0)
    
    def mostrar(self):
        print(self.tiempo.__str__())
    
    def modificar(self):
        hora = int(input("Ingrese hora: "))
        minuto = int(input("Ingrese minuto: "))
        segundo = int(input("Ingrese segundo: "))
        self.tiempo.modificar(hora, minuto, segundo)


prueba = prueba_tiempo()
prueba.mostrar()
prueba.modificar()
prueba.mostrar()