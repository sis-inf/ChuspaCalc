import csv


def parse_csv(file_path, has_header=True, delimiter=',', encoding='utf-8'):
    """
    Lee un archivo CSV y devuelve:
    - has_header=True: lista de diccionarios (claves = primera fila)
    - has_header=False: lista de listas
    """
    try:
        with open(file_path, 'r', encoding=encoding) as f:
            reader = csv.reader(f, delimiter=delimiter)
            if has_header:
                try:
                    headers = next(reader)
                except StopIteration:
                    raise ValueError('El archivo CSV está vacío')
                return [dict(zip(headers, row)) for row in reader]
            else:
                return list(reader)
    except UnicodeDecodeError:
        with open(file_path, 'r', encoding='latin-1') as f:
            reader = csv.reader(f, delimiter=delimiter)
            if has_header:
                try:
                    headers = next(reader)
                except StopIteration:
                    raise ValueError('El archivo CSV está vacío')
                return [dict(zip(headers, row)) for row in reader]
            else:
                return list(reader)
    except FileNotFoundError:
        raise FileNotFoundError(f"No se encuentra el archivo: {file_path}")
