# Integración con Google Sheets

Ejemplo de función personalizada usando Google Apps Script para invocar cálculos de ChuspaCalc desde una hoja de cálculo.

## Uso

1. Ejecutar ChuspaCalc localmente con la API HTTP activada.
2. Abrir Google Sheets.
3. Crear un proyecto de Apps Script.
4. Copiar el contenido de `funcion-personalizada.gs`.

Ejemplo:

=CHUSPACALC_CALCULAR("herramienta", A1:B2)

## Limitación

Esta integración requiere que ChuspaCalc esté ejecutándose localmente y que el servidor HTTP esté disponible.

La función realiza una petición al endpoint local y devuelve el resultado recibido.
