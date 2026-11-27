"""
Herramientas para cálculo de cargas distribuidas parciales en vigas.
"""

import math
from numbers import Real

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_numero(valor: object, nombre: str) -> float:
    """
    Verifica que el valor sea un número real finito y lo devuelve como float.

    Args:
        valor: Dato a validar.
        nombre: Nombre del parámetro, usado en el mensaje de error.

    Returns:
        El valor convertido a ``float``.

    Raises:
        ErrorValidacion: Si el tipo no es numérico (incluye ``bool``) o si
            el valor es NaN o infinito.
    """
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(
            f"{nombre} debe ser un número, se recibió {type(valor).__name__}"
        )
    try:
        numero = float(valor)
    except OverflowError:
        raise ErrorValidacion(f"{nombre} es demasiado grande para procesarse") from None
    if not math.isfinite(numero):
        raise ErrorValidacion(f"{nombre} debe ser un número finito")
    return numero


def calcular_reacciones_carga_parcial(
    longitud_viga: float,
    carga_por_metro: float,
    inicio_carga: float,
    fin_carga: float,
) -> dict[str, float]:
    """
    Calcula las reacciones en los apoyos para una carga
    distribuida uniforme aplicada sobre una parte de la viga.

    Args:
        longitud_viga: Longitud total de la viga (> 0).
        carga_por_metro: Carga distribuida por metro (> 0).
        inicio_carga: Posición donde empieza la carga (>= 0).
        fin_carga: Posición donde termina la carga (<= longitud_viga).

    Returns:
        Diccionario con ``reaccion_izquierda``, ``reaccion_derecha``,
        ``resultante`` y ``posicion_resultante``.

    Raises:
        ErrorValidacion: Si algún dato no es numérico, no es finito o
            está fuera de dominio.
    """

    longitud_viga = _validar_numero(longitud_viga, "longitud_viga")
    carga_por_metro = _validar_numero(carga_por_metro, "carga_por_metro")
    inicio_carga = _validar_numero(inicio_carga, "inicio_carga")
    fin_carga = _validar_numero(fin_carga, "fin_carga")

    if longitud_viga <= 0:
        raise ErrorValidacion("La longitud de la viga debe ser positiva")

    if carga_por_metro <= 0:
        raise ErrorValidacion("La carga por metro debe ser positiva")

    if inicio_carga < 0:
        raise ErrorValidacion("inicio_carga no puede ser negativo")

    if inicio_carga >= fin_carga:
        raise ErrorValidacion("inicio_carga debe ser menor que fin_carga")

    if fin_carga > longitud_viga:
        raise ErrorValidacion("fin_carga no puede superar la longitud de la viga")

    longitud_carga = fin_carga - inicio_carga

    resultante = carga_por_metro * longitud_carga

    posicion_resultante = (inicio_carga + fin_carga) / 2

    reaccion_derecha = (resultante * posicion_resultante) / longitud_viga

    reaccion_izquierda = resultante - reaccion_derecha

    return {
        "reaccion_izquierda": reaccion_izquierda,
        "reaccion_derecha": reaccion_derecha,
        "resultante": resultante,
        "posicion_resultante": posicion_resultante,
    }
