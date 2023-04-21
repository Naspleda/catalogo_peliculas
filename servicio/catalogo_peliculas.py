import os


class CatalogoPeliculas:
    # Creamos un nuevo archivo en caso de que no haya uno
    ruta_archivo = 'peliculas.txt'

    # Metodo: Agregar Pelicula
    @classmethod
    def agregar_pelicula(cls, pelicula):
        with open(cls.ruta_archivo, "a", encoding='utf8')as archivo:
            archivo.write(f'{pelicula.nombre}\n')

    # Metodo: Listar Peliculas
    @classmethod
    def listar_peliculas(cls):
        with open(cls.ruta_archivo, 'r', encoding='utf8')as archivo:
            print(f'Catálogo de Peliculas'.center(50, '-'))
            print(archivo.read())

    # Metodo: Eliminar archivo
    @classmethod
    def eliminar_peliculas(cls):
        os.remove(cls.ruta_archivo)
        print(f'Archivo Elminado: {cls.ruta_archivo}')
