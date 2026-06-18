from Estados.IEstadoTurno import IEstadoTurno

class EstadoFinalizado(IEstadoTurno):

    def confirmar(self, turno):
        print("❌ No se puede confirmar un turno finalizado.")

    def cancelar(self, turno):
        print("❌ No se puede cancelar un turno finalizado.")

    def finalizar(self, turno):
        print("❌ El turno ya está finalizado.")

    def __str__(self):
        return "FINALIZADO"
