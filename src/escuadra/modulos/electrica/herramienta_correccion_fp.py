"""
Herramienta para cálculo de corrección
del factor de potencia.
"""

from .correccion_fp import calcular_capacitancia_correccion


def herramienta_correccion_fp(
    potencia_activa,
    fp_actual,
    fp_deseado,
    voltaje,
    frecuencia=60,
):
    """
    Wrapper para calcular la capacitancia de corrección.
    """

    return calcular_capacitancia_correccion(
        potencia_activa,
        fp_actual,
        fp_deseado,
        voltaje,
        frecuencia,
    )
