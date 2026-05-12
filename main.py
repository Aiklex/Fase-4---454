# main.py
from entidades.cliente import Cliente
from entidades.reserva import Reserva
from servicios.reserva_sala import ReservaSala
from servicios.alquiler_equipo import AlquilerEquipo
from servicios.asesoria import AsesoriaEspecializada
from excepciones.excepciones import (
    SistemaFJError,
    ClienteInvalidoError,
    ServicioNoDisponibleError,
    ReservaInvalidaError,
    ParametroFaltanteError,
)

from utils.logger import logger


class SistemaFJ:
    def __init__(self):
        self.clientes = []
        self.servicios = []
        self.reservas = []

    def registrar_cliente(self, cliente):
        self.clientes.append(cliente)
        print(f" Cliente registrado: {cliente.nombre}")
        logger.info(f"Cliente registrado: {cliente.nombre}")

    def agregar_servicio(self, servicio):
        self.servicios.append(servicio)
        print(f" Servicio disponible: {servicio.nombre}")
        logger.info(f"Servicio agregado: {servicio.nombre}")

    def crear_reserva(self, reserva):
        reserva.procesar()
        self.reservas.append(reserva)
        print(f" Reserva confirmada para: {reserva.cliente.nombre}")
        logger.info(f"Reserva creada para {reserva.cliente.nombre}")


def ejecutar_simulacion():
    sistema = SistemaFJ()
    print("=== INICIANDO SIMULACIÓN SOFTWARE FJ (10 OPERACIONES) ===\n")

    # --- CLIENTES (4 operaciones) ---
    try:
        # 2-3 clientes válidos
        c1 = Cliente(1, "Alexandra Largo", "alex@mail.com", "3001")
        c2 = Cliente(2, "Jose Guzman", "jose@mail.com", "3002")
        sistema.registrar_cliente(c1)
        sistema.registrar_cliente(c2)

        # 1-2 clientes inválidos
        print("\nProbando cliente inválido...")
        c_inv = Cliente(3, "", "correo_mal", "000")
        sistema.registrar_cliente(c_inv)
    except ClienteInvalidoError as e:
        print(f" Error capturado en Cliente: {e}")

    try:
        # Cliente inválido por email
        print("\nProbando cliente con email inválido...")
        c_inv2 = Cliente(4, "Pedro Perez", "correosinservidor", "3003")
        sistema.registrar_cliente(c_inv2)
    except ClienteInvalidoError as e:
        print(f" Error capturado en Cliente: {e}")

    # --- SERVICIOS (4 operaciones) ---
    try:
        # 3 servicios correctos
        s1 = ReservaSala(101, "Sala Juntas", capacidad=10)
        s2 = AlquilerEquipo(102, "PC Gamer", tipo_equipo="Laptop")
        s3 = AsesoriaEspecializada(103, "Clase Java", area="Sistemas")
        sistema.agregar_servicio(s1)
        sistema.agregar_servicio(s2)
        sistema.agregar_servicio(s3)

        # 1 servicio incorrecto
        print("\nProbando servicio con parámetros incorrectos...")
        s_inv = ReservaSala(104, "Sala Error", capacidad=-5)
        s_inv.validar_parametros(horas=0)
    except (ParametroFaltanteError, ValueError) as e:
        print(f" Error capturado en Servicio: {e}")

    # --- RESERVAS (2 operaciones) ---
    try:
        # Reserva exitosa
        res1 = Reserva("RES-001", "Reserva Sala", c1, s1, "2 Horas")
        sistema.crear_reserva(res1)

        # Reserva fallida
        print("\nProbando reserva fallida...")
        res_fallida = Reserva("RES-002", "Reserva Fallida", None, s2, "1 Día")
        sistema.crear_reserva(res_fallida)
    except Exception as e:
        print(f" Error capturado en Reserva: {e}")

    try:
        # Segunda reserva exitosa
        res2 = Reserva("RES-003", "Reserva Equipo", c2, s2, "3 Dias")
        sistema.crear_reserva(res2)
    except Exception as e:
        print(f" Error capturado en Reserva: {e}")

    print("\n=== SIMULACIÓN FINALIZADA SIN CRASHES ===")


if __name__ == "__main__":
    ejecutar_simulacion()
