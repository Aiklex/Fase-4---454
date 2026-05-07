from .servicio_base import Servicio
from excepciones.excepciones import ParametroFaltanteError, SoftwareFJError
from utils.logger import logger

class AsesoriaEspecializada(Servicio):
    """
    Servicio de asesoría técnica por niveles.
    Implementa polimorfismo y manejo de excepciones avanzado.
    """
    def __init__(self, id_entidad, nombre, area):
        super().__init__(id_entidad, nombre, "Asesoría")
        self.__area = area
        self.__tarifas_por_nivel = {"Junior": 80000, "Senior": 150000, "Expert": 250000}

    def validar_parametros(self, **kwargs):
        """Valida que el nivel exista y las horas sean positivas."""
        nivel = kwargs.get('nivel')
        horas = kwargs.get('horas', 1)
        
        if nivel not in self.__tarifas_por_nivel:
            logger.warning(f"Intento de uso de nivel inválido: {nivel}")
            raise ParametroFaltanteError(f"Nivel '{nivel}' no es válido. Opciones: Junior, Senior, Expert.")
            
        if not isinstance(horas, (int, float)) or horas <= 0:
            raise ParametroFaltanteError("La cantidad de horas debe ser un número mayor a 0.")

    def calcular_costo(self, nivel="Junior", horas=1, es_festivo=False):
        """
        Calcula el costo basado en el nivel de expertise y horas.
        Incluye recargo por días festivos (simulación de sobrecarga).
        """
        try:
            self.validar_parametros(nivel=nivel, horas=horas)
            base = self.__tarifas_por_nivel[nivel] * horas
            
            if es_festivo:
                base *= 1.20 # 20% de recargo por día festivo
                
            logger.info(f"Costo calculado para Asesoría ({self.__area}): ${base} (Nivel: {nivel})")
            return base
        except (ParametroFaltanteError, KeyError) as e:
            raise e
        except Exception as e:
            logger.critical(f"Error fatal en cálculo de Asesoría: {str(e)}")
            raise SoftwareFJError(f"Error en el sistema de asesorías: {e}") from e

    def describir(self):
        return f"Asesoría técnica en {self.__area}. Consultores niveles: Junior, Senior y Expert."
