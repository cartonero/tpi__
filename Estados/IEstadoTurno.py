from abc import ABC, abstractmethod

class IEstadoTurno(ABC):

    @abstractmethod
    def confirmar(self, turno):
        pass

    @abstractmethod
    def cancelar(self, turno):
        pass

    @abstractmethod
    def finalizar(self, turno):
        pass

    @abstractmethod
    def __str__(self):
        pass
