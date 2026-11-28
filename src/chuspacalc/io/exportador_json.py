"""Módulo para exportar resultados de cálculo a archivos JSON."""

import json
import os
from typing import Any

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


class ErrorTipoExportacion(ErrorValidacion, TypeError):
    """Error de validación por tipo de dato incorrecto.

    Hereda de ``ErrorValidacion`` (estandarizado) y de ``TypeError`` para
    conservar la compatibilidad con código que ya capturaba ``TypeError``.
    """


def _validar_ruta(ruta_archivo: object) -> str:
    """Valida que la ruta sea un texto no vacío.

    Args:
        ruta_archivo: Ruta del archivo a validar.

    Returns:
        La ruta validada.

    Raises:
        ErrorTipoExportacion: Si la ruta no es texto.
        ErrorValidacion: Si la ruta está vacía o es solo espacios.
    """
    if not isinstance(ruta_archivo, str):
        raise ErrorTipoExportacion(
            f"La ruta debe ser texto, se recibió {type(ruta_archivo).__name__}"
        )
    if not ruta_archivo.strip():
        raise ErrorValidacion("La ruta del archivo no puede estar vacía")
    return ruta_archivo


def _escribir_json(datos: Any, ruta_archivo: str, sobreescribir: bool) -> None:
    """Escribe ``datos`` como JSON con indentación de 2 espacios.

    Args:
        datos: Objeto serializable a JSON.
        ruta_archivo: Ruta de destino (ya validada).
        sobreescribir: Si es ``False`` y el archivo existe, falla.

    Raises:
        FileExistsError: Si el archivo existe y no se permite sobreescribir.
        ErrorValidacion: Si ``datos`` contiene valores no serializables a JSON.
    """
    if os.path.exists(ruta_archivo) and not sobreescribir:
        raise FileExistsError(ruta_archivo)

    try:
        contenido = json.dumps(datos, indent=2, ensure_ascii=False)
    except (TypeError, ValueError) as error:
        raise ErrorValidacion(
            f"Los datos no se pueden serializar a JSON: {error}"
        ) from error

    directorio = os.path.dirname(ruta_archivo)
    if directorio and not os.path.exists(directorio):
        os.makedirs(directorio, exist_ok=True)

    with open(ruta_archivo, "w", encoding="utf-8") as f:
        f.write(contenido)


def exportar_resultado(
    resultado: dict[str, Any], ruta_archivo: str, sobreescribir: bool = False
) -> None:
    """Exporta un diccionario a un archivo JSON con indentación de 2 espacios.

    Args:
        resultado: Diccionario a exportar.
        ruta_archivo: Ruta del archivo JSON de destino.
        sobreescribir: Si es ``True``, reemplaza un archivo existente.

    Raises:
        ErrorTipoExportacion: Si ``resultado`` no es ``dict`` o la ruta no es texto.
        ErrorValidacion: Si la ruta está vacía o los datos no son serializables.
        FileExistsError: Si el archivo existe y ``sobreescribir`` es ``False``.
    """
    if not isinstance(resultado, dict):
        raise ErrorTipoExportacion(
            f"Se esperaba un dict, se recibió {type(resultado).__name__}"
        )
    ruta = _validar_ruta(ruta_archivo)
    _escribir_json(resultado, ruta, sobreescribir)


def exportar_lista(
    resultados: list[Any], ruta_archivo: str, sobreescribir: bool = False
) -> None:
    """Exporta una lista de resultados a un archivo JSON con indentación de 2.

    Args:
        resultados: Lista a exportar.
        ruta_archivo: Ruta del archivo JSON de destino.
        sobreescribir: Si es ``True``, reemplaza un archivo existente.

    Raises:
        ErrorTipoExportacion: Si ``resultados`` no es ``list`` o la ruta no es texto.
        ErrorValidacion: Si la ruta está vacía o los datos no son serializables.
        FileExistsError: Si el archivo existe y ``sobreescribir`` es ``False``.
    """
    if not isinstance(resultados, list):
        raise ErrorTipoExportacion(
            f"Se esperaba una list, se recibió {type(resultados).__name__}"
        )
    ruta = _validar_ruta(ruta_archivo)
    _escribir_json(resultados, ruta, sobreescribir)
