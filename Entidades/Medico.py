from Entidades.Persona import Persona

class Medico(Persona):
    def __init__(self, nombre, apellido, dni, especialidad, matricula):
        super().__init__(nombre, apellido, dni)
        self.__especialidad = especialidad
        self.__matricula = matricula

    @property
    def especialidad(self):
        return self.__especialidad

    @property
    def matricula(self):
        return self.__matricula

    def mostrar_datos(self):
        super().mostrar_datos()
        print(f"Especialidad: {self.__especialidad} | Matrícula: {self.__matricula}")
