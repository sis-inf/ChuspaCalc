"""
Tests unitarios para las funciones del módulo estadisticas, verificando
media, mediana, moda y desviación estándar, así como el manejo de listas
vacías y de datos insuficientes.
"""

import pytest

from chuspacalc.modulos.matematicas.estadisticas import (
    calcular_desviacion_estandar,
    calcular_media,
    calcular_mediana,
    calcular_moda,
)


def test_calcular_media():
    assert calcular_media([1, 2, 3, 4]) == 2.5


def test_calcular_mediana_cantidad_impar():
    assert calcular_mediana([3, 1, 2]) == 2.0


def test_calcular_mediana_cantidad_par_promedia_los_dos_centrales():
    assert calcular_mediana([4, 1, 3, 2]) == 2.5


def test_calcular_moda_devuelve_todos_los_valores_mas_frecuentes():
    assert calcular_moda([1, 2, 2, 3, 3]) == [2, 3]


def test_calcular_desviacion_estandar_poblacional():
    datos = [2, 4, 4, 4, 5, 5, 7, 9]
    assert calcular_desviacion_estandar(datos, poblacional=True) == 2.0


def test_calcular_desviacion_estandar_muestral_con_un_solo_dato_lanza_error():
    with pytest.raises(ValueError):
        calcular_desviacion_estandar([5])


def test_calcular_media_con_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        calcular_media([])


def test_calcular_mediana_con_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        calcular_mediana([])


def test_calcular_moda_con_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        calcular_moda([])


def test_calcular_desviacion_estandar_con_lista_vacia_lanza_error():
    with pytest.raises(ValueError):
        calcular_desviacion_estandar([])


@pytest.mark.parametrize(
    "funcion",
    [
        calcular_media,
        calcular_mediana,
        calcular_moda,
        calcular_desviacion_estandar,
    ],
)
@pytest.mark.parametrize(
    "datos",
    [
        [1, 2, float("nan")],
        [1, 2, float("inf")],
        [1, 2, float("-inf")],
        [1, 2, "hola"],
    ],
)
def test_funciones_estadisticas_rechazan_datos_invalidos(funcion, datos):
    with pytest.raises(ValueError):
        funcion(datos)


def test_calcular_moda_acepta_enteros_grandes():
    numero_grande = 10**400

    resultado = calcular_moda([numero_grande, numero_grande, 2])

    assert resultado == [numero_grande]


def test_calcular_desviacion_estandar_muestral():
    datos = [1, 2, 3]

    resultado = calcular_desviacion_estandar(datos, poblacional=False)

    assert resultado == pytest.approx(1.0)
