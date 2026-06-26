import sys
import os
sys.path.insert(0, os.path.dirname(__file__))

from Entidades.AdminMedico import AdminMedico

adm = AdminMedico()

MENU = """
********************************************
     Administración de Turnos Médicos

     1. Mostrar Médicos
     2. Agregar Médico
     3. Mostrar Pacientes
     4. Agregar Paciente
     5. Mostrar Turnos
     6. Agregar Turno
     7. Confirmar Turno
     8. Cancelar Turno
     9. Finalizar Turno
     0. Salir
********************************************
"""

#********************************************
#     Administración de Turnos Médicos
#     1. Mostrar Médicos
#     2. Agregar Médico
#     3. Mostrar Pacientes
#     4. Agregar Paciente
#     5. Mostrar Turnos
#     6. Agregar Turno
#     7. Confirmar Turno
#     8. Cancelar Turno
#     9. Finalizar Turno
#    0. Salir
#********************************************


def main():
    while True:
        print(MENU)
        opcion = input("Ingrese una opción: ").strip()

        if opcion == "1":
            adm.mostrar_medicos()

        elif opcion == "2":
            nombre     = input("Nombre: ")
            apellido   = input("Apellido: ")
            dni        = input("DNI: ")
            especialidad = input("Especialidad: ")
            matricula  = input("Matrícula: ")
            adm.agregar_medico(nombre, apellido, dni, especialidad, matricula)

        elif opcion == "3":
            adm.mostrar_pacientes()

        elif opcion == "4":
            nombre      = input("Nombre: ")
            apellido    = input("Apellido: ")
            dni         = input("DNI: ")
            obra_social = input("Obra Social: ")
            adm.agregar_paciente(nombre, apellido, dni, obra_social)

        elif opcion == "5":
            adm.mostrar_turnos()

        elif opcion == "6":
            dni_pac    = input("DNI del Paciente: ")
            matricula  = input("Matrícula del Médico: ")
            fecha_hora = input("Fecha y Hora (ej: 2026-06-25 10:00): ")
            adm.agregar_turno(dni_pac, matricula, fecha_hora)

        elif opcion == "7":
            adm.mostrar_turnos()
            idx = int(input("Número de turno a confirmar (desde 0): "))
            adm.confirmar_turno(idx)

        elif opcion == "8":
            adm.mostrar_turnos()
            idx = int(input("Número de turno a cancelar (desde 0): "))
            adm.cancelar_turno(idx)

        elif opcion == "9":
            adm.mostrar_turnos()
            idx = int(input("Número de turno a finalizar (desde 0): "))
            adm.finalizar_turno(idx)

        elif opcion == "0":
            print("Saliendo...")
            break

        else:
            print("❌ Opción inválida.")

if __name__ == "__main__":
    main()
