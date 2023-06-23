from datetime import datetime, timedelta

""" Clase Usuario
 - atributos: id, nombre, apellido, teléfono, username, email, contraseña, fecha de
registro, avatar, estado, online
- métodos: login(), registrar() """
class Usuario:
    def __init__(self, id, nombre, apellido, teléfono, username, email, contraseña, fecha_registro, avatar):
        self.id = id
        self.nombre = nombre
        self.apellido = apellido
        self.teléfono = teléfono
        self.username = username
        self.email = email
        self.contrasena = contraseña
        self.fecha_registro = fecha_registro
        self.avatar = avatar
        self._estado = False
        self._online = False
    
    def comentar(self, id, id_articulo, comentario, articulos):#-> Excepcion, Comentario
        if not self.get_online():
            return Exception("El usuario no está conectado"), None
        existe = False
        for articulo in articulos:
            if not isinstance(articulo, Articulo):
                return Exception("El articulo no es un objeto de tipo Articulo"), None
            if articulo.id == id_articulo:
                existe = True
        if not isinstance(id, int) or not isinstance(id_articulo, int):
            return Exception("El id y el id del articulo debe ser un entero"), None
        if not isinstance(comentario, str):
            return Exception("El comentario debe ser un string"), None
        if not existe:
            return Exception("El articulo no existe"), None
        fecha_hora = datetime.now()
        return None, Comentario(id, id_articulo, self.id, comentario, fecha_hora, True)
    def login(self):#-> Excepcion
        if not self.get_estado():
            return Exception("El usuario no está activo o no existe")
        self.set_online(True)
        return None
    def registrar(self):#-> Excepcion
        if self.get_estado():
            return Exception("El usuario ya está registrado")
        self.set_estado(True)
        return None
    def set_online(self, online):#-> Excepcion
        if not isinstance(online, bool):
            return Exception("El parametro online debe ser un booleano")
        self._online = online
        return None
    def get_online(self):#-> Bool
        return self._online
    def set_estado(self, estado):#-> Excepcion
        if not isinstance(estado, bool):
            return Exception("El parametro estado debe ser un booleano")
        self._estado = estado
        return None
    def get_estado(self):#-> Bool
        return self._estado

""" Clase Publico(Usuario)
 - atributo: es_publico
 - métodos: registrar(), comentar() """
class Publico(Usuario):
    def __init__(self, id, nombre, apellido, teléfono, username, email, contraseña, fecha_registro, avatar):
        Usuario.__init__(self, id, nombre, apellido, teléfono, username, email, contraseña, fecha_registro, avatar)
        self.es_publico = True

""" clase Colaborador(Usuario)
 - atributos: es_colaborador
 - métodos: registrar(), comentar(), publicar() """
class Colaborador(Usuario):
    def __init__(self, id, nombre, apellido, teléfono, username, email, contraseña, fecha_registro, avatar):
        Usuario.__init__(self, id, nombre, apellido, teléfono, username, email, contraseña, fecha_registro, avatar)
        self.es_colaborador = True
    def publicar(self, id_articulo, titulo, resumen, contenido, imagen="", estado=True):#-> Excepcion, Articulo
        if not self.get_online():
            return Exception("El usuario no está conectado"), None
        if not isinstance(id_articulo, int):
            return Exception("El id del articulo debe ser un entero"), None
        if not isinstance(titulo, str) or not isinstance(resumen, str) or not isinstance(contenido, str):
            return Exception("Los titulos, resumen y contenido deben ser un string"), None
        fecha_publicacion = datetime.now()
        return None, Articulo(id_articulo, self.id, titulo, resumen, contenido, fecha_publicacion, imagen, estado)

""" clase Articulo
atributos: id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado """
class Articulo:
    def __init__(self, id, id_usuario, titulo, resumen, contenido, fecha_publicacion, imagen, estado):
        self.id = id
        self.id_usuario = id_usuario
        self.titulo = titulo
        self.resumen = resumen
        self.contenido = contenido
        self.fecha_publicacion = fecha_publicacion
        self.imagen = imagen
        self.estado = estado

""" clase Comentario
- atributos: id, id_articulo, id_usuario, contenido, fecha_hora, estado """
class Comentario:
    def __init__(self, id, id_articulo, id_usuario, contenido, fecha_hora, estado):
        self.id = id
        self.id_articulo = id_articulo
        self.id_usuario = id_usuario
        self.contenido = contenido
        self.fecha_hora = fecha_hora
        self.estado = estado
    def print_info(self):
        print("id: ", self.id)
        print("id_articulo: ", self.id_articulo)
        print("id_usuario: ", self.id_usuario)
        print("contenido: ", self.contenido)
        print("fecha_hora: ", self.fecha_hora)

# PROBANDO
"""
usuarios: creando usuarios colaboradores y publicos 
"""
joel = Colaborador(1, "Joel", "Martinez", "1234567890", "joelmartinez", "joelmartinez", "joelmartinez", datetime.now(), "joelmartinez.jpg")
lucas = Publico(2, "Lucas", "Martinez", "1234567890", "lucasmartinez", "lucasmartinez", "lucasmartinez", datetime.now(), "lucasmartinez.jpg")
lautaro = Publico(3, "Lautaro", "Martinez", "1234567890", "lautarmartinez", "lautarmartinez", "lautarmartinez", datetime.now(), "lautarmartinez.jpg")

"""
registrando los usuarios creados
"""
joel.registrar()
lucas.registrar()
lautaro.registrar()

"""
logueando los usuarios para podes comentar y publicar
"""
joel.login()
lucas.login()
lautaro.login()

"""
articulos: creando articulos
"""
exception, articulo1 = joel.publicar(1, "Titulo1", "Resumen1", "Contenido1")
if exception:
    print(exception)
exception, articulo2 = joel.publicar(2, "Titulo2", "Resumen2", "Contenido2")
if exception:
    print(exception)
exception, articulo3 = joel.publicar(3, "Titulo3", "Resumen3", "Contenido3")
if exception:
    print(exception)
lista_articulos = [articulo1, articulo2, articulo3]

"""
comentar: esta funcion crea algunos comentarios y muestra errores en caso de tener alguno
"""
def comentar():
    exception, comentario1 = lucas.comentar(1, 1, "Comentario1", lista_articulos)
    if exception:
        print(exception)
    else:
        comentario1.print_info()
    exception, comentario2 = lautaro.comentar(2, 2, "Comentario2", lista_articulos)
    if exception:
        print(exception)
    else:
        comentario2.print_info()

"""
Llamo la funcion comentar con los usuarios registrados y logueados
"""
comentar()

# integrantes
# Pablo, Acevedo
# Matías Gastón, Serial Trachta
# Lugo Mauro, Rodrigo
# Julio R, Escanciano Gonzalez
# Facundo, Vicedo
# Gabriel, Leiva
# Joel, Chavez
# Maximiliano Imanol, Aguer
# Cristian J, Salto
# Fabricio, Herrera
