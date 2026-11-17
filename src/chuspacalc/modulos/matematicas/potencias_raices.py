import math
from numbers import Real

from .error_validacion import ErrorValidacion

_MENSAJE_RESULTADO = "El resultado calculado no es finito"


def _validar_real_finito(valor: int | float, nombre: str) -> None:
    """Comprueba que el valor sea un número real finito (sin contar bool)."""
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(f"{nombre} debe ser un número real")

    if isinstance(valor, int):
        return

    try:
        es_finito = math.isfinite(valor)
    except OverflowError:
        es_finito = False

    if not es_finito:
        raise ErrorValidacion(f"{nombre} debe ser un número finito")


def _resultado_finito(resultado: float) -> float:
    """Comprueba que el resultado calculado sea finito."""
    if not math.isfinite(resultado):
        raise ErrorValidacion(_MENSAJE_RESULTADO)
    return resultado


def potencia(base: int | float, exponente: int | float) -> float:
    """
    Calcula una potencia.

    Fórmula:
        resultado = base ** exponente

    Raises:
        ErrorValidacion: Si base o exponente no son números reales finitos,
            si la base es cero con exponente negativo, si la base es
            negativa con exponente no entero o si el resultado no es finito.
    """
    _validar_real_finito(base, "La base")
    _validar_real_finito(exponente, "El exponente")

    if base == 0 and exponente < 0:
        raise ErrorValidacion("No se puede elevar cero a un exponente negativo")

    if base < 0 and exponente % 1 != 0:
        raise ErrorValidacion("Una base negativa requiere un exponente entero")

    try:
        resultado = float(base**exponente)
    except OverflowError as error:
        raise ErrorValidacion(_MENSAJE_RESULTADO) from error

    return _resultado_finito(resultado)


def raiz_n(valor: int | float, n: int) -> float:
    """
    Calcula la raíz n-ésima de un número.

    Raises:
        ErrorValidacion: Si n no es un entero positivo, si valor no es un
            número real finito, si valor es negativo y n es par o si el
            resultado no es finito.
    """
    if type(n) is not int or n <= 0:
        raise ErrorValidacion("n debe ser un entero positivo")

    _validar_real_finito(valor, "El valor")

    try:
        if valor < 0:
            if n % 2 == 0:
                raise ErrorValidacion(
                    "No existe raíz par real de un número negativo"
                )
            resultado = -float((-valor) ** (1 / n))
        else:
            resultado = float(valor ** (1 / n))
    except OverflowError as error:
        raise ErrorValidacion(_MENSAJE_RESULTADO) from error

    return _resultado_finito(resultado)


def raiz_cuadrada(valor: int | float) -> float:
    """
    Calcula la raíz cuadrada.

    Fórmula:
        sqrt(valor)

    Raises:
        ErrorValidacion: Si valor no es un número real finito, si es
            negativo o si el resultado no es finito.
    """
    _validar_real_finito(valor, "El valor")

    if valor < 0:
        raise ErrorValidacion(
            "No se puede calcular la raíz cuadrada de un número negativo"
        )

    try:
        resultado = float(math.sqrt(valor))
    except OverflowError as error:
        raise ErrorValidacion(_MENSAJE_RESULTADO) from error

    return _resultado_finito(resultado)


def logaritmo_natural(valor: int | float) -> float:
    """
    Calcula el logaritmo natural.

    Fórmula:
        ln(valor)

    Raises:
        ErrorValidacion: Si valor no es un número real finito o no es
            mayor que 0.
    """
    _validar_real_finito(valor, "El valor")

    if valor <= 0:
        raise ErrorValidacion(
            "El valor debe ser mayor que 0"
        )

    return float(math.log(valor))


def logaritmo_base10(valor: int | float) -> float:
    """
    Calcula el logaritmo en base 10.

    Fórmula:
        log10(valor)

    Raises:
        ErrorValidacion: Si valor no es un número real finito o no es
            mayor que 0.
    """
    _validar_real_finito(valor, "El valor")

    if valor <= 0:
        raise ErrorValidacion(
            "El valor debe ser mayor que 0"
        )

    return float(math.log10(valor))


def logaritmo_base(valor: int | float, base: int | float) -> float:
    """
    Calcula el logaritmo en una base arbitraria.

    Fórmula:
        log(valor, base)

    Raises:
        ErrorValidacion: Si valor o base no son números reales finitos, si
            valor no es mayor que 0 o si la base no es positiva y distinta
            de 1.
    """
    _validar_real_finito(valor, "El valor")
    _validar_real_finito(base, "La base")

    if valor <= 0:
        raise ErrorValidacion(
            "El valor debe ser mayor que 0"
        )

    if base <= 0 or base == 1:
        raise ErrorValidacion(
            "La base debe ser positiva y distinta de 1"
        )

    return float(math.log(valor, base))
