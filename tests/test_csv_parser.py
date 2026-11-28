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


@pytest.fixture
def csv_valido(tmp_path):
    ruta = tmp_path / "valido.csv"
    ruta.write_text("a,b\n1,2\n", encoding="utf-8")
    return ruta


@pytest.mark.parametrize("ruta", [123, None])
def test_parse_csv_ruta_de_tipo_invalido_lanza_type_error(ruta):
    mensaje = "^file_path debe ser una ruta de archivo$"
    with pytest.raises(TypeError, match=mensaje):
        parse_csv(ruta)


@pytest.mark.parametrize("valor", [1, "si", None])
def test_parse_csv_has_header_de_tipo_invalido_lanza_type_error(csv_valido, valor):
    mensaje = "^has_header debe ser un valor booleano$"
    with pytest.raises(TypeError, match=mensaje):
        parse_csv(csv_valido, has_header=valor)


@pytest.mark.parametrize("valor", [1, None])
def test_parse_csv_delimiter_de_tipo_invalido_lanza_type_error(csv_valido, valor):
    with pytest.raises(TypeError, match="^delimiter debe ser texto$"):
        parse_csv(csv_valido, delimiter=valor)


@pytest.mark.parametrize("valor", [1, None])
def test_parse_csv_encoding_de_tipo_invalido_lanza_type_error(csv_valido, valor):
    with pytest.raises(TypeError, match="^encoding debe ser texto$"):
        parse_csv(csv_valido, encoding=valor)


@pytest.mark.parametrize(
    "delimitador",
    ["", ",,", "\n", "\r", "\0"],
    ids=[
        "vacio",
        "dos_caracteres",
        "salto_de_linea",
        "retorno_de_carro",
        "nul",
    ],
)
def test_parse_csv_delimitador_prohibido_lanza_value_error(csv_valido, delimitador):
    mensaje = "^delimiter debe tener un carácter distinto de un salto de línea o NUL$"
    with pytest.raises(ValueError, match=mensaje):
        parse_csv(csv_valido, delimiter=delimitador)


@pytest.mark.parametrize("has_header", [True, False])
@pytest.mark.parametrize(
    ("contenido", "fila"),
    [
        (b'a,b\n"1,2\n', 2),
        (b'a,b\n1,2\n"3,4\n', 3),
        (b'a,b\n"1"x,2\n', 2),
    ],
    ids=[
        "comilla_sin_cerrar_fila_2",
        "comilla_sin_cerrar_fila_3",
        "texto_tras_comilla_fila_2",
    ],
)
def test_parse_csv_malformado_informa_fila(tmp_path, contenido, fila, has_header):
    ruta = tmp_path / "malformado.csv"
    ruta.write_bytes(contenido)

    with pytest.raises(ValueError, match=rf"^Fila {fila}: CSV inválido: "):
        parse_csv(ruta, has_header=has_header)
