from escuadra.modulos.electrica.circuitos_rc_rl import (
    calcular_constante_tiempo_rc,
    calcular_constante_tiempo_rl,
    calcular_voltaje_carga_capacitor,
)


def herramienta_calcular_constante_tiempo_rc(resistencia, capacitancia):
    return calcular_constante_tiempo_rc(resistencia, capacitancia)


def herramienta_calcular_constante_tiempo_rl(resistencia, inductancia):
    return calcular_constante_tiempo_rl(resistencia, inductancia)


def herramienta_calcular_voltaje_carga_capacitor(
    voltaje_fuente, tiempo, constante_tiempo
):
    return calcular_voltaje_carga_capacitor(voltaje_fuente, tiempo, constante_tiempo)
