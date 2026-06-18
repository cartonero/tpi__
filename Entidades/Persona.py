class Persona:
    def __init__(self, nombre, apellido, dni):
        self.__nombre = nombre
        self.__apellido = apellido
        self.__dni = dni

    @property
    def nombre(self):
        return self.__nombre

    @property
    def apellido(self):
        return self.__apellido

    @property
    def dni(self):
        return self.__dni

    def mostrar_datos(self):
        print(f"Nombre: {self.__nombre} {self.__apellido} | DNI: {self.__dni}")
