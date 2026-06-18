from Estados.IEstadoTurno import IEstadoTurno

class EstadoCancelado(IEstadoTurno):

    def confirmar(self, turno):
        print("❌ No se puede confirmar un turno cancelado.")

    def cancelar(self, turno):
        print("❌ El turno ya está cancelado.")

    def finalizar(self, turno):
        print("❌ No se puede finalizar un turno cancelado.")

    def __str__(self):
        return "CANCELADO"
