import ast
import math
import operator
from collections.abc import Callable, Mapping

from PySide6.QtWidgets import QWidget

from chuspacalc.core.carrera import Carrera
from chuspacalc.core.herramienta import Herramienta

MAX_EXPRESSION_LENGTH = 512
MAX_AST_NODES = 128
MAX_AST_DEPTH = 24
MAX_ABS_RESULT = 1e100
MAX_ABS_EXPONENT = 100


class _EvaluadorMatematico:
    """Interpreta una expresión matemática sobre una lista blanca de nodos AST."""

    _operadores_binarios: dict[type[ast.operator], Callable[[float, float], float]] = {
        ast.Add: operator.add,
        ast.Sub: operator.sub,
        ast.Mult: operator.mul,
        ast.Div: operator.truediv,
        ast.FloorDiv: operator.floordiv,
        ast.Mod: operator.mod,
    }
    _operadores_unarios: dict[type[ast.unaryop], Callable[[float], float]] = {
        ast.UAdd: operator.pos,
        ast.USub: operator.neg,
    }

    def __init__(
        self,
        funciones: Mapping[str, Callable[[float], float]],
        constantes: Mapping[str, float],
    ) -> None:
        self._funciones = funciones
        self._constantes = constantes

    def evaluar(self, expresion: str) -> float:
        arbol = ast.parse(expresion, mode="eval")
        nodos = list(ast.walk(arbol))
        if len(nodos) > MAX_AST_NODES:
            raise ValueError("La expresión es demasiado compleja.")
        return self._evaluar_nodo(arbol.body, profundidad=1)

    def _evaluar_nodo(self, nodo: ast.AST, profundidad: int) -> float:
        if profundidad > MAX_AST_DEPTH:
            raise ValueError("La expresión excede la profundidad permitida.")

        if isinstance(nodo, ast.Constant):
            if isinstance(nodo.value, bool) or not isinstance(nodo.value, (int, float)):
                raise ValueError("Solo se permiten constantes numéricas.")
            return self._validar_resultado(float(nodo.value))

        if isinstance(nodo, ast.Name):
            if nodo.id not in self._constantes:
                raise ValueError(f"Nombre no permitido: {nodo.id}")
            return self._constantes[nodo.id]

        if isinstance(nodo, ast.UnaryOp) and type(nodo.op) in self._operadores_unarios:
            valor = self._evaluar_nodo(nodo.operand, profundidad + 1)
            return self._validar_resultado(
                self._operadores_unarios[type(nodo.op)](valor)
            )

        if isinstance(nodo, ast.BinOp):
            izquierda = self._evaluar_nodo(nodo.left, profundidad + 1)
            derecha = self._evaluar_nodo(nodo.right, profundidad + 1)
            if isinstance(nodo.op, ast.Pow):
                if abs(derecha) > MAX_ABS_EXPONENT:
                    raise ValueError("El exponente excede el límite permitido.")
                try:
                    resultado = izquierda**derecha
                except OverflowError as error:
                    raise ValueError(
                        "El resultado excede el límite permitido."
                    ) from error
            elif type(nodo.op) in self._operadores_binarios:
                resultado = self._operadores_binarios[type(nodo.op)](izquierda, derecha)
            else:
                raise ValueError("Operador no permitido.")
            if isinstance(resultado, complex):
                raise ValueError("El resultado debe ser un número real.")
            return self._validar_resultado(float(resultado))

        if isinstance(nodo, ast.Call):
            if (
                not isinstance(nodo.func, ast.Name)
                or nodo.func.id not in self._funciones
            ):
                raise ValueError("Función no permitida.")
            if len(nodo.args) != 1 or nodo.keywords:
                raise ValueError("La función requiere exactamente un argumento.")
            argumento = self._evaluar_nodo(nodo.args[0], profundidad + 1)
            return self._validar_resultado(
                float(self._funciones[nodo.func.id](argumento))
            )

        raise ValueError(f"Construcción no permitida: {type(nodo).__name__}")

    @staticmethod
    def _validar_resultado(resultado: float) -> float:
        if not math.isfinite(resultado):
            raise ValueError("El resultado debe ser finito.")
        if abs(resultado) > MAX_ABS_RESULT:
            raise ValueError("El resultado excede el límite permitido.")
        return resultado


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
        if len(expresion) > MAX_EXPRESSION_LENGTH:
            raise ValueError("La expresión excede la longitud permitida.")

        expresion_limpia = expresion.replace("^", "**").replace("π", "pi")

        funciones = {
            "sin": math.sin,
            "cos": math.cos,
            "tan": math.tan,
            "log": math.log10,
            "ln": math.log,
            "sqrt": math.sqrt,
        }
        constantes = {
            "pi": math.pi,
            "e": math.e,
        }

        if modo_angular == "Grados":
            funciones["sin"] = lambda x: math.sin(math.radians(x))
            funciones["cos"] = lambda x: math.cos(math.radians(x))
            funciones["tan"] = lambda x: math.tan(math.radians(x))

        try:
            return _EvaluadorMatematico(funciones, constantes).evaluar(expresion_limpia)

        except ZeroDivisionError:
            raise ZeroDivisionError("Error: División por cero.")
        except ValueError as ve:
            raise ValueError(f"Error de dominio o sintaxis: {str(ve)}")
        except SyntaxError:
            raise SyntaxError("Error de sintaxis: La expresión está mal formada.")

    def crear_widget(self) -> QWidget:
        widget = QWidget()
        return widget
