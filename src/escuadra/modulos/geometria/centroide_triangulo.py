
import math


def calcular_centroide_triangulo(p1, p2, p3):
    """
    Calcula las coordenadas del centroide de un triángulo.

    Args:
        p1: Tupla con las coordenadas (x, y) del primer vértice.
        p2: Tupla con las coordenadas (x, y) del segundo vértice.
        p3: Tupla con las coordenadas (x, y) del tercer vértice.

    Returns:
        Tupla (x, y) con las coordenadas del centroide.

    Raises:
        TypeError: Si las coordenadas no son numéricas.
        ValueError: Si los puntos no tienen dos coordenadas
                    o contienen valores no finitos.
    """
    puntos = (p1, p2, p3)

    for punto in puntos:
        if not isinstance(punto, (tuple, list)) or len(punto) != 2:
            raise ValueError("Cada vértice debe contener dos coordenadas.")

        for coordenada in punto:
            if isinstance(coordenada, bool) or not isinstance(coordenada, (int, float)):
                raise TypeError("Las coordenadas deben ser numéricas.")

            if not math.isfinite(coordenada):
                raise ValueError("Las coordenadas deben ser finitas.")

    cx = (p1[0] + p2[0] + p3[0]) / 3
    cy = (p1[1] + p2[1] + p3[1]) / 3

    return (cx, cy)
