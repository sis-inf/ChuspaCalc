import math

import pytest
from chuspacalc.modulos.estadistica.amplitud_intervalo import (
    calcular_amplitud_intervalo,
)
from chuspacalc.modulos.estadistica.frecuencia_relativa import (
    calcular_frecuencia_relativa,
)
from chuspacalc.modulos.estadistica.puntuacion_z import calcular_puntuacion_z
from chuspacalc.modulos.fisica.aceleracion_centripeta import (
    calcular_aceleracion_centripeta,
)
from chuspacalc.modulos.fisica.impulso import calcular_impulso
from chuspacalc.modulos.fisica.velocidad_angular import calcular_velocidad_angular
from chuspacalc.modulos.quimica.formula_empirica import calcular_formula_empirica
from chuspacalc.modulos.quimica.fraccion_molar import calcular_fraccion_molar
from chuspacalc.modulos.quimica.reactivo_limitante import (
    identificar_reactivo_limitante,
)
from chuspacalc.modulos.quimica.vida_media import calcular_cantidad_restante


@pytest.mark.parametrize(
    ("calculo", "esperado"),
    [
        (lambda: calcular_puntuacion_z(12, 10, 2), 1.0),
        (lambda: calcular_frecuencia_relativa([1, 1, 2], 1), 2 / 3),
        (lambda: calcular_amplitud_intervalo(0, 10, 5), 2.0),
        (lambda: calcular_aceleracion_centripeta(10, 5), 20.0),
        (lambda: calcular_impulso(4, 3), 12.0),
        (lambda: calcular_velocidad_angular(math.pi, 2), math.pi / 2),
        (lambda: calcular_fraccion_molar(2, 5), 0.4),
        (lambda: calcular_cantidad_restante(100, 20, 10), 25.0),
    ],
)
def test_modulos_estudiantiles_conservan_resultados(calculo, esperado) -> None:
    assert calculo() == pytest.approx(esperado)


def test_formula_empirica_conserva_proporcion_entera() -> None:
    assert calcular_formula_empirica([1, 2, 1]) == [1, 2, 1]


def test_reactivo_limitante_devuelve_indice_original() -> None:
    assert identificar_reactivo_limitante([4, 9], [2, 3]) == 0


@pytest.mark.parametrize(
    "calculo",
    [
        lambda: calcular_puntuacion_z(1, 0, 0),
        lambda: calcular_frecuencia_relativa([], 1),
        lambda: calcular_amplitud_intervalo(10, 0, 5),
        lambda: calcular_aceleracion_centripeta(1, 0),
        lambda: calcular_impulso(1, -1),
        lambda: calcular_velocidad_angular(1, 0),
        lambda: calcular_formula_empirica([]),
        lambda: calcular_fraccion_molar(2, 1),
        lambda: identificar_reactivo_limitante([1], []),
        lambda: calcular_cantidad_restante(1, 1, 0),
    ],
)
def test_modulos_estudiantiles_conservan_validaciones(calculo) -> None:
    with pytest.raises((TypeError, ValueError)):
        calculo()


@pytest.mark.parametrize(
    "ruta",
    [
        "estadistica.amplitud_intervalo",
        "estadistica.frecuencia_relativa",
        "estadistica.puntuacion_z",
        "fisica.aceleracion_centripeta",
        "fisica.impulso",
        "fisica.velocidad_angular",
        "quimica.formula_empirica",
        "quimica.fraccion_molar",
        "quimica.reactivo_limitante",
        "quimica.vida_media",
    ],
)
def test_namespace_escuadra_comparte_modulo_canonico(ruta) -> None:
    import importlib

    canonico = importlib.import_module(f"chuspacalc.modulos.{ruta}")
    heredado = importlib.import_module(f"escuadra.modulos.{ruta}")

    assert heredado is canonico
