import csv


def _validar_encabezados(headers):
    """Rechaza encabezados vacíos o duplicados."""
    vistos = set()
    for posicion, nombre in enumerate(headers, start=1):
        if not nombre.strip():
            mensaje = f"Fila 1: el encabezado de la columna {posicion} está vacío"
            raise ValueError(mensaje)
        if nombre in vistos:
            raise ValueError(f"Fila 1: el encabezado '{nombre}' está duplicado")
        vistos.add(nombre)


def _construir_registros(headers, reader):
    """Arma los registros validando la cantidad de campos de cada fila."""
    _validar_encabezados(headers)
    registros = []
    for row in reader:
        if not row:
            continue
        if len(row) != len(headers):
            raise ValueError(
                f"Fila {reader.line_num}: se esperaban {len(headers)} campos "
                f"y se encontraron {len(row)}"
            )
        registros.append(dict(zip(headers, row)))
    return registros


def parse_csv(file_path, has_header=True, delimiter=",", encoding="utf-8"):
    """
    Lee un archivo CSV y devuelve:
    - has_header=True: lista de diccionarios (claves = primera fila)
    - has_header=False: lista de listas
    """
    try:
        with open(file_path, "r", encoding=encoding) as f:
            reader = csv.reader(f, delimiter=delimiter)
            if has_header:
                try:
                    headers = next(reader)
                except StopIteration:
                    raise ValueError("El archivo CSV está vacío")
                return _construir_registros(headers, reader)
            else:
                return list(reader)
    except UnicodeDecodeError:
        with open(file_path, "r", encoding="latin-1") as f:
            reader = csv.reader(f, delimiter=delimiter)
            if has_header:
                try:
                    headers = next(reader)
                except StopIteration:
                    raise ValueError("El archivo CSV está vacío")
                return _construir_registros(headers, reader)
            else:
                return list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encuentra el archivo: {file_path}")
