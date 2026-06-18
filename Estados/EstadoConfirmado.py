from Estados.IEstadoTurno import IEstadoTurno

class EstadoConfirmado(IEstadoTurno):

    def confirmar(self, turno):
        print("❌ El turno ya está confirmado.")

    def cancelar(self, turno):
        from Estados.EstadoCancelado import EstadoCancelado
        print("✔ Turno cancelado.")
        turno.set_estado(EstadoCancelado())

    def finalizar(self, turno):
        from Estados.EstadoFinalizado import EstadoFinalizado
        print("✔ Turno finalizado.")
        turno.set_estado(EstadoFinalizado())

    def __str__(self):
        return "CONFIRMADO"
