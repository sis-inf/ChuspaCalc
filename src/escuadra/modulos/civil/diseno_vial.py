class ErrorDisenoVial(Exception):
    pass


def calcular_pendiente(
    elevacion_inicial: float, elevacion_final: float, distancia_horizontal: float
) -> float:
    """
    Calcula pendiente en porcentaje (%)
    """

    if distancia_horizontal <= 0:
        raise ErrorDisenoVial("La distancia horizontal debe ser mayor a 0")

    pendiente = ((elevacion_final - elevacion_inicial) / distancia_horizontal) * 100
    return pendiente


def calcular_peralte_curva(
    velocidad_diseno: float, radio_curva: float, friccion_lateral: float = 0.15
) -> float:
    """
    Calcula peralte básico de curva horizontal
    """

    if radio_curva <= 0:
        raise ErrorDisenoVial("El radio de curva debe ser mayor a 0")

    if velocidad_diseno <= 0:
        raise ErrorDisenoVial("La velocidad debe ser mayor a 0")

    g = 9.81

    v = velocidad_diseno / 3.6  # km/h → m/s

    peralte = (v**2) / (g * radio_curva) - friccion_lateral

    return peralte
