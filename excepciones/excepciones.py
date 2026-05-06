# excepciones/excepciones.py


class SistemaFJError(Exception):
    """Excepción base del sistema. Todas las excepciones personalizadas heredan de esta."""

    pass


class ClienteInvalidoError(SistemaFJError):
    """Se lanza cuando los datos de un cliente son inválidos."""

    pass


class ServicioNoDisponibleError(SistemaFJError):
    """Se lanza cuando un servicio no está disponible o no existe."""

    pass


class ReservaInvalidaError(SistemaFJError):
    """Se lanza cuando se intenta crear o procesar una reserva incorrecta."""

    pass


class ParametroFaltanteError(SistemaFJError):
    """Se lanza cuando falta un parámetro obligatorio."""

    pass


class OperacionNoPermitidaError(SistemaFJError):
    """Se lanza cuando se intenta realizar una operación no permitida."""

    pass


class CalculoInconsistenteError(SistemaFJError):
    """Se lanza cuando un cálculo produce un resultado inválido o inconsistente."""

    pass
