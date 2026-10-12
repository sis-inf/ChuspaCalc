"""
Herramientas para cálculo de cargas distribuidas parciales en vigas.
"""


def calcular_reacciones_carga_parcial(
    longitud_viga,
    carga_por_metro,
    inicio_carga,
    fin_carga,
):
    """
    Calcula las reacciones en los apoyos para una carga
    distribuida uniforme aplicada sobre una parte de la viga.
    """

    if longitud_viga <= 0:
        raise ValueError("La longitud de la viga debe ser positiva")

    if carga_por_metro <= 0:
        raise ValueError("La carga por metro debe ser positiva")

    if inicio_carga < 0:
        raise ValueError("inicio_carga no puede ser negativo")

    if inicio_carga >= fin_carga:
        raise ValueError("inicio_carga debe ser menor que fin_carga")

    if fin_carga > longitud_viga:
        raise ValueError("fin_carga no puede superar la longitud de la viga")

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
