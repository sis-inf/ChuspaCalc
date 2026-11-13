
import math


def calcular_esfuerzo_axial(fuerza, area):
    """
    Calcula el esfuerzo normal producido por una fuerza axial.

    Args:
        fuerza: Fuerza axial en Newtons (N).
                Positiva para tracción y negativa para compresión.
        area: Área transversal en metros cuadrados (m²).

    Returns:
        float: Esfuerzo axial en Pascales (Pa).

    Raises:
        ValueError: Si la fuerza no es numérica o finita,
                    o si el área no es positiva y finita.
    """

    if isinstance(fuerza, bool) or not isinstance(fuerza, (int, float)):
        raise ValueError("La fuerza debe ser un valor numérico.")

    if isinstance(area, bool) or not isinstance(area, (int, float)):
        raise ValueError("El área debe ser un valor numérico.")

    if not math.isfinite(fuerza):
        raise ValueError("La fuerza debe ser finita.")

    if not math.isfinite(area) or area <= 0:
        raise ValueError("El área debe ser positiva y finita.")

    esfuerzo = fuerza / area

    if not math.isfinite(esfuerzo):
        raise ValueError("El esfuerzo calculado debe ser finito.")

    return esfuerzo
