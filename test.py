from dominio.pelicula import Pelicula
from servicio.catalogo_peliculas import CatalogoPeliculas as cp

opc = None
while opc != 4:
    try:
        print(f'''
            Opciones: 2
            1- Agregar Película
            2- Listar Peliculas
            3- Eliminar archivo de películas
            4- Salir
            ''')
        opc = int(input('Selecciona una opción: '))

        if opc == 1:
            nombre_pelicula = input('Proporciona el nombre de la película: ')
            pelicula = Pelicula(nombre_pelicula)
            cp.agregar_pelicula(pelicula)
        elif opc == 2:
            cp.listar_peliculas()
        elif opc == 3:
            cp.eliminar_peliculas()

    except Exception as e:
        print(f'Ocurrió un error {e}')
        opc = None
else:
    print('Salimos del programa')
