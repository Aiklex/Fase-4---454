# Software FJ — Sistema Integral de Gestión de Clientes, Servicios y Reservas.

## Descripción del proyecto

Sistema orientado a objetos desarrollado en Python para gestionar clientes, servicios y reservas de la empresa ficticia **Software FJ**. La empresa ofrece tres tipos de servicios: reserva de salas, alquiler de equipos y asesorías especializadas.

El sistema opera completamente en memoria (sin base de datos), utilizando objetos, listas y manejo de archivos únicamente para el registro de eventos y errores. Implementa de forma rigurosa los principios de la programación orientada a objetos: abstracción, herencia, polimorfismo, encapsulación y manejo avanzado de excepciones.

Proyecto desarrollado como tarea grupal para el curso de Programación — Fase 4.

---

## Equipo de desarrollo

| Integrante | Paso asignado |
|---|---|
| Francy Alexandra Largo Alvarado | Paso 1 — Estructura base y clases abstractas |
| Yasmin Liseth Gelves Pena | Paso 2 — Clase Cliente |
| Jose Guzman | Paso 3 — Servicios especializados |
| Integrante 4 | Paso 4 — Clase Reserva |
| Integrante 5 | Paso 5 — Sistema principal y simulación |

---

## Pasos de desarrollo

### Paso 1 — Estructura base y clases abstractas
- Clase abstracta `Entidad` con atributos comunes: id, nombre, fecha de creación
- Clase abstracta `Servicio` con métodos abstractos: `calcular_costo()`, `describir()`, `validar_parametros()`
- Excepciones personalizadas: `ClienteInvalidoError`, `ServicioNoDisponibleError`, `ReservaInvalidaError`, `ParametroFaltanteError`, entre otras
- Configuración del logger para registro de eventos y errores en `eventos.log`

**Archivos:** `entidades/entidad_base.py`, `servicios/servicio_base.py`, `excepciones/excepciones.py`, `utils/logger.py`

---

### Paso 2 — Clase Cliente
- Hereda de `Entidad`
- Atributos encapsulados con propiedades y validaciones: nombre, email, teléfono, ID
- Lista interna de reservas asociadas al cliente
- Lanza `ClienteInvalidoError` ante datos inválidos

**Archivos:** `entidades/cliente.py`

---

### Paso 3 — Servicios especializados
- Tres clases que heredan de `Servicio`:
  - `ReservaSala` — costo por hora según capacidad
  - `AlquilerEquipo` — costo por día según tipo de equipo
  - `AsesoriaEspecializada` — costo variable según área y nivel
- Cada una implementa `calcular_costo()` con parámetros opcionales para descuentos e impuestos (sobrecarga simulada), `describir()` y `validar_parametros()`

**Archivos:** `servicios/reserva_sala.py`, `servicios/alquiler_equipo.py`, `servicios/asesoria.py`

---

### Paso 4 — Clase Reserva
- Atributos: cliente, servicio, duración, estado (`PENDIENTE`, `CONFIRMADA`, `CANCELADA`)
- Métodos: `confirmar()`, `cancelar()`, `procesar()`
- Manejo de excepciones con bloques `try/except`, `try/except/else`, `try/except/finally` y encadenamiento de excepciones
- Cada error se registra en el log antes de propagarse

**Archivos:** `entidades/reserva.py`

---

### Paso 5 — Sistema principal y simulación
- Clase `SistemaFJ` con listas internas: `clientes[]`, `servicios[]`, `reservas[]`
- Métodos: `registrar_cliente()`, `agregar_servicio()`, `crear_reserva()`
- Simulación de mínimo 10 operaciones: clientes válidos e inválidos, servicios correctos e incorrectos, reservas exitosas y fallidas
- El sistema nunca interrumpe su ejecución: cada error se captura, se loguea y continúa

**Archivos:** `main.py`

---

## Estructura del proyecto

```
software_fj/
│
├── entidades/
│   ├── __init__.py
│   ├── entidad_base.py
│   ├── cliente.py
│   └── reserva.py
│
├── servicios/
│   ├── __init__.py
│   ├── servicio_base.py
│   ├── reserva_sala.py
│   ├── alquiler_equipo.py
│   └── asesoria.py
│
├── excepciones/
│   ├── __init__.py
│   └── excepciones.py
│
├── utils/
│   ├── __init__.py
│   └── logger.py
│
├── eventos.log
├── README.md
└── main.py
```

## Estándar para NOMBRES

### Nombres de BRANCHES

| paso/autor/descripcion-corta |

Ejemplos:

- paso-1/alexandra/clases-abstractas-y-base
- paso-2/yasmin/clase-cliente
- paso-3/jhonatan/servicios-especializados
- paso-4/juan/clase-reserva
- paso-5/pedro/simulacion-principal

---

### Nombres de commits

| paso/tipo/autor/descripcion-corta |

| Tipo | Cuándo usarlo |
|---|---|
| `feat` | Agregar código nuevo |
| `fix` | Corregir un bug |
| `docs` | Documentación o comentarios |
| `refactor` | Reorganizar código |
| `chore` | Configuración o estructura |
| `test` | Agregar pruebas |
| `merge` | Merge de branches |

Ejemplos:

- paso-1/feat/alexandra/agrega-excepciones-personalizadas
- paso-2/feat/liseth/agrega-clase-cliente

---

### Nombres de Pull Requests y MERGES

| Paso N | Autor | Descripcion |

Ejemplos:

- Paso 1 | Alexandra | Clases Abstractas y Base
- Paso 2 | Liseth | Clase Cliente
- Paso 3 | Jhonatan | Servicios Especializados





