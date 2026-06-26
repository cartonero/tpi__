# Sistema de Administración de Turnos Médicos

Trabajo Práctico Integrador (TPI) de Programación Orientada a Objetos. Aplicación de consola en Python para gestionar médicos, pacientes y turnos médicos, aplicando los pilares de la POO y el patrón de diseño **State**.

## Descripción del proyecto

El sistema permite administrar el flujo completo de turnos médicos de un consultorio:

- Registrar **médicos** (nombre, apellido, DNI, especialidad y matrícula).
- Registrar **pacientes** (nombre, apellido, DNI y obra social).
- Asignar **turnos** entre un paciente y un médico en una fecha y hora determinada.
- Controlar el **ciclo de vida de cada turno** (Pendiente → Confirmado → Finalizado, o Cancelado), evitando transiciones inválidas como confirmar un turno ya cancelado o finalizar uno que nunca fue confirmado.

Ese control de transiciones está resuelto con el patrón de diseño **State**, que evita usar condicionales (`if/elif`) repartidos por el código y permite agregar nuevos estados sin modificar las clases existentes.

## Tecnologías

- **Python 3** (sin dependencias externas — solo librería estándar).

## Estructura del proyecto

```
ProyectoTPI/
├── Program.py                      # Punto de entrada — menú por consola
├── Entidades/
│   ├── Persona.py                  # Clase base (nombre, apellido, DNI)
│   ├── Medico.py                   # Hereda de Persona
│   ├── Paciente.py                 # Hereda de Persona
│   ├── Turno.py                    # Contexto del patrón State
│   └── AdminMedico.py              # Controlador: administra médicos, pacientes y turnos
└── Estados/
    ├── IEstadoTurno.py              # Interfaz del patrón State
    ├── EstadoPendiente.py           # Estado concreto
    ├── EstadoConfirmado.py          # Estado concreto
    ├── EstadoCancelado.py           # Estado concreto (terminal)
    └── EstadoFinalizado.py          # Estado concreto (terminal)
```

## Pilares de la POO aplicados

| Pilar | Dónde se aplica |
|---|---|
| **Encapsulamiento** | Atributos privados (`__nombre`, `__estado`, etc.) con acceso controlado mediante `@property` en `Persona` y `Turno`. |
| **Herencia** | `Medico` y `Paciente` heredan de `Persona`, reutilizando atributos y constructor con `super()`. |
| **Polimorfismo** | `Turno.confirmar()` delega en `self.__estado.confirmar(self)`: el mismo llamado se comporta distinto según la clase concreta del estado activo (`EstadoPendiente`, `EstadoConfirmado`, etc.), sin usar ningún `if`. |
| **Abstracción** | `IEstadoTurno` define el contrato (`confirmar`, `cancelar`, `finalizar`) como clase abstracta, sin implementar el comportamiento — cada estado concreto lo completa. |

## Patrón de diseño: State

El ciclo de vida de un `Turno` se modela con el patrón **State**:

- **Contexto**: `Turno`, que mantiene una referencia a su estado actual y delega en él los métodos `confirmar()`, `cancelar()` y `finalizar()`.
- **Interfaz State**: `IEstadoTurno`, que define el contrato común.
- **Estados concretos**: `EstadoPendiente`, `EstadoConfirmado`, `EstadoCancelado` y `EstadoFinalizado`, cada uno con sus propias transiciones válidas.

```python
# Turno.py — el contexto solo delega, sin condicionales
def confirmar(self):
    self.__estado.confirmar(self)
```

```python
# EstadoPendiente.py — el propio estado decide la transición
def confirmar(self, turno):
    turno.set_estado(EstadoConfirmado())
```

### Diagrama de transiciones

```
PENDIENTE ──confirmar──> CONFIRMADO ──finalizar──> FINALIZADO
    │                         │
    └──cancelar──> CANCELADO <┘
```

## Diagrama UML

El diagrama de clases completo (entidades + patrón State) se encuentra en [`docs/diagrama-uml.png`](docs/diagrama-uml.png).

> Si todavía no subiste la imagen del diagrama, agregala en una carpeta `docs/` en la raíz del repositorio con ese nombre para que el link funcione.

## Instrucciones de ejecución

### Requisitos

- Tener instalado Python 3.8 o superior.

### Pasos

1. Cloná el repositorio:
   ```bash
   git clone <URL-del-repositorio>
   cd ProyectoTPI
   ```

2. Ejecutá el programa:
   ```bash
   python Program.py
   ```
   (en algunos sistemas el comando es `python3 Program.py`)

3. Usá el menú interactivo por consola:
   ```
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
   ```

### Flujo de prueba sugerido

1. Agregar un médico (opción 2).
2. Agregar un paciente (opción 4).
3. Crear un turno entre ambos (opción 6) — queda en estado `PENDIENTE`.
4. Mostrar los turnos (opción 5) para ver el estado actual.
5. Confirmar el turno (opción 7) — pasa a `CONFIRMADO`.
6. Intentar confirmarlo de nuevo (opción 7) para ver el control de transiciones inválidas en acción.

## Autores

_Completar con los nombres del grupo._

## Materia / Cátedra

_Completar con el nombre de la materia y la cátedra._
