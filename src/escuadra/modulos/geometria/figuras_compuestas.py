from .calculo_area import (
    area_triangulo,
    area_circulo,
    area_rectangulo,
)

from .volumen import (
    volumen_cubo,
    volumen_esfera,
    volumen_cilindro,
    volumen_cono,
    volumen_paralelepipedo,
)


FUNCIONES_AREA = {
    "triangulo": area_triangulo,
    "circulo": area_circulo,
    "rectangulo": area_rectangulo,
}


FUNCIONES_VOLUMEN = {
    "cubo": volumen_cubo,
    "esfera": volumen_esfera,
    "cilindro": volumen_cilindro,
    "cono": volumen_cono,
    "paralelepipedo": volumen_paralelepipedo,
}


def calcular_area_compuesta(figuras):
    """
    Calcula el área total de una figura compuesta.

    Cada figura debe tener el siguiente formato:

    {
        "tipo": "rectangulo",
        "parametros": {
            "base": 10,
            "altura": 5
        },
        "operacion": "sumar"
    }
    """

    total = 0

    for figura in figuras:
        tipo = figura["tipo"]
        parametros = figura["parametros"]
        operacion = figura.get("operacion", "sumar")

        if tipo not in FUNCIONES_AREA:
            raise ValueError(f"Figura de área no soportada: {tipo}")

        resultado = FUNCIONES_AREA[tipo](**parametros)

        if operacion == "sumar":
            total += resultado
        elif operacion == "restar":
            total -= resultado
        else:
            raise ValueError(f"Operación no válida: {operacion}")

    return total


def calcular_volumen_compuesto(figuras):
    """
    Calcula el volumen total de una figura compuesta.

    Cada figura debe tener el siguiente formato:

    {
        "tipo": "cilindro",
        "parametros": {
            "radio": 2,
            "altura": 5
        },
        "operacion": "sumar"
    }
    """

    total = 0

    for figura in figuras:
        tipo = figura["tipo"]
        parametros = figura["parametros"]
        operacion = figura.get("operacion", "sumar")

        if tipo not in FUNCIONES_VOLUMEN:
            raise ValueError(f"Figura de volumen no soportada: {tipo}")

        resultado = FUNCIONES_VOLUMEN[tipo](**parametros)

        if operacion == "sumar":
            total += resultado
        elif operacion == "restar":
            total -= resultado
        else:
            raise ValueError(f"Operación no válida: {operacion}")

    return total
