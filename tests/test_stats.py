import math

import pytest

from escuadra.math.stats import (
    calcular_desviacion_estandar,
    calcular_media,
    calcular_mediana,
)


def test_calcular_media():
    numeros = [1, 2, 3, 4, 5]

    assert calcular_media(numeros) == 3.0


def test_calcular_mediana():
    numeros = [1, 2, 3, 4, 5]

    assert calcular_mediana(numeros) == 3.0


def test_calcular_desviacion_estandar():
    numeros = [1, 2, 3, 4, 5]

    assert math.isclose(
        calcular_desviacion_estandar(numeros),
        1.5811388300841898,
        rel_tol=1e-9,
    )


def test_calcular_media_lista_vacia():
    with pytest.raises(ValueError):
        calcular_media([])


def test_calcular_mediana_lista_vacia():
    with pytest.raises(ValueError):
        calcular_mediana([])


def test_calcular_desviacion_estandar_lista_vacia():
    with pytest.raises(ValueError):
        calcular_desviacion_estandar([])
