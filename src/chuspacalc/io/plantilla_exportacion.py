"""Plantillas reutilizables para configuraciones de exportación."""

from __future__ import annotations

from typing import Any

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion

FORMATOS_VALIDOS = ("json", "markdown", "md", "latex", "csv")

# Opciones que se pueden modificar con ``actualizar``.
_OPCIONES_ACTUALIZABLES = ("formato", "incluir_pasos", "campos")


class ErrorTipoPlantilla(ErrorValidacion, TypeError):
    """Error de validación por tipo de dato incorrecto.

    Hereda de ``ErrorValidacion`` (estandarizado) y de ``TypeError`` para
    conservar la compatibilidad con código que ya capturaba ``TypeError``.
    """


def _validar_formato(formato: object) -> None:
    """Valida que el formato sea uno de los soportados.

    Args:
        formato: Formato a validar.

    Raises:
        ErrorValidacion: Si el formato no está en ``FORMATOS_VALIDOS``.
    """
    if formato not in FORMATOS_VALIDOS:
        raise ErrorValidacion("Formato inválido: " + str(formato))


def _validar_campos(campos: object) -> None:
    """Valida que ``campos`` sea una lista de ``str``.

    Args:
        campos: Valor a validar.

    Raises:
        ErrorTipoPlantilla: Si no es una lista o contiene elementos no ``str``.
    """
    if not isinstance(campos, list):
        raise ErrorTipoPlantilla("campos debe ser una lista")
    for campo in campos:
        if not isinstance(campo, str):
            raise ErrorTipoPlantilla("todos los campos deben ser str")


def _validar_incluir_pasos(incluir_pasos: object) -> None:
    """Valida que ``incluir_pasos`` sea booleano.

    Args:
        incluir_pasos: Valor a validar.

    Raises:
        ErrorTipoPlantilla: Si no es ``bool``.
    """
    if not isinstance(incluir_pasos, bool):
        raise ErrorTipoPlantilla(
            f"incluir_pasos debe ser bool, se recibió {type(incluir_pasos).__name__}"
        )


class PlantillaExportacion:
    """Representa una configuración reutilizable para exportaciones."""

    def __init__(
        self,
        formato: str = "json",
        incluir_pasos: bool = False,
        campos: list[str] | None = None,
    ) -> None:
        """Crea la plantilla validando sus opciones.

        Args:
            formato: Formato de salida (ver ``FORMATOS_VALIDOS``).
            incluir_pasos: Si es ``True``, se incluyen los pasos del cálculo.
            campos: Lista de nombres de campos a exportar.

        Raises:
            ErrorValidacion: Si el formato no es válido.
            ErrorTipoPlantilla: Si ``incluir_pasos`` o ``campos`` tienen
                un tipo incorrecto.
        """
        _validar_formato(formato)
        _validar_incluir_pasos(incluir_pasos)
        if campos is not None:
            _validar_campos(campos)
        self.formato = formato
        self.incluir_pasos = incluir_pasos
        self.campos: list[str] = list(campos) if campos is not None else []

    def guardar(self) -> dict[str, Any]:
        """Devuelve la plantilla como un diccionario serializable."""
        return {
            "formato": self.formato,
            "incluir_pasos": self.incluir_pasos,
            "campos": self.campos.copy(),
        }

    @classmethod
    def cargar(cls, datos: dict[str, Any]) -> PlantillaExportacion:
        """Crea una plantilla a partir de un diccionario.

        Args:
            datos: Diccionario con las claves ``formato``, ``incluir_pasos``
                y ``campos`` (todas opcionales).

        Returns:
            La plantilla creada.

        Raises:
            ErrorTipoPlantilla: Si ``datos`` no es un ``dict`` o algún valor
                tiene un tipo incorrecto.
            ErrorValidacion: Si el formato no es válido.
        """
        if not isinstance(datos, dict):
            raise ErrorTipoPlantilla(
                f"Se esperaba un dict, se recibió {type(datos).__name__}"
            )

        return cls(
            formato=datos.get("formato", "json"),
            incluir_pasos=datos.get("incluir_pasos", False),
            campos=datos.get("campos", []),
        )

    def actualizar(self, **opciones: Any) -> None:
        """Actualiza la configuración de la plantilla.

        Solo se aplican ``formato``, ``incluir_pasos`` y ``campos``; las demás
        claves se ignoran. Todo se valida antes de modificar la plantilla, por
        lo que un error no deja cambios a medias.

        Args:
            **opciones: Opciones a modificar.

        Raises:
            ErrorValidacion: Si el formato no es válido.
            ErrorTipoPlantilla: Si ``incluir_pasos`` o ``campos`` tienen
                un tipo incorrecto.
        """
        if "formato" in opciones:
            _validar_formato(opciones["formato"])
        if "incluir_pasos" in opciones:
            _validar_incluir_pasos(opciones["incluir_pasos"])
        if "campos" in opciones:
            _validar_campos(opciones["campos"])

        for clave, valor in opciones.items():
            if clave not in _OPCIONES_ACTUALIZABLES:
                continue
            if clave == "campos":
                valor = list(valor)
            setattr(self, clave, valor)

    def copiar(self) -> PlantillaExportacion:
        """Devuelve una copia independiente de la plantilla."""
        return PlantillaExportacion.cargar(self.guardar())
