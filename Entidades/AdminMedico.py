from Entidades.Paciente import Paciente
from Entidades.Medico import Medico
from Entidades.Turno import Turno

class AdminMedico:
    def __init__(self):
        self.__lista_pacientes = []
        self.__lista_medicos = []
        self.__lista_turnos = []

    # --- Pacientes ---
    def agregar_paciente(self, nombre, apellido, dni, obra_social):
        p = Paciente(nombre, apellido, dni, obra_social)
        self.__lista_pacientes.append(p)
        print("✔ Paciente agregado.")

    def mostrar_pacientes(self):
        if not self.__lista_pacientes:
            print("No hay pacientes registrados.")
            return
        for p in self.__lista_pacientes:
            print("----------------------------")
            p.mostrar_datos()

    def buscar_paciente_dni(self, dni):
        for p in self.__lista_pacientes:
            if p.dni == dni:
                return p
        return None

    # --- Médicos ---
    def agregar_medico(self, nombre, apellido, dni, especialidad, matricula):
        m = Medico(nombre, apellido, dni, especialidad, matricula)
        self.__lista_medicos.append(m)
        print("✔ Médico agregado.")

    def mostrar_medicos(self):
        if not self.__lista_medicos:
            print("No hay médicos registrados.")
            return
        for m in self.__lista_medicos:
            print("----------------------------")
            m.mostrar_datos()

    def buscar_medico_matricula(self, matricula):
        for m in self.__lista_medicos:
            if m.matricula == matricula:
                return m
        return None

    # --- Turnos ---
    def agregar_turno(self, dni_paciente, matricula_medico, fecha_hora):
        paciente = self.buscar_paciente_dni(dni_paciente)
        medico = self.buscar_medico_matricula(matricula_medico)
        if not paciente:
            print("❌ Paciente no encontrado.")
            return
        if not medico:
            print("❌ Médico no encontrado.")
            return
        t = Turno(paciente, medico, fecha_hora)
        self.__lista_turnos.append(t)
        print("✔ Turno creado con estado PENDIENTE.")

    def mostrar_turnos(self):
        if not self.__lista_turnos:
            print("No hay turnos registrados.")
            return
        for t in self.__lista_turnos:
            print("----------------------------")
            t.mostrar_datos()

    def confirmar_turno(self, indice):
        self.__accion_turno(indice, "confirmar")

    def cancelar_turno(self, indice):
        self.__accion_turno(indice, "cancelar")

    def finalizar_turno(self, indice):
        self.__accion_turno(indice, "finalizar")

    def __accion_turno(self, indice, accion):
        if indice < 0 or indice >= len(self.__lista_turnos):
            print("❌ Índice de turno inválido.")
            return
        turno = self.__lista_turnos[indice]
        getattr(turno, accion)()
