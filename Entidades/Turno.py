from Estados.IEstadoTurno import IEstadoTurno

class Turno:
    def __init__(self, paciente, medico, fecha_hora):
        self.__paciente = paciente
        self.__medico = medico
        self.__fecha_hora = fecha_hora
        # Estado inicial
        from Estados.EstadoPendiente import EstadoPendiente
        self.__estado = EstadoPendiente()

    @property
    def paciente(self):
        return self.__paciente

    @property
    def medico(self):
        return self.__medico

    @property
    def fecha_hora(self):
        return self.__fecha_hora

    def set_estado(self, nuevo_estado: IEstadoTurno):
        self.__estado = nuevo_estado

    def confirmar(self):
        self.__estado.confirmar(self)

    def cancelar(self):
        self.__estado.cancelar(self)

    def finalizar(self):
        self.__estado.finalizar(self)

    def mostrar_datos(self):
        print(f"Paciente: {self.__paciente.nombre} {self.__paciente.apellido} | "
                f"Médico: {self.__medico.nombre} {self.__medico.apellido} | "
                f"Fecha/Hora: {self.__fecha_hora} | Estado: {self.__estado}")
