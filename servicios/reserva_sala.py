from servicios.servicio_base import Servicio
from excepciones.excepciones import ParametroFaltanteError, SistemaFJError
from utils.logger import logger

class ReservaSala(Servicio):
    """
    Servicio de reserva de salas físicas.
    Implementa polimorfismo y manejo de excepciones.
    """
    def __init__(self, id_entidad, nombre, capacidad):
        super().__init__(id=id_entidad, nombre=nombre)
        self.__capacidad = capacidad
        self.__precio_hora_base = 50000

    def validar_parametros(self, **kwargs):
        """Valida horas y capacidad."""
        horas = kwargs.get('horas', 0)
        personas = kwargs.get('personas', 0)

        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ParametroFaltanteError("El tiempo de reserva debe ser mayor a 0 horas.")

        if personas > self.__capacidad:
            logger.warning(f"Sobrecapacidad detectada: {personas} personas en sala de {self.__capacidad}")
            raise SistemaFJError(f"La sala solo tiene capacidad para {self.__capacidad} personas.")

    def calcular_costo(self, horas=1, incluir_refrigerio=False, personas=0):
        """
        Calcula el costo total de la reserva.
        Simula sobrecarga con extras (refrigerio) y validación de capacidad.
        """
        try:
            self.validar_parametros(horas=horas, personas=personas)
            total = self.__precio_hora_base * horas

            if incluir_refrigerio:
                total += (15000 * personas) # 15k adicionales por refrigerio de cada persona

            logger.info(f"Cálculo de sala exitoso: ${total} para {personas} personas")
            return total
        except (ParametroFaltanteError, SistemaFJError) as e:
            raise e
        except Exception as e:
            logger.critical(f"Error sistémico en reserva de sala: {str(e)}")
            raise SistemaFJError(f"Fallo crítico al reservar: {e}") from e

    def describir(self):
        return f"Sala '{self.nombre}' (Capacidad: {self.__capacidad} pers., Tarifa: ${self.__precio_hora_base}/h)"

    def __str__(self):
        return f"Sala '{self.nombre}' (Capacidad: {self._ReservaSala__capacidad} pers., Tarifa: ${self._ReservaSala__precio_hora_base}/h)"
