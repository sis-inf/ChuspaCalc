"""
Exportador de resultados a formato LaTeX.
Permite generar tablas y fórmulas listas para documentos académicos.
"""


def escapar_latex(texto):
    """Escapa caracteres especiales de LaTeX."""
    reemplazos = {
        "&": r"\&",
        "%": r"\%",
        "$": r"\$",
        "#": r"\#",
        "_": r"\_",
    }

    texto = str(texto)

    for caracter, reemplazo in reemplazos.items():
        texto = texto.replace(caracter, reemplazo)

    return texto


def exportar_tabla(parametros, resultado, formula=None):
    """
    Genera una tabla LaTeX con parámetros y resultado.

    Args:
        parametros (dict): Datos usados en el cálculo.
        resultado: Resultado obtenido.
        formula (str): Fórmula opcional usada.

    Returns:
        str: Código LaTeX generado.
    """

    lineas = [
        r"\begin{tabular}{|l|l|}",
        r"\hline",
        "Parámetro & Valor \\\\",
        r"\hline",
    ]

    for clave, valor in parametros.items():
        lineas.append(
            f"{escapar_latex(clave)} & {escapar_latex(valor)} \\\\"
        )

    lineas.extend([
        r"\hline",
        f"Resultado & {escapar_latex(resultado)} \\\\",
        r"\hline",
        r"\end{tabular}",
    ])

    if formula:
        lineas.append("")
        lineas.append(r"\[")
        lineas.append(str(formula))
        lineas.append(r"\]")

    return "\n".join(lineas)
