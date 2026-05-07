from .servicio_base import Servicio
from excepciones.excepciones import ParametroFaltanteError, SoftwareFJError
from utils.logger import logger

class AlquilerEquipo(Servicio):
    """
    Servicio de alquiler de equipos tecnológicos.
    Implementa polimorfismo y manejo de excepciones.
    """
    def __init__(self, id_entidad, nombre, tipo_equipo):
        super().__init__(id_entidad, nombre, "Alquiler de Equipo")
        self.__tipo_equipo = tipo_equipo
        self.__tarifas = {"Laptop": 35000, "Proyector": 25000, "Tablet": 15000}

    def validar_parametros(self, **kwargs):
        """Valida que los días sean mayores a cero."""
        if 'dias' not in kwargs or not isinstance(kwargs['dias'], (int, float)) or kwargs['dias'] <= 0:
            logger.error(f"Validación fallida en AlquilerEquipo: {kwargs.get('dias')} días")
            raise ParametroFaltanteError("El número de días debe ser un valor numérico mayor a 0.")

    def calcular_costo(self, dias=1, incluir_seguro=False, descuento=0.0):
        """
        Calcula el costo del alquiler.
        Simula sobrecarga con parámetros opcionales (seguro y descuento).
        """
        try:
            self.validar_parametros(dias=dias)
            tarifa_base = self.__tarifas.get(self.__tipo_equipo, 10000)
            subtotal = tarifa_base * dias
            
            if incluir_seguro:
                subtotal += (5000 * dias) # Seguro adicional por día
                
            total = subtotal * (1 - descuento)
            
            logger.info(f"Cálculo de costo exitoso para Alquiler {self.__tipo_equipo}: ${total}")
            return total
        except (ParametroFaltanteError, KeyError) as e:
            raise e
        except Exception as e:
            logger.critical(f"Error crítico en AlquilerEquipo: {str(e)}")
            raise SoftwareFJError(f"Fallo inesperado al procesar el servicio: {e}") from e

    def describir(self):
        return f"Servicio de Alquiler: {self.__tipo_equipo} (Tarifa base: ${self.__tarifas.get(self.__tipo_equipo, 0)}/día)"
