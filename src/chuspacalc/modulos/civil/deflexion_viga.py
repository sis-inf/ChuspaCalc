import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_real_finito(nombre: str, valor: float) -> None:
    """
    Comprueba que el valor sea un número real finito (sin contar bool).

    Raises:
        ErrorValidacion: Si el valor no es numérico o no es finito.
    """
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ErrorValidacion(f"{nombre} debe ser un número real")
    try:
        es_finito = math.isfinite(valor)
    except OverflowError:
        es_finito = False
    if not es_finito:
        raise ErrorValidacion(f"{nombre} debe ser un número finito")


def calcular_deflexion_max(
    longitud: float,
    carga: float,
    modulo_elasticidad: float,
    inercia: float,
    tipo_carga: str = "puntual_central",
) -> dict[str, float]:
    """
    Calcula la deflexión máxima de una viga simplemente apoyada.

    Para carga puntual central:
        δ = P * L³ / (48 * E * I)

    Para carga distribuida:
        δ = 5 * w * L⁴ / (384 * E * I)

    Retorna un diccionario con:
    - deflexion_max (mm)
    - posicion (m)

    Raises:
        ErrorValidacion: Si algún valor no es un número real finito, si no es
            mayor que cero, si el tipo de carga es inválido o si el resultado
            no es finito.
    """

    _validar_real_finito("La longitud de la viga", longitud)
    _validar_real_finito("La carga", carga)
    _validar_real_finito("El módulo de elasticidad", modulo_elasticidad)
    _validar_real_finito("La inercia", inercia)

    if longitud <= 0:
        raise ErrorValidacion("La longitud de la viga debe ser mayor que cero")

    if modulo_elasticidad <= 0 or inercia <= 0:
        raise ErrorValidacion(
            "La rigidez a flexión debe ser positiva (E e I deben ser mayores que cero)"
        )

    if carga <= 0:
        raise ErrorValidacion("La carga debe ser mayor que cero")

    try:
        if tipo_carga == "puntual_central":
            delta = (carga * longitud**3) / (48 * modulo_elasticidad * inercia)

        elif tipo_carga == "distribuida":
            delta = (5 * carga * longitud**4) / (384 * modulo_elasticidad * inercia)

        else:
            raise ErrorValidacion("Tipo de carga inválido")
    except OverflowError as error:
        raise ErrorValidacion("El resultado calculado no es finito") from error

    deflexion_max = delta * 1000
    if not math.isfinite(deflexion_max):
        raise ErrorValidacion("El resultado calculado no es finito")

    return {
        "deflexion_max": deflexion_max,
        "posicion": longitud / 2,
    }
