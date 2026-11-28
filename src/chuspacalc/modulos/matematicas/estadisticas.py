import math
from collections.abc import Sequence
from numbers import Real

from .error_validacion import ErrorValidacion

Numero = int | float

_MENSAJE_FUERA_DE_RANGO = "El resultado esta fuera del rango permitido."


def _validar_datos(datos: Sequence[Numero]) -> None:
    if not isinstance(datos, Sequence) or isinstance(datos, (str, bytes)):
        raise ErrorValidacion(
            "Los datos deben ser una lista o tupla de numeros reales.",
        )

    if not datos:
        raise ErrorValidacion("La lista no puede estar vacia")

    for posicion, valor in enumerate(datos):
        if isinstance(valor, bool) or not isinstance(valor, Real):
            raise ErrorValidacion(
                f"El dato en la posicion {posicion} debe ser un numero real.",
            )

        if isinstance(valor, int):
            continue

        if not math.isfinite(valor):
            raise ErrorValidacion(
                f"El dato en la posicion {posicion} debe ser finito.",
            )


def _validar_resultado(resultado: float) -> float:
    if not math.isfinite(resultado):
        raise ErrorValidacion("El resultado debe ser finito.")

    return resultado


def calcular_media(datos: Sequence[Numero]) -> float:
    _validar_datos(datos)

    try:
        resultado = float(sum(datos) / len(datos))
    except OverflowError as exc:
        raise ErrorValidacion(_MENSAJE_FUERA_DE_RANGO) from exc

    return _validar_resultado(resultado)


def calcular_mediana(datos: Sequence[Numero]) -> float:
    _validar_datos(datos)

    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    mitad = n // 2

    try:
        if n % 2 == 0:
            resultado = float(
                (datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2,
            )
        else:
            resultado = float(datos_ordenados[mitad])
    except OverflowError as exc:
        raise ErrorValidacion(_MENSAJE_FUERA_DE_RANGO) from exc

    return _validar_resultado(resultado)


def calcular_moda(datos: Sequence[Numero]) -> list[Numero]:
    _validar_datos(datos)

    frecuencias: dict[Numero, int] = {}

    for valor in datos:
        frecuencias[valor] = frecuencias.get(valor, 0) + 1

    maxima = max(frecuencias.values())

    return [valor for valor, frec in frecuencias.items() if frec == maxima]


def calcular_desviacion_estandar(
    datos: Sequence[Numero],
    poblacional: bool = False,
) -> float:
    _validar_datos(datos)

    if not isinstance(poblacional, bool):
        raise ErrorValidacion("El parametro 'poblacional' debe ser booleano.")

    n = len(datos)

    if not poblacional and n < 2:
        raise ErrorValidacion(
            "Se requieren al menos dos datos para la desviacion muestral",
        )

    try:
        media = sum(datos) / n

        suma_cuadrados: float = 0.0

        for valor in datos:
            suma_cuadrados += (valor - media) ** 2

        divisor = n if poblacional else n - 1

        varianza = suma_cuadrados / divisor

        resultado = float(varianza**0.5)
    except OverflowError as exc:
        raise ErrorValidacion(_MENSAJE_FUERA_DE_RANGO) from exc

    return _validar_resultado(resultado)
