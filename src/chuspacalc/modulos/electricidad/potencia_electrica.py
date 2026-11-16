
import math


def calcular_potencia(voltaje, corriente):
    """
    Calcula la potencia eléctrica mediante la fórmula P = V * I.

    Args:
        voltaje: Tensión eléctrica expresada en voltios.
        corriente: Corriente eléctrica expresada en amperios.

    Returns:
        Potencia eléctrica expresada en vatios.

    Raises:
        TypeError: Si los argumentos no son números reales.
        ValueError: Si algún argumento no es finito.
    """
    if isinstance(voltaje, bool) or not isinstance(voltaje, (int, float)):
        raise TypeError("El voltaje debe ser un número real.")

    if isinstance(corriente, bool) or not isinstance(corriente, (int, float)):
        raise TypeError("La corriente debe ser un número real.")

    if not math.isfinite(voltaje):
        raise ValueError("El voltaje debe ser un valor finito.")

    if not math.isfinite(corriente):
        raise ValueError("La corriente debe ser un valor finito.")

    potencia = voltaje * corriente

    if not math.isfinite(potencia):
        raise ValueError("El resultado de la potencia debe ser finito.")

    return potencia
