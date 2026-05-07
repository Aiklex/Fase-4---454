import re
from entidades.entidad_base import EntidadBase
from excepciones.excepciones import ClienteInvalidoError

class Cliente(EntidadBase):
    def __init__(self, id_cliente, nombre, email, telefono):

        # pasamos id y nombre al padre para que los almacene
        super().__init__(id=id_cliente, nombre=nombre)
        # Atributos encapsulados (privados con __)
        # Ahora ya NO repites id ni nombre como atributos propios
        # porque ya los heredaste del padre (self.id y self.nombre)
        self.__email    = self.validar_email(email)
        self.__telefono = self.validar_telefono(telefono)
        self.__reservas = []

          # ── Validaciones ──────────────────────────────────────────────────────────

    def validar_email(self, email):
        if "@" not in email or "." not in email.split("@")[-1]:
            raise ClienteInvalidoError(f"Email inválido: '{email}'.")
        return email.lower()

    def validar_telefono(self, telefono):
        if not str(telefono).isdigit():
            raise ClienteInvalidoError("El teléfono debe contener solo números.")
        return str(telefono)

    # ── Getters (acceso controlado a atributos privados) ──────────────────────
    # self.id y self.nombre NO necesitan @property porque vienen
    # del padre como atributos públicos directamente accesibles.

    @property
    def email(self):
        return self.__email

    @property
    def telefono(self):
        return self.__telefono

    @property
    def reservas(self):
        return list(self.__reservas)  # retorna copia, no la lista original
    

    # ── Gestión de la lista interna de reservas ───────────────────────────────

    def agregar_reserva(self, id_reserva):
        """Asocia el ID de una reserva al cliente (en memoria, sin BD)."""
        self.__reservas.append(id_reserva)

    def eliminar_reserva(self, id_reserva):
        """Elimina una reserva de la lista interna si existe."""
        if id_reserva in self.__reservas:
            self.__reservas.remove(id_reserva)
            return True
        return False
    
      # ── Método abstracto obligatorio heredado de EntidadBase ─────────────────

    def __str__(self):
        return (
            f"Cliente ID  : {self.id}\n"
            f"Nombre      : {self.nombre}\n"
            f"Email       : {self.__email}\n"
            f"Teléfono    : {self.__telefono}\n"
            f"Reservas    : {len(self.__reservas)}\n"
            f"Registro    : {self.fecha_creacion.strftime('%Y-%m-%d %H:%M')}"
        )