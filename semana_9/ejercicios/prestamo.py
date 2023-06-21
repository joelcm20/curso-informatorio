from datetime import datetime, timedelta
import random

class Solicitante:
    def __init__(self, dni, nombre, apellido, telefono):
        self.dni = dni
        self.nombre = nombre
        self.apellido = apellido
        self.telefono = telefono

class Trabajador(Solicitante):
    def __init__(self, dni, nombre, apellido, telefono):
        super().__init__(dni, nombre, apellido, telefono)

class Prestamo:
    def __init__(self, n_prestamo, solitante, monto, fecha_autorizacion, gestor):
        self.n_prestamo = n_prestamo
        self.solitante = solitante
        self.monto = monto
        self.fecha_autorizacion = fecha_autorizacion
        self.fecha_entrega = self.fecha_autorizacion + timedelta(days=7)
        self.fecha_pago = self.fecha_entrega+timedelta(days=30)
        self.gestor = gestor
        self.autorizado = False
        self.fecha_maxima_autorizar = datetime.now() + timedelta(days=10)
    
    def informacion(self):
        return f"Nombre: {self.solitante.nombre} {self.solitante.apellido}\nDNI: {self.solitante.dni}\nTelefono: {self.solitante.telefono}\nFecha de autorización: {self.fecha_autorizacion}\nFecha de entrega: {self.fecha_entrega}\nFecha de pago: {self.fecha_pago}\nGestor:\nNombre: {self.gestor.nombre} {self.gestor.apellido}\nDNI: {self.gestor.dni}\nTelefono: {self.gestor.telefono}"
    
    

class Cooperativa:
    def __init__(self, nombre, nit, direccion, telefono, cantidad_maxima):
        self.nombre = nombre
        self.nit = nit
        self.direccion = direccion
        self.telefono = telefono
        self.trabajadores = []
        self.prestamos = []
        self.cantidad_maxima = cantidad_maxima
    
    def agregar_trabajador(self, dni, nombre, apellido, telefono):
        self.trabajadores.append(Trabajador(dni, nombre, apellido, telefono))
    
    def realizar_prestamo(self, n_prestamo, solitante, monto, fecha_autorizacion):
        if self.obtener_cantidad_prestadas()+monto > self.cantidad_maxima:
            raise Exception("No hay más prestamos disponibles.")
        gestor = self.trabajadores[random.randint(0, len(self.trabajadores)-1)]
        self.prestamos.append(Prestamo(n_prestamo, solitante, monto, fecha_autorizacion, gestor))
    
    def autorizar_prestamo(self, n_prestamo):
        if datetime.now().day > 20:
            raise Exception("Solo se puede autorizar en los primeros 20 días del mes.")
        for prestamo in self.prestamos:
            if prestamo.n_prestamo == n_prestamo:
                if prestamo.fecha_maxima_autorizar < datetime.now():
                    raise Exception("El prestamo ya no puede autorizarse (fecha expirada).")
                prestamo.autorizado = True
                break
    
    def obtener_cantidad_prestadas(self):
        monto = 0
        for prestamo in self.prestamos:
            monto += prestamo.monto
        return monto
    

joel_inc = Cooperativa("Joel Inc", "123456789", "Calle 123", "123456789", 1000)
joel_inc.agregar_trabajador("123456789", "juan", "perez", "123456789")
joel_inc.agregar_trabajador("123456789", "pedro", "dominguez", "123456789")
joel_inc.agregar_trabajador("123456789", "lautaro", "altamirano", "123456789")

laura = Solicitante("123456789", "laura", "altamirano", "123456789")
marcos = Solicitante("123456789", "marcos", "rosales", "123456789")
gavito = Solicitante("123456789", "gavito", "roldan", "123456789")

try:
    joel_inc.realizar_prestamo(1, laura, 500, datetime.now()+timedelta(days=13))
except Exception as e:
    print(e)
try:
    joel_inc.realizar_prestamo(2, marcos, 400, datetime.now()+timedelta(days=13))
except Exception as e:
    print(e)
try:
    joel_inc.realizar_prestamo(3, gavito, 100, datetime.now()+timedelta(days=13))
except Exception as e:
    print(e)

try:
    joel_inc.autorizar_prestamo(1)
except Exception as e:
    print(e)
try:
    joel_inc.autorizar_prestamo(2)
except Exception as e:
    print(e)
try:
    joel_inc.autorizar_prestamo(3)
except Exception as e:
    print(e)

for prestamo in joel_inc.prestamos:
    print(prestamo.informacion())
    print("\n")