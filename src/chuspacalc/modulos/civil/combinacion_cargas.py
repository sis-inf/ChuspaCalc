"""
Modulo para combinacion de cargas vivas y muertas en ingenieria civil.

Este calculo es educativo y simplificado.
No reemplaza la normativa estructural local vigente.
"""

import math

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_numero,
)


def _validar_cargas(carga_muerta: object, carga_viva: object) -> tuple[float, float]:
    """
    Valida que las cargas suministradas sean numeros finitos no negativos.

    Args:
        carga_muerta: carga permanente o muerta.
        carga_viva: carga variable o viva.

    Returns:
        Tupla con la carga muerta y la carga viva convertidas a float.

    Raises:
        ErrorValidacion: si alguna carga no es un numero real finito, es
            booleana o es negativa.
    """
    validadas: list[float] = []

    for nombre, carga in (("carga_muerta", carga_muerta), ("carga_viva", carga_viva)):
        numero = validar_numero(carga, nombre)

        if numero < 0:
            raise ErrorValidacion(
                f"El valor de '{nombre}' no puede ser negativo "
                f"(valor recibido: {numero})."
            )

        validadas.append(numero)

    return validadas[0], validadas[1]


def _validar_resultado(valor: float, nombre: str) -> float:
    """
    Verifica que un resultado intermedio siga siendo finito.

    Args:
        valor: resultado a comprobar.
        nombre: nombre del resultado, usado en el mensaje de error.

    Returns:
        El mismo valor cuando es finito.

    Raises:
        ErrorValidacion: si el valor se desborda o no es finito.
    """
    if not math.isfinite(valor):
        raise ErrorValidacion(
            f"El resultado '{nombre}' esta fuera del rango representable."
        )

    return valor


def combinar_cargas_lrfd(
    carga_muerta: float,
    carga_viva: float,
    factor_muerta: float = 1.2,
    factor_viva: float = 1.6,
) -> float:
    """
    Calcula la carga ultima de diseno mediante factores LRFD.

    Formula:
        U = factor_muerta * carga_muerta + factor_viva * carga_viva

    Args:
        carga_muerta: carga permanente o muerta. Debe ser finita y no negativa.
        carga_viva: carga variable o viva. Debe ser finita y no negativa.
        factor_muerta: factor aplicado a carga muerta. Debe ser finito.
        factor_viva: factor aplicado a carga viva. Debe ser finito.

    Returns:
        Carga ultima combinada.

    Raises:
        ErrorValidacion: si alguna carga o factor no es un numero real
            finito, si es booleano, si una carga es negativa o si el
            resultado se desborda.
    """
    muerta, viva = _validar_cargas(carga_muerta, carga_viva)
    peso_muerta = validar_numero(factor_muerta, "factor_muerta")
    peso_viva = validar_numero(factor_viva, "factor_viva")

    return _validar_resultado(peso_muerta * muerta + peso_viva * viva, "carga ultima")


def combinar_cargas_asd(carga_muerta: float, carga_viva: float) -> float:
    """
    Calcula la carga de servicio combinada mediante el metodo ASD.

    Formula:
        S = carga_muerta + carga_viva

    Args:
        carga_muerta: carga permanente o muerta. Debe ser finita y no negativa.
        carga_viva: carga variable o viva. Debe ser finita y no negativa.

    Returns:
        Carga combinada de servicio.

    Raises:
        ErrorValidacion: si alguna carga no es un numero real finito, es
            booleana, es negativa o si el resultado se desborda.
    """
    muerta, viva = _validar_cargas(carga_muerta, carga_viva)

    return _validar_resultado(muerta + viva, "carga de servicio")


def combinacion_servicio(
    carga_muerta: float,
    carga_viva: float,
    viento: float = 0.0,
) -> dict[str, float]:
    """
    Calcula las combinaciones de carga de servicio con factores unitarios.

    El viento se considera bidireccional: se evalua actuando a favor y en
    contra de las cargas gravitatorias, sin importar el signo recibido.

    Formulas:
        basica = 1.0 * carga_muerta + 1.0 * carga_viva
        viento_presion = basica + abs(viento)
        viento_succion = basica - abs(viento)

    Args:
        carga_muerta: carga permanente o muerta en kN. Debe ser finita y
            no negativa.
        carga_viva: carga variable o viva en kN. Debe ser finita y no
            negativa.
        viento: carga de viento en kN. Debe ser finita.

    Returns:
        Diccionario con las claves basica, viento_presion, viento_succion
        y critica, esta ultima con la combinacion de mayor magnitud, en kN.

    Raises:
        ErrorValidacion: si alguna carga es nula, no es un numero real
            finito, es booleana, si la carga muerta o la carga viva es
            negativa o si algun resultado se desborda.
    """
    muerta, viva = _validar_cargas(carga_muerta, carga_viva)
    empuje = validar_numero(viento, "viento")

    basica = _validar_resultado(muerta + viva, "basica")
    viento_presion = _validar_resultado(basica + abs(empuje), "viento_presion")
    viento_succion = _validar_resultado(basica - abs(empuje), "viento_succion")

    return {
        "basica": basica,
        "viento_presion": viento_presion,
        "viento_succion": viento_succion,
        "critica": max(basica, viento_presion, viento_succion, key=abs),
    }
