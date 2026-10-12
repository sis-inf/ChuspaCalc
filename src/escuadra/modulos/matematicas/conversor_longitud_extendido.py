from escuadra.modulos.matematicas.conversor_longitud import (
    UNIDADES_A_METROS as UNIDADES_BASE,
)

UNIDADES_A_METROS = {
    **UNIDADES_BASE,
    "ua": 1.496e11,
    "al": 9.461e15,
    "mn": 1852.0,
    "pc": 3.086e16,
}


def convertir_longitud(valor: float, unidad_origen: str, unidad_destino: str) -> float:
    if valor < 0:
        raise ValueError("El valor no puede ser negativo")

    de_unidad = unidad_origen.strip().lower()
    a_unidad = unidad_destino.strip().lower()

    if de_unidad not in UNIDADES_A_METROS:
        raise ValueError(f"Unidad origen no reconocida: {de_unidad}")

    if a_unidad not in UNIDADES_A_METROS:
        raise ValueError(f"Unidad destino no reconocida: {a_unidad}")

    valor_en_metros = valor * UNIDADES_A_METROS[de_unidad]
    return valor_en_metros / UNIDADES_A_METROS[a_unidad]
