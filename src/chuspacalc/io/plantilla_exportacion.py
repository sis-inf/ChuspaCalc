"""Plantillas reutilizables para configuraciones de exportación."""

FORMATOS_VALIDOS = ("json", "markdown", "latex", "csv")


def _validar_formato(formato) -> None:
    """Lanza ValueError si el formato no es válido."""
    if formato not in FORMATOS_VALIDOS:
        raise ValueError("Formato inválido: " + str(formato))


def _validar_campos(campos) -> None:
    """Lanza TypeError si campos no es una lista de str."""
    if not isinstance(campos, list):
        raise TypeError("campos debe ser una lista")
    for campo in campos:
        if not isinstance(campo, str):
            raise TypeError("todos los campos deben ser str")


class PlantillaExportacion:
    """Representa una configuración reutilizable para exportaciones."""

    def __init__(
        self,
        formato: str = "json",
        incluir_pasos: bool = False,
        campos: list | None = None,
    ) -> None:
        _validar_formato(formato)
        if campos is not None:
            _validar_campos(campos)
        self.formato = formato
        self.incluir_pasos = incluir_pasos
        self.campos = list(campos) if campos is not None else []

    def guardar(self) -> dict:
        """Devuelve la plantilla como un diccionario serializable."""
        return {
            "formato": self.formato,
            "incluir_pasos": self.incluir_pasos,
            "campos": self.campos.copy(),
        }

    @classmethod
    def cargar(cls, datos: dict):
        """Crea una plantilla a partir de un diccionario."""
        if not isinstance(datos, dict):
            raise TypeError(f"Se esperaba un dict, se recibió {type(datos).__name__}")

        return cls(
            formato=datos.get("formato", "json"),
            incluir_pasos=datos.get("incluir_pasos", False),
            campos=datos.get("campos", []),
        )

    def actualizar(self, **opciones) -> None:
        """Actualiza la configuración de la plantilla."""
        if "formato" in opciones:
            _validar_formato(opciones["formato"])
        if "campos" in opciones:
            _validar_campos(opciones["campos"])
        for clave, valor in opciones.items():
            if hasattr(self, clave):
                setattr(self, clave, valor)

    def copiar(self):
        """Devuelve una copia independiente de la plantilla."""
        return PlantillaExportacion.cargar(self.guardar())
