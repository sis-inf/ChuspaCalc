import pytest

from escuadra.io.csv_parser import parse_csv


def test_parse_csv_con_encabezados_devuelve_diccionarios(tmp_path):
    ruta = tmp_path / "datos.csv"
    ruta.write_text("a,b\n1,2\n3,4\n", encoding="utf-8")

    resultado = parse_csv(ruta)

    assert resultado == [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]


def test_parse_csv_sin_encabezados_incluye_la_primera_fila(tmp_path):
    ruta = tmp_path / "sin_encabezados.csv"
    ruta.write_text("a,b\n1,2\n3,4\n", encoding="utf-8")

    resultado = parse_csv(ruta, has_header=False)

    assert resultado == [["a", "b"], ["1", "2"], ["3", "4"]]


def test_parse_csv_admite_separador_punto_y_coma(tmp_path):
    ruta = tmp_path / "separador.csv"
    ruta.write_text("a;b\n1;2\n3;4\n", encoding="utf-8")

    resultado = parse_csv(ruta, delimiter=";")

    assert resultado == [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]


def test_parse_csv_vacio_con_encabezados_lanza_value_error(tmp_path):
    ruta = tmp_path / "vacio.csv"
    ruta.write_text("", encoding="utf-8")

    with pytest.raises(ValueError, match="^El archivo CSV está vacío$"):
        parse_csv(ruta)


def test_parse_csv_ruta_inexistente_lanza_file_not_found_error(tmp_path):
    ruta = tmp_path / "inexistente.csv"

    with pytest.raises(FileNotFoundError):
        parse_csv(ruta)


def test_parse_csv_lee_enie_en_archivo_latin_1(tmp_path):
    ruta = tmp_path / "latin_1.csv"
    ruta.write_bytes("nombre\nPeña\n".encode("latin-1"))

    resultado = parse_csv(ruta)

    assert resultado == [{"nombre": "Peña"}]
