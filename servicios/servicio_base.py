# servicios/servicio_base.py

from abc import abstractmethod
from entidades.entidad_base import Entidad


class Servicio(Entidad):

    @abstractmethod
    def calcular_costo(self):
        pass

    @abstractmethod
    def describir(self):
        pass

    @abstractmethod
    def validar_parametros(self):
        pass
