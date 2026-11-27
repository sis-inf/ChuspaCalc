import pytest

from chuspacalc.modulos.matematicas.error_validacion import (
    ErrorValidacion,
    validar_no_cero,
    validar_numero,
    validar_rango,
)


def test_error_validacion_es_subclase_de_value_error() -> None:
    assert issubclass(ErrorValidacion, ValueError)


def test_error_validacion_se_captura_con_except_value_error() -> None:
    try:
        raise ErrorValidacion("mensaje")
    except ValueError as error:
        assert isinstance(error, ErrorValidacion)
    else:
        assert False, "La excepción debía ser capturada"


def test_error_validacion_conserva_el_mensaje() -> None:
    error = ErrorValidacion("mensaje")

    assert str(error) == "mensaje"


# --- validar_numero ---


@pytest.mark.parametrize("valor", [5, 2.5, -3, 0, 0.0, 1e300])
def test_validar_numero_acepta_numeros_finitos(valor: float) -> None:
    resultado = validar_numero(valor, "x")

    assert isinstance(resultado, float)
    assert resultado == float(valor)


@pytest.mark.parametrize("valor", [True, False, "5", None, [1], (1,), 1 + 2j])
def test_validar_numero_rechaza_tipos_no_numericos(valor: object) -> None:
    with pytest.raises(ErrorValidacion, match="'masa'.*número entero o decimal"):
        validar_numero(valor, "masa")


@pytest.mark.parametrize("valor", [float("nan"), float("inf"), float("-inf")])
def test_validar_numero_rechaza_nan_e_infinitos(valor: float) -> None:
    with pytest.raises(ErrorValidacion, match="'x'.*finito"):
        validar_numero(valor, "x")


def test_validar_numero_rechaza_entero_fuera_de_rango_de_float() -> None:
    with pytest.raises(ErrorValidacion, match="fuera del rango"):
        validar_numero(10**400, "x")


def test_validar_numero_el_error_es_value_error() -> None:
    with pytest.raises(ValueError):
        validar_numero("abc", "x")


# --- validar_no_cero ---


@pytest.mark.parametrize("valor", [4, -2.5, 1e-300])
def test_validar_no_cero_acepta_valores_distintos_de_cero(valor: float) -> None:
    assert validar_no_cero(valor, "divisor") == float(valor)


@pytest.mark.parametrize("valor", [0, 0.0, -0.0])
def test_validar_no_cero_rechaza_cero(valor: float) -> None:
    with pytest.raises(ErrorValidacion, match="'divisor'.*cero"):
        validar_no_cero(valor, "divisor")


@pytest.mark.parametrize("valor", [float("nan"), float("inf"), "1", None, True])
def test_validar_no_cero_rechaza_valores_invalidos(valor: object) -> None:
    with pytest.raises(ErrorValidacion):
        validar_no_cero(valor, "divisor")


# --- validar_rango ---


def test_validar_rango_acepta_valor_dentro_del_rango() -> None:
    assert validar_rango(5, "x", minimo=0, maximo=10) == 5.0


def test_validar_rango_limites_son_inclusivos() -> None:
    assert validar_rango(0, "x", minimo=0, maximo=10) == 0.0
    assert validar_rango(10, "x", minimo=0, maximo=10) == 10.0


def test_validar_rango_sin_limites_solo_valida_el_numero() -> None:
    assert validar_rango(-1e9, "x") == -1e9


def test_validar_rango_solo_minimo() -> None:
    assert validar_rango(1, "x", minimo=0) == 1.0
    with pytest.raises(ErrorValidacion, match="menor que"):
        validar_rango(-1, "x", minimo=0)


def test_validar_rango_solo_maximo() -> None:
    assert validar_rango(1, "x", maximo=2) == 1.0
    with pytest.raises(ErrorValidacion, match="mayor que"):
        validar_rango(3, "x", maximo=2)


def test_validar_rango_rechaza_valor_bajo_el_minimo() -> None:
    with pytest.raises(ErrorValidacion, match="'temperatura'.*menor que -273.15"):
        validar_rango(-300, "temperatura", minimo=-273.15)


def test_validar_rango_rechaza_valor_sobre_el_maximo() -> None:
    with pytest.raises(ErrorValidacion, match="'x'.*mayor que 10"):
        validar_rango(11, "x", minimo=0, maximo=10)


def test_validar_rango_rechaza_limites_invertidos() -> None:
    with pytest.raises(ErrorValidacion, match="Rango inválido"):
        validar_rango(5, "x", minimo=10, maximo=0)


@pytest.mark.parametrize("valor", [float("nan"), float("inf"), "5", True, None])
def test_validar_rango_rechaza_valores_invalidos(valor: object) -> None:
    with pytest.raises(ErrorValidacion):
        validar_rango(valor, "x", minimo=0, maximo=10)
