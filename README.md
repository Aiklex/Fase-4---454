# Software FJ — Sistema Integral de Gestión de Clientes, Servicios y Reservas.

## Descripción del proyecto

Sistema orientado a objetos desarrollado en Python para gestionar clientes, servicios y reservas de la empresa ficticia **Software FJ**. La empresa ofrece tres tipos de servicios: reserva de salas, alquiler de equipos y asesorías especializadas.

El sistema opera completamente en memoria (sin base de datos), utilizando objetos, listas y manejo de archivos únicamente para el registro de eventos y errores. Implementa de forma rigurosa los principios de la programación orientada a objetos: abstracción, herencia, polimorfismo, encapsulación y manejo avanzado de excepciones.

Proyecto desarrollado como tarea grupal para el curso de Programación — Fase 4.

---

## Equipo de desarrollo

| Integrante | Paso asignado |
|---|---|
| Alexandra Largo Alvarado | Paso 1 — Estructura base y clases abstractas |
| Integrante 2 | Paso 2 — Clase Cliente |
| Integrante 3 | Paso 3 — Servicios especializados |
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

software_fj/
│
├── entidades/
│   ├── init.py
│   ├── entidad_base.py
│   ├── cliente.py
│   └── reserva.py
│
├── servicios/
│   ├── init.py
│   ├── servicio_base.py
│   ├── reserva_sala.py
│   ├── alquiler_equipo.py
│   └── asesoria.py
│
├── excepciones/
│   ├── init.py
│   └── excepciones.py
│
├── utils/
│   ├── init.py
│   └── logger.py
│
├── eventos.log
├── README.md
└── main.py

---

## Estándar de branches

### Formato
tipo/descripcion-en-español-con-guiones

### Tipos

| Tipo | Cuándo usarlo |
| `estructura/` | Organización de carpetas, configuración inicial |
| `feature/` | Agregar algo nuevo (una clase, un módulo) |
| `fix/` | Corregir un bug o error |
| `docs/` | Documentación o comentarios |
| `test/` | Agregar pruebas |

### Ejemplos

estructura/carpetas-base
feature/clase-cliente
feature/clase-reserva
feature/servicios-especializados
feature/excepciones-personalizadas
feature/logger
feature/simulacion-principal
fix/validacion-email-cliente
docs/readme

### Reglas
- Todo en **minúsculas**
- Palabras separadas con **guión** `-`
- Descripción corta y clara, máximo 3-4 palabras
- Descripciones siempre en **español**

---

## Ejecución del proyecto

```bash
python main.py
```

Los eventos y errores quedan registrados automáticamente en `eventos.log`.
