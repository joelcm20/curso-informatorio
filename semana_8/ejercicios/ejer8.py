class Libro():
    def __init__(self, titulo, autor, paginas, calificacion):
        self._titulo = titulo
        self._autor = autor
        self._paginas = paginas
        self._calificacion = calificacion

    def get_titulo(self):
        return self._titulo
    def get_autor(self):
        return self._autor
    def get_paginas(self):
        return self._paginas
    def get_calificacion(self):
        return self._calificacion
    def set_titulo(self, titulo):
        self._titulo = titulo
    def set_autor(self, autor):
        self._autor = autor
    def set_paginas(self, paginas):
        self._paginas = paginas
    def set_calificacion(self, calificacion):
        self._calificacion = calificacion


class ConjuntoLibros():
    def __init__(self):
        self._libros = []
    def agregar_libro(self, libro):
        self._libros.append(libro)
    def eliminar_libro(self, titulo=None, autor=None):
        if titulo != None:
            for libro in self._libros:
                if libro.get_titulo() == titulo:
                    self._libros.remove(libro)
        elif autor != None:
            for libro in self._libros:
                if libro.get_autor() == autor:
                    self._libros.remove(libro)
    def calificaciones(self):
        lista_ordenada = sorted(self._libros, key=lambda libro: libro.get_calificacion())
        if len(lista_ordenada) == 1:
            print(f"Solo hay 1 libro: {lista_ordenada[0].get_titulo()} de {lista_ordenada[0].get_autor()}")
        else:
            print(f"El libro mas calificado es: {lista_ordenada[-1].get_titulo()} de {lista_ordenada[-1].get_autor()}")
            print(f"El libro menos calificado es: {lista_ordenada[0].get_titulo()} de {lista_ordenada[0].get_autor()}")
    
    def mostrar_libros(self):
        for libro in self._libros:
            print(f"autor: {libro.get_autor()} titulo: {libro.get_titulo()} paginas: {libro.get_paginas()} calificacion: {libro.get_calificacion()}")



libros = ConjuntoLibros()
libros.agregar_libro(Libro("El señor de los anillos", "J.R.R. Tolkien", 500, 9.5))
libros.agregar_libro(Libro("hallo", "J.R.R. Tolkien", 500, 7))
libros.agregar_libro(Libro("Harry Potter", "J.K. Rowling", 320, 10))
libros.calificaciones()
libros.mostrar_libros()
libros.eliminar_libro(titulo="hallo")
libros.mostrar_libros()