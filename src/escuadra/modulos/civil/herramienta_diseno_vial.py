from escuadra.modulos.civil.diseno_vial import (
    calcular_pendiente,
    calcular_peralte_curva,
    ErrorDisenoVial
)


def herramienta_diseno_vial(
    elevacion_inicial: float,
    elevacion_final: float,
    distancia_horizontal: float,
    velocidad_diseno: float,
    radio_curva: float,
    friccion_lateral: float = 0.15
) -> str:
    """
    Wrapper de herramienta para diseño vial
    """

    try:
        pendiente = calcular_pendiente(
            elevacion_inicial,
            elevacion_final,
            distancia_horizontal
        )

        peralte = calcular_peralte_curva(
            velocidad_diseno,
            radio_curva,
            friccion_lateral
        )

        return (
            f"PENDIENTE: {pendiente:.2f}%\n"
            f"PERALTE: {peralte:.4f}"
        )

    except ErrorDisenoVial as e:
        return f"ERROR: {str(e)}"
