import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


class ErrorDisenoVial(ErrorValidacion):
    pass


def _validar_real_finito(nombre: str, valor: float) -> None:
    """
    Comprueba que el valor sea un número real finito (sin contar bool).

    Raises:
        ErrorDisenoVial: Si el valor no es numérico o no es finito.
    """
    if isinstance(valor, bool) or not isinstance(valor, (int, float)):
        raise ErrorDisenoVial(f"{nombre} debe ser un número")
    try:
        es_finito = math.isfinite(valor)
    except OverflowError:
        es_finito = False
    if not es_finito:
        raise ErrorDisenoVial(f"{nombre} debe ser un número finito")


def _resultado_finito(resultado: float) -> float:
    """Comprueba que el resultado calculado sea finito."""
    if not math.isfinite(resultado):
        raise ErrorDisenoVial("El resultado calculado no es finito")
    return resultado


def calcular_pendiente(
    elevacion_inicial: float, elevacion_final: float, distancia_horizontal: float
) -> float:
    """
    Calcula pendiente en porcentaje (%)

    Raises:
        ErrorDisenoVial: Si algún valor no es un número finito, si la distancia
            horizontal no es mayor a 0 o si el resultado no es finito.
    """

    _validar_real_finito("La elevación inicial", elevacion_inicial)
    _validar_real_finito("La elevación final", elevacion_final)
    _validar_real_finito("La distancia horizontal", distancia_horizontal)

    if distancia_horizontal <= 0:
        raise ErrorDisenoVial("La distancia horizontal debe ser mayor a 0")

    try:
        pendiente = (
            (elevacion_final - elevacion_inicial) / distancia_horizontal
        ) * 100
    except OverflowError as error:
        raise ErrorDisenoVial("El resultado calculado no es finito") from error
    return _resultado_finito(pendiente)


def calcular_peralte_curva(
    velocidad_diseno: float, radio_curva: float, friccion_lateral: float = 0.15
) -> float:
    """
    Calcula peralte básico de curva horizontal

    Raises:
        ErrorDisenoVial: Si algún valor no es un número finito, si el radio o la
            velocidad no son mayores a 0 o si el resultado no es finito.
    """

    _validar_real_finito("La velocidad", velocidad_diseno)
    _validar_real_finito("El radio de curva", radio_curva)
    _validar_real_finito("La fricción lateral", friccion_lateral)

    if radio_curva <= 0:
        raise ErrorDisenoVial("El radio de curva debe ser mayor a 0")

    if velocidad_diseno <= 0:
        raise ErrorDisenoVial("La velocidad debe ser mayor a 0")

    g = 9.81

    v = velocidad_diseno / 3.6  # km/h → m/s

    try:
        peralte = (v**2) / (g * radio_curva) - friccion_lateral
    except OverflowError as error:
        raise ErrorDisenoVial("El resultado calculado no es finito") from error

    return _resultado_finito(peralte)
