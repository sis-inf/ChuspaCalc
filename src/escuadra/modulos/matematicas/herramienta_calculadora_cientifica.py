import math

from PySide6.QtWidgets import QWidget

from escuadra.core.carrera import Carrera
from escuadra.core.herramienta import Herramienta


class HerramientaCalculadoraCientifica(Herramienta):
    nombre = "Calculadora científica"
    carrera = Carrera.MATEMATICAS
    descripcion = (
        "Calculadora con operaciones aritméticas, trigonométricas, "
        "logarítmicas y constantes."
    )

    def __init__(self):
        super().__init__()

    def evaluar_expresion(
        self, expresion: str, modo_angular: str = "Radianes"
    ) -> float:
        if not expresion or not isinstance(expresion, str):
            raise ValueError("La expresión debe ser una cadena de texto válida.")

        expresion_limpia = expresion.replace("^", "**")
        expresion_limpia = expresion_limpia.replace("π", "math.pi")

        entorno_seguro = {
            "math": math,
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "sqrt": math.sqrt,
            "pi": math.pi,
            "e": math.e,
        }

        if modo_angular == "Grados":
            entorno_seguro["sin"] = lambda x: math.sin(math.radians(x))
            entorno_seguro["cos"] = lambda x: math.cos(math.radians(x))
            entorno_seguro["tan"] = lambda x: math.tan(math.radians(x))

        try:
            resultado = eval(expresion_limpia, {"__builtins__": None}, entorno_seguro)

            if not isinstance(resultado, (int, float)):
                raise ValueError("Expresión inválida")

            return float(resultado)

        except ZeroDivisionError:
            raise ZeroDivisionError("Error: División por cero.")
        except ValueError as ve:
            raise ValueError(f"Error de dominio o sintaxis: {str(ve)}")
        except SyntaxError:
            raise SyntaxError("Error de sintaxis: La expresión está mal formada.")
        except Exception:
            raise ValueError("Error claro: Expresión inválida o no permitida.")

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        return widget
