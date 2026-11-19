import pytest

from chuspacalc.io.csv_parser import parse_csv


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


def test_parse_csv_fila_corta_lanza_value_error_con_numero_de_fila(tmp_path):
    ruta = tmp_path / "fila_corta.csv"
    ruta.write_text("a,b,c\n1,2,3\n4,5\n", encoding="utf-8")

    mensaje = "^Fila 3: se esperaban 3 campos y se encontraron 2$"
    with pytest.raises(ValueError, match=mensaje):
        parse_csv(ruta)


def test_parse_csv_fila_larga_lanza_value_error_con_numero_de_fila(tmp_path):
    ruta = tmp_path / "fila_larga.csv"
    ruta.write_text("a,b\n1,2,3\n", encoding="utf-8")

    mensaje = "^Fila 2: se esperaban 2 campos y se encontraron 3$"
    with pytest.raises(ValueError, match=mensaje):
        parse_csv(ruta)


def test_parse_csv_encabezado_duplicado_lanza_value_error(tmp_path):
    ruta = tmp_path / "duplicado.csv"
    ruta.write_text("a,a\n1,2\n", encoding="utf-8")

    with pytest.raises(ValueError, match="^Fila 1: el encabezado 'a' está duplicado$"):
        parse_csv(ruta)


def test_parse_csv_encabezado_vacio_lanza_value_error(tmp_path):
    ruta = tmp_path / "vacio_encabezado.csv"
    ruta.write_text("a,,c\n1,2,3\n", encoding="utf-8")

    mensaje = "^Fila 1: el encabezado de la columna 2 está vacío$"
    with pytest.raises(ValueError, match=mensaje):
        parse_csv(ruta)


def test_parse_csv_ignora_lineas_vacias(tmp_path):
    ruta = tmp_path / "lineas_vacias.csv"
    ruta.write_text("a,b\n1,2\n\n3,4\n\n", encoding="utf-8")

    resultado = parse_csv(ruta)

    assert resultado == [{"a": "1", "b": "2"}, {"a": "3", "b": "4"}]


def test_parse_csv_sin_encabezados_no_valida_cantidad_de_campos(tmp_path):
    ruta = tmp_path / "sin_encabezados_irregular.csv"
    ruta.write_text("1,2\n3\n", encoding="utf-8")

    resultado = parse_csv(ruta, has_header=False)

    assert resultado == [["1", "2"], ["3"]]
