# entidades/entidad_base.py

from abc import ABC, abstractmethod
from datetime import datetime


class Entidad(ABC):

    def __init__(self, id, nombre):
        self.id = id
        self.nombre = nombre
        self.fecha_creacion = datetime.now()

    @abstractmethod
    def __str__(self):
        pass
