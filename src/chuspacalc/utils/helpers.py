import math
from pathlib import Path


def formatear_numero(valor: int | float, decimales: int = 2) -> str:
    """
    Formatea un número con separadores de miles y decimales especificados.

    Args:
        valor: Número que se desea formatear.
        decimales: Cantidad de posiciones decimales. Por defecto, 2.

    Returns:
        El número formateado como una cadena de texto.

    Ejemplo:
        >>> formatear_numero(1234.567)
        '1,234.57'
        >>> formatear_numero(1234.567, 0)
        '1,235'
    """
    if decimales == 0:
        return f"{valor:,.0f}"

    return f"{valor:,.{decimales}f}"


def copiar_al_portapapeles(texto: str) -> None:
    """
    Copia una cadena de texto al portapapeles del sistema.

    Args:
        texto: Texto que se desea copiar.

    Raises:
        RuntimeError: Si no existe una instancia activa de QApplication.
    """
    from PySide6.QtWidgets import QApplication

    app = QApplication.instance()

    if not isinstance(app, QApplication):
        raise RuntimeError("No hay QApplication activa")

    clipboard = app.clipboard()
    clipboard.setText(texto)


def exportar_a_archivo(contenido: str, ruta: str | Path) -> None:
    """
    Exporta contenido de texto a un archivo.

    Crea los directorios necesarios si todavía no existen.

    Args:
        contenido: Texto que se desea guardar.
        ruta: Ruta del archivo de destino.

    Raises:
        OSError: Si ocurre un error al crear directorios o escribir el archivo.
    """
    path = Path(ruta)

    path.parent.mkdir(parents=True, exist_ok=True)

    with open(path, "w", encoding="utf-8") as archivo:
        archivo.write(contenido)


def leer_archivo(ruta: str | Path) -> str:
    """
    Lee un archivo de texto y devuelve su contenido.

    Args:
        ruta: Ruta del archivo que se desea leer.

    Returns:
        Contenido del archivo como una cadena de texto.

    Raises:
        OSError: Si ocurre un error al abrir o leer el archivo.
    """
    with open(ruta, "r", encoding="utf-8") as archivo:
        return archivo.read()


def validar_numero(
    texto: str,
    permitir_negativo: bool = True,
    permitir_decimal: bool = True,
) -> bool:
    """
    Valida si un texto puede convertirse a número.

    Permite configurar si se aceptan números negativos y decimales.

    Args:
        texto: Cadena de texto que se desea validar.
        permitir_negativo: Indica si se permiten números negativos.
            Por defecto, True.
        permitir_decimal: Indica si se permiten números con punto decimal.
            Por defecto, True.

    Returns:
        True si el texto representa un número finito que cumple las
        condiciones de validación; False en caso contrario. Los valores
        no finitos (nan, inf y -inf) siempre se rechazan.
    """
    try:
        numero = float(texto)

        if not math.isfinite(numero):
            return False

        if not permitir_negativo and numero < 0:
            return False

        if not permitir_decimal and "." in texto:
            return False

        return True

    except ValueError:
        return False
