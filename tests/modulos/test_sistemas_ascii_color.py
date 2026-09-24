from escuadra.modulos.sistemas.conversor_color import (
    hex_a_rgb,
    rgb_a_hex,
    rgb_a_hsl,
)
from escuadra.modulos.sistemas.tabla_ascii import listar_ascii_rango


def test_generacion_tabla_ascii_rango():
    tabla = listar_ascii_rango(65, 67)

    assert len(tabla) == 3

    assert tabla[0]["caracter"] == "A"
    assert tabla[0]["decimal"] == 65
    assert tabla[0]["hexadecimal"] == "0x41"
    assert tabla[0]["octal"] == "0o101"
    assert tabla[0]["binario"] == "0b1000001"

    assert tabla[1]["caracter"] == "B"
    assert tabla[2]["caracter"] == "C"


def test_conversion_color_rojo():
    assert rgb_a_hex(255, 0, 0) == "#FF0000"
    assert hex_a_rgb("#FF0000") == (255, 0, 0)
    assert rgb_a_hsl(255, 0, 0) == (0, 100, 50)


def test_conversion_color_blanco():
    assert rgb_a_hex(255, 255, 255) == "#FFFFFF"
    assert hex_a_rgb("#FFFFFF") == (255, 255, 255)
    assert rgb_a_hsl(255, 255, 255) == (0, 0, 100)


def test_conversion_color_negro():
    assert rgb_a_hex(0, 0, 0) == "#000000"
    assert hex_a_rgb("#000000") == (0, 0, 0)
    assert rgb_a_hsl(0, 0, 0) == (0, 0, 0)
