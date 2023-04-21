class Pelicula:
    def __init__(self, nombre):
        self._nombre = nombre

    def __str__(self):
        return f'Nombre: {self._nombre}'

    # Getter
    @property
    def nombre(self):
        return self._nombre

    # Setter
    @nombre.setter
    def nombre(self, nombre):
        self._nombre = nombre
