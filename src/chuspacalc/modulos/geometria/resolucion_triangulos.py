"""
Resolución de triángulos mediante ley de senos y cosenos.
"""

import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_numero(nombre: str, valor: float) -> None:
    """Exige un número real finito representable como flotante."""
    try:
        if isinstance(valor, (int, float)) and not isinstance(valor, bool):
            if math.isfinite(valor):
                return
    except OverflowError:
        raise ErrorValidacion(f"{nombre} excede el rango numérico") from None
    raise ErrorValidacion(f"{nombre} debe ser un número real finito")


def _angulo_opuesto(a: float, b: float, c: float) -> float:
    """Calcula un ángulo mediante la fórmula del semiángulo."""
    menor, mayor = sorted((b, c))
    diferencia = mayor - menor
    seno = math.sqrt(a - diferencia) * math.sqrt(a + diferencia)
    coseno = math.sqrt(menor + (mayor - a)) * math.sqrt(a + b + c)
    return math.degrees(2 * math.atan2(seno, coseno))


def resolver_triangulo_lados(
    a: float, b: float, c: float
) -> tuple[float, float, float]:
    """Devuelve los ángulos en grados, en el orden de sus lados opuestos."""
    _validar_numero("a", a)
    _validar_numero("b", b)
    _validar_numero("c", c)
    menor, medio, mayor = sorted((a, b, c))

    if menor <= 0:
        raise ErrorValidacion("Los lados deben ser mayores a cero")

    if menor <= mayor - medio:
        raise ErrorValidacion("Los lados no forman un triángulo válido")

    _, exponente = math.frexp(mayor)
    a = math.ldexp(a, -exponente)
    b = math.ldexp(b, -exponente)
    c = math.ldexp(c, -exponente)
    angulos = (
        _angulo_opuesto(a, b, c),
        _angulo_opuesto(b, a, c),
        _angulo_opuesto(c, a, b),
    )
    if not all(0 < angulo < 180 for angulo in angulos):
        raise ErrorValidacion("Los ángulos exceden la precisión numérica disponible")
    return angulos


def resolver_triangulo_lado_angulo(
    a: float,
    angulo_a: float,
    angulo_b: float,
) -> tuple[float, float, float]:
    """Devuelve los lados b y c y el ángulo C en grados mediante la ley de senos."""
    _validar_numero("a", a)
    _validar_numero("angulo_a", angulo_a)
    _validar_numero("angulo_b", angulo_b)

    if a <= 0:
        raise ErrorValidacion("El lado debe ser mayor a cero")

    if not 0 < angulo_a < 180 or not 0 < angulo_b < 180:
        raise ErrorValidacion("Cada ángulo debe estar entre 0 y 180 grados")

    angulo_c = math.fsum((180.0, -angulo_a, -angulo_b))
    if angulo_c <= 0:
        raise ErrorValidacion("La suma de ángulos es inválida")

    seno_a = math.sin(math.radians(angulo_a))
    if seno_a == 0:
        raise ErrorValidacion("El ángulo A es demasiado pequeño para calcular su seno")
    b = a * (math.sin(math.radians(angulo_b)) / seno_a)
    c = a * (math.sin(math.radians(angulo_c)) / seno_a)
    if not (0 < b < math.inf and 0 < c < math.inf):
        raise ErrorValidacion("Los lados calculados exceden el rango numérico")

    return b, c, angulo_c
