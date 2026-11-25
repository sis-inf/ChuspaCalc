import pytest

from chuspacalc.modulos.geometria.calculo_area import area_trapecio


def test_area_trapecio_aplica_formula() -> None:
    assert area_trapecio(8, 4, 3) == pytest.approx(18.0)


@pytest.mark.parametrize(
    ("base_mayor", "base_menor", "altura"),
    [(0, 1, 1), (1, 0, 1), (1, 1, 0), (-1, 1, 1), (True, 1, 1)],
)
def test_area_trapecio_rechaza_dimensiones_invalidas(
    base_mayor, base_menor, altura
) -> None:
    with pytest.raises(ValueError):
        area_trapecio(base_mayor, base_menor, altura)
