"""
Pruebas unitarias para el enum Carrera.
"""

from chuspacalc.core.carrera import Carrera


def test_carrera_civil_tiene_codigo_y_etiqueta_correctos():
    """Verifica el código y la etiqueta de Ingeniería Civil."""
    assert Carrera.CIVIL.codigo == "civil"
    assert Carrera.CIVIL.etiqueta == "Ingeniería Civil"


def test_carrera_enum_tiene_exactamente_cinco_miembros():
    """Verifica que Carrera contenga exactamente cinco miembros."""
    miembros_esperados = {
        "SISTEMAS",
        "MATEMATICAS",
        "ELECTRICA",
        "CIVIL",
        "GEOMETRIA",
    }

    miembros_actuales = {carrera.name for carrera in Carrera}

    assert len(Carrera) == 5
    assert miembros_actuales == miembros_esperados


def test_codigos_de_carrera_son_unicos():
    """Verifica que ninguna carrera tenga un código repetido."""
    codigos = [carrera.codigo for carrera in Carrera]

    assert len(codigos) == len(set(codigos))


def test_carrera_sistemas_tiene_codigo_correcto():
    """Verifica que SISTEMAS tenga el código esperado."""
    assert Carrera.SISTEMAS.codigo == "sistemas"
