import pytest

from escuadra.modulos.civil.carga_distribuida import calcular_reacciones_carga_parcial


def test_carga_en_toda_la_viga_reparte_las_reacciones_por_igual():
    resultado = calcular_reacciones_carga_parcial(
        longitud_viga=10,
        carga_por_metro=2,
        inicio_carga=0,
        fin_carga=10,
    )

    assert resultado == pytest.approx(
        {
            "reaccion_izquierda": 10.0,
            "reaccion_derecha": 10.0,
            "resultante": 20.0,
            "posicion_resultante": 5.0,
        }
    )


def test_carga_entre_dos_y_seis_metros_da_reacciones_de_doce_y_ocho():
    resultado = calcular_reacciones_carga_parcial(
        longitud_viga=10,
        carga_por_metro=5,
        inicio_carga=2,
        fin_carga=6,
    )

    assert resultado == pytest.approx(
        {
            "reaccion_izquierda": 12.0,
            "reaccion_derecha": 8.0,
            "resultante": 20.0,
            "posicion_resultante": 4.0,
        }
    )


@pytest.mark.parametrize("longitud_viga", [0, -10])
def test_longitud_viga_no_positiva_lanza_value_error(longitud_viga):
    with pytest.raises(ValueError, match="La longitud de la viga debe ser positiva"):
        calcular_reacciones_carga_parcial(longitud_viga, 2, 0, 10)


@pytest.mark.parametrize("carga_por_metro", [0, -2])
def test_carga_por_metro_no_positiva_lanza_value_error(carga_por_metro):
    with pytest.raises(ValueError, match="La carga por metro debe ser positiva"):
        calcular_reacciones_carga_parcial(10, carga_por_metro, 0, 10)


def test_inicio_carga_negativo_lanza_value_error():
    with pytest.raises(ValueError, match="inicio_carga no puede ser negativo"):
        calcular_reacciones_carga_parcial(10, 2, -1, 6)


@pytest.mark.parametrize("inicio_carga, fin_carga", [(4, 4), (6, 2)])
def test_inicio_carga_igual_o_mayor_al_fin_lanza_value_error(inicio_carga, fin_carga):
    with pytest.raises(ValueError, match="inicio_carga debe ser menor que fin_carga"):
        calcular_reacciones_carga_parcial(10, 2, inicio_carga, fin_carga)


def test_fin_carga_fuera_de_la_viga_lanza_value_error():
    mensaje = "fin_carga no puede superar la longitud de la viga"
    with pytest.raises(ValueError, match=mensaje):
        calcular_reacciones_carga_parcial(10, 2, 0, 11)
