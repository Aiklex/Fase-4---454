from entidades.entidad_base import Entidad
from excepciones.excepciones import ReservaInvalidaError
from entidades.cliente import Cliente
from servicios.servicio_base import Servicio
from utils.logger import logger

class Reserva(Entidad):
    def __init__(self, id_reserva, nombre, cliente, servicio, duracion):
        super().__init__(id=id_reserva, nombre=nombre)
        if not isinstance(cliente, Cliente):
            raise ReservaInvalidaError("El cliente no es válido.")
        if not isinstance(servicio, Servicio):
            raise ReservaInvalidaError("El servicio no es válido.")
        self.cliente = cliente
        self.servicio = servicio
        self.duracion = duracion
        self.estado = "PENDIENTE"

    def confirmar(self):
        self.estado = "CONFIRMADA"
        logger.info(f"Reserva {self.id} confirmada.")

    def cancelar(self):
        try:
            self.estado = "CANCELADA"
        except Exception as e:
            raise ReservaInvalidaError(f"Error al cancelar la reserva: {e}") from e
        finally:
            logger.info(f"Intento de cancelación para reserva {self.id}")

    def procesar(self):
        try:
            self.servicio.calcular_costo()
        except Exception as e:
            logger.error(f"Error al procesar reserva {self.id}: {e}")
            self.estado = "CANCELADA"
            raise ReservaInvalidaError(f"Error al procesar la reserva: {e}") from e
        else:
            self.estado = "CONFIRMADA"
            logger.info(f"Reserva {self.id} procesada exitosamente.")

    def __str__(self):
        return f"Reserva(id={self.id}, nombre='{self.nombre}', cliente='{self.cliente}', servicio='{self.servicio}', duracion={self.duracion}, estado='{self.estado}')"
