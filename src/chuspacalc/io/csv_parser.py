import csv
from os import PathLike, fspath

RutaCSV = str | bytes | PathLike[str] | PathLike[bytes]


def _validar_encabezados(headers: list[str]) -> None:
    """Rechaza encabezados vacíos o duplicados."""
    vistos = set()
    for posicion, nombre in enumerate(headers, start=1):
        if not nombre.strip():
            mensaje = f"Fila 1: el encabezado de la columna {posicion} está vacío"
            raise ValueError(mensaje)
        if nombre in vistos:
            raise ValueError(f"Fila 1: el encabezado '{nombre}' está duplicado")
        vistos.add(nombre)


def _leer_csv(
    ruta: str | bytes, has_header: bool, delimiter: str, encoding: str
) -> list[dict[str, str]] | list[list[str]]:
    """Lee los registros y valida su ancho cuando hay encabezados."""
    with open(ruta, newline="", encoding=encoding) as archivo:
        reader = csv.reader(archivo, delimiter=delimiter, strict=True)
        try:
            if not has_header:
                return list(reader)
            headers = next(reader, None)
            if not headers:
                raise ValueError("El archivo CSV está vacío")
            _validar_encabezados(headers)
            registros = []
            for fila in reader:
                if not fila:
                    continue
                if len(fila) != len(headers):
                    raise ValueError(
                        f"Fila {reader.line_num}: se esperaban {len(headers)} campos "
                        f"y se encontraron {len(fila)}"
                    )
                registros.append(dict(zip(headers, fila)))
            return registros
        except csv.Error as error:
            raise ValueError(
                f"Fila {reader.line_num}: CSV inválido: {error}"
            ) from error


def parse_csv(
    file_path: RutaCSV,
    has_header: bool = True,
    delimiter: str = ",",
    encoding: str = "utf-8",
) -> list[dict[str, str]] | list[list[str]]:
    """Lee registros CSV como diccionarios con encabezados o como filas de texto.

    Sin encabezados se admiten filas de longitud variable. Si falla la
    decodificación con la codificación solicitada, se reintenta con Latin-1.

    Raises:
        TypeError: Si la ruta o las opciones tienen un tipo incorrecto.
        ValueError: Si una opción o la estructura del archivo es inválida.
        LookupError: Si la codificación no existe.
        FileNotFoundError: Si la ruta no existe.
    """
    try:
        ruta = fspath(file_path)
    except TypeError as error:
        raise TypeError("file_path debe ser una ruta de archivo") from error
    if not isinstance(has_header, bool):
        raise TypeError("has_header debe ser un valor booleano")
    if not isinstance(delimiter, str):
        raise TypeError("delimiter debe ser texto")
    if len(delimiter) != 1 or delimiter in "\r\n\0":
        raise ValueError(
            "delimiter debe tener un carácter distinto de un salto de línea o NUL"
        )
    if not isinstance(encoding, str):
        raise TypeError("encoding debe ser texto")
    if not ruta or not encoding.strip():
        raise ValueError("La ruta y la codificación no pueden estar vacías")

    try:
        try:
            return _leer_csv(ruta, has_header, delimiter, encoding)
        except UnicodeDecodeError:
            return _leer_csv(ruta, has_header, delimiter, "latin-1")
    except FileNotFoundError as error:
        raise FileNotFoundError(
            error.errno, "No se encuentra el archivo", error.filename
        ) from error
