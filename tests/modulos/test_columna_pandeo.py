import pytest

from escuadra.modulos.civil.columna_pandeo import calcular_carga_critica_euler


@pytest.mark.parametrize(
    "condicion_apoyo, esperado",
    [
        ("biarticulada", 1754596.3379714415),
        ("empotrada-libre", 438649.0844928604),
        ("empotrada-empotrada", 7018385.351885766),
        ("empotrada-articulada", 3580808.853002942),
    ],
)
def test_carga_critica_segun_condicion_de_apoyo(condicion_apoyo, esperado):
    resultado = calcular_carga_critica_euler(
        modulo_elasticidad=200e9,
        momento_inercia=8e-6,
        longitud=3,
        condicion_apoyo=condicion_apoyo,
    )

    assert resultado == pytest.approx(esperado, rel=1e-9)


def test_apoyo_predeterminado_corresponde_a_columna_biarticulada():
    resultado = calcular_carga_critica_euler(200e9, 8e-6, 3)

    assert resultado == pytest.approx(1754596.3379714415, rel=1e-9)


@pytest.mark.parametrize("modulo_elasticidad", [0, -200e9])
def test_modulo_elasticidad_no_positivo_lanza_value_error(modulo_elasticidad):
    with pytest.raises(ValueError, match="modulo_elasticidad debe ser mayor que 0"):
        calcular_carga_critica_euler(modulo_elasticidad, 8e-6, 3)


@pytest.mark.parametrize("momento_inercia", [0, -8e-6])
def test_momento_inercia_no_positivo_lanza_value_error(momento_inercia):
    with pytest.raises(ValueError, match="momento_inercia debe ser mayor que 0"):
        calcular_carga_critica_euler(200e9, momento_inercia, 3)


@pytest.mark.parametrize("longitud", [0, -3])
def test_longitud_no_positiva_lanza_value_error(longitud):
    with pytest.raises(ValueError, match="longitud debe ser mayor que 0"):
        calcular_carga_critica_euler(200e9, 8e-6, longitud)


def test_condicion_apoyo_desconocida_lanza_value_error():
    with pytest.raises(ValueError, match="condicion_apoyo debe ser una de"):
        calcular_carga_critica_euler(200e9, 8e-6, 3, condicion_apoyo="desconocida")
