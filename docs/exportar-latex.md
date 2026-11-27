# Exportación de resultados a LaTeX

## Introducción

ChuspaCalc permite exportar los resultados de los cálculos en formato **LaTeX**, facilitando su incorporación en informes técnicos, artículos científicos, tesis y otros documentos académicos.

La exportación genera código compatible con LaTeX, listo para copiar e insertar en un documento `.tex`.

---

## ¿Qué se exporta?

La exportación puede incluir la siguiente información:

- Nombre de la herramienta utilizada.
- Parámetros de entrada.
- Resultados obtenidos.
- Tabla con los valores calculados.

El contenido generado puede incorporarse directamente a un documento académico sin necesidad de modificaciones adicionales.

---

## Cómo exportar un resultado

1. Ejecutar un cálculo desde la interfaz gráfica.
2. Verificar los resultados mostrados.
3. Seleccionar la opción **Exportar**.
4. Elegir el formato **LaTeX (.tex)**.
5. Indicar la ubicación donde se guardará el archivo.
6. Confirmar la exportación.

---

## Ejemplo de tabla LaTeX generada

```latex
\begin{table}[h]
\centering
\begin{tabular}{|l|c|}
\hline
\textbf{Parámetro} & \textbf{Valor} \\
\hline
Longitud & 12.50 \\
Ancho & 8.00 \\
Área & 100.00 \\
\hline
\end{tabular}
\caption{Resultado del cálculo de un área rectangular}
\label{tab:area_rectangular}
\end{table}
```

La tabla anterior puede copiarse directamente dentro de un documento LaTeX y compilarse sin modificaciones.

---

## Ejemplo de uso en un documento

```latex
\documentclass{article}

\begin{document}

Los resultados del cálculo se presentan en la Tabla~\ref{tab:area_rectangular}.

\begin{table}[h]
\centering
\begin{tabular}{|l|c|}
\hline
\textbf{Parámetro} & \textbf{Valor} \\
\hline
Longitud & 12.50 \\
Ancho & 8.00 \\
Área & 100.00 \\
\hline
\end{tabular}
\caption{Resultado del cálculo de un área rectangular}
\label{tab:area_rectangular}
\end{table}

\end{document}
```

---

## Casos de uso

La exportación a LaTeX resulta útil para:

- Elaboración de informes técnicos.
- Redacción de artículos científicos.
- Desarrollo de tesis y proyectos de investigación.
- Preparación de material académico.
- Generación de documentación profesional.

---

## Consideraciones

- El código generado utiliza sintaxis estándar de LaTeX.
- Puede integrarse en cualquier documento `.tex`.
- Es compatible con distribuciones habituales como **TeX Live** y **MiKTeX**.
- Se recomienda revisar el contenido antes de la compilación final del documento cuando se combinen múltiples tablas o resultados.