"""
Modulo para combinacion de cargas vivas y muertas en ingenieria civil.

Este calculo es educativo y simplificado.
No reemplaza la normativa estructural local vigente.
"""


def _validar_cargas(carga_muerta: float, carga_viva: float) -> None:
    """
    Valida que las cargas suministradas no sean negativas.

    Raises:
        ValueError: si la carga muerta o la carga viva es negativa.
    """
    if carga_muerta < 0:
        raise ValueError("La carga muerta no puede ser negativa.")
    if carga_viva < 0:
        raise ValueError("La carga viva no puede ser negativa.")


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
        carga_muerta: carga permanente o muerta.
        carga_viva: carga variable o viva.
        factor_muerta: factor aplicado a carga muerta.
        factor_viva: factor aplicado a carga viva.

    Returns:
        Carga ultima combinada.

    Raises:
        ValueError: si la carga muerta o la carga viva es negativa.
    """
    _validar_cargas(carga_muerta, carga_viva)
    return factor_muerta * carga_muerta + factor_viva * carga_viva


def combinar_cargas_asd(carga_muerta: float, carga_viva: float) -> float:
    """
    Calcula la carga de servicio combinada mediante el metodo ASD.

    Formula:
        S = carga_muerta + carga_viva

    Args:
        carga_muerta: carga permanente o muerta.
        carga_viva: carga variable o viva.

    Returns:
        Carga combinada de servicio.

    Raises:
        ValueError: si la carga muerta o la carga viva es negativa.
    """
    _validar_cargas(carga_muerta, carga_viva)
    return carga_muerta + carga_viva


def combinacion_servicio(
    carga_muerta: float,
    carga_viva: float,
    viento: float = 0.0,
) -> dict:
    """
    Calcula las combinaciones de carga de servicio con factores unitarios.

    El viento se considera bidireccional: se evalua actuando a favor y en
    contra de las cargas gravitatorias, sin importar el signo recibido.

    Formulas:
        basica = 1.0 * carga_muerta + 1.0 * carga_viva
        viento_presion = basica + abs(viento)
        viento_succion = basica - abs(viento)

    Args:
        carga_muerta: carga permanente o muerta en kN.
        carga_viva: carga variable o viva en kN.
        viento: carga de viento en kN.

    Returns:
        Diccionario con las claves basica, viento_presion, viento_succion
        y critica, esta ultima con la combinacion de mayor magnitud, en kN.

    Raises:
        ValueError: si alguna carga es nula, o si la carga muerta o la
            carga viva es negativa.
    """
    if carga_muerta is None or carga_viva is None or viento is None:
        raise ValueError("Las cargas no pueden ser nulas.")
    _validar_cargas(carga_muerta, carga_viva)

    basica = carga_muerta + carga_viva
    viento_presion = basica + abs(viento)
    viento_succion = basica - abs(viento)

    return {
        "basica": basica,
        "viento_presion": viento_presion,
        "viento_succion": viento_succion,
        "critica": max(basica, viento_presion, viento_succion, key=abs),
    }
