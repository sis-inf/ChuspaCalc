import math
from numbers import Real

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_numero(valor: object, nombre: str) -> float:
    """Verifica que el valor sea un número real y lo devuelve como float.

    Args:
        valor: Dato a validar.
        nombre: Nombre del parámetro para el mensaje de error.

    Returns:
        El valor convertido a ``float``.

    Raises:
        ErrorValidacion: Si no es numérico (incluye ``bool``) o es demasiado
            grande para convertirse a ``float``.
    """
    if isinstance(valor, bool) or not isinstance(valor, Real):
        raise ErrorValidacion(f"{nombre} debe ser un número")
    try:
        return float(valor)
    except OverflowError:
        raise ErrorValidacion(f"{nombre} es demasiado grande") from None


def calcular_carga_critica_euler(
    modulo_elasticidad: float,
    momento_inercia: float,
    longitud: float,
    condicion_apoyo: str = "biarticulada",
) -> float:
    """
    Calcula la carga crítica de pandeo de Euler para columnas a compresión.

    Fórmula:
        P_cr = π² · E · I / (K · L)²

    Unidades:
        - E: módulo de elasticidad en Pascales (Pa) o MPa
        - I: momento de inercia en m⁴
        - L: longitud de la columna en metros (m)
        - P_cr: carga crítica en Newtons (N)

    Factores de longitud efectiva (K):
        - biarticulada: K = 1.0
        - empotrada-libre: K = 2.0
        - empotrada-empotrada: K = 0.5
        - empotrada-articulada: K = 0.7

    Args:
        modulo_elasticidad: Módulo de elasticidad del material (Pa)
        momento_inercia: Momento de inercia de la sección (m⁴)
        longitud: Longitud de la columna (m)
        condicion_apoyo: Tipo de condición de apoyo (default: 'biarticulada')

    Returns:
        Carga crítica de pandeo en Newtons (N)

    Raises:
        ErrorValidacion: Si los parámetros no son válidos o la condición de
            apoyo no existe
    """
    modulo_elasticidad = _validar_numero(modulo_elasticidad, "modulo_elasticidad")
    momento_inercia = _validar_numero(momento_inercia, "momento_inercia")
    longitud = _validar_numero(longitud, "longitud")

    for nombre, valor in (
        ("modulo_elasticidad", modulo_elasticidad),
        ("momento_inercia", momento_inercia),
        ("longitud", longitud),
    ):
        if not math.isfinite(valor):
            raise ErrorValidacion(f"{nombre} debe ser un número finito")

    if modulo_elasticidad <= 0:
        raise ErrorValidacion("modulo_elasticidad debe ser mayor que 0")

    if momento_inercia <= 0:
        raise ErrorValidacion("momento_inercia debe ser mayor que 0")

    if longitud <= 0:
        raise ErrorValidacion("longitud debe ser mayor que 0")

    # Definir factores K según condición de apoyo
    factores_k = {
        "biarticulada": 1.0,
        "empotrada-libre": 2.0,
        "empotrada-empotrada": 0.5,
        "empotrada-articulada": 0.7,
    }

    if condicion_apoyo not in factores_k:
        raise ErrorValidacion(
            f"condicion_apoyo debe ser una de: {list(factores_k.keys())}. "
            f"Valor recibido: {condicion_apoyo}"
        )

    K = factores_k[condicion_apoyo]

    # Calcular carga crítica de Euler
    # P_cr = π² · E · I / (K · L)²
    pi_cuadrado = math.pi**2
    longitud_efectiva = K * longitud
    carga_critica = (pi_cuadrado * modulo_elasticidad * momento_inercia) / (
        longitud_efectiva**2
    )

    return float(carga_critica)
