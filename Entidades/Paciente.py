from Entidades.Persona import Persona

class Paciente(Persona):
    def __init__(self, nombre, apellido, dni, obra_social):
        super().__init__(nombre, apellido, dni)
        self.__obra_social = obra_social

    @property
    def obra_social(self):
        return self.__obra_social

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Obra Social: {self.__obra_social}")
