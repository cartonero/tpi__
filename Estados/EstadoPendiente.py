from Estados.IEstadoTurno import IEstadoTurno

class EstadoPendiente(IEstadoTurno):

    def confirmar(self, turno):
        from Estados.EstadoConfirmado import EstadoConfirmado
        print("✔ Turno confirmado.")
        turno.set_estado(EstadoConfirmado())

    def cancelar(self, turno):
        from Estados.EstadoCancelado import EstadoCancelado
        print("✔ Turno cancelado.")
        turno.set_estado(EstadoCancelado())

    def finalizar(self, turno):
        print("❌ No se puede finalizar un turno pendiente.")

    def __str__(self):
        return "PENDIENTE"
