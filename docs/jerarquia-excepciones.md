# Jerarquía de excepciones

## Descripción

Este documento describe las excepciones específicas del dominio utilizadas en el proyecto ChuspaCalc. Estas excepciones permiten identificar distintos tipos de errores durante la ejecución de las herramientas.

Para conocer ejemplos de errores frecuentes y sus posibles soluciones, consultar el documento `docs/errores-comunes.md`.

## ErrorChuspaCalc

`ErrorChuspaCalc` es la excepción base del proyecto.

Las demás excepciones específicas heredan de esta clase y representan distintos tipos de errores relacionados con el funcionamiento de ChuspaCalc.

Se utiliza para agrupar las excepciones propias del dominio y facilitar su manejo.

## ErrorParametros

`ErrorParametros` representa errores ocasionados por parámetros inválidos o incompletos proporcionados por el usuario.

Ejemplos:

- Valores fuera del rango permitido.
- Parámetros obligatorios ausentes.
- Tipos de datos incorrectos.

## ErrorCalculo

`ErrorCalculo` se utiliza cuando ocurre un problema durante la ejecución de un cálculo.

Puede presentarse cuando una operación matemática no puede completarse correctamente o cuando los datos de entrada producen un resultado inválido.

## ErrorValidacion

`ErrorValidacion` representa errores detectados durante la validación de los datos antes de ejecutar un proceso.

Esta excepción ayuda a garantizar que la información cumpla con las reglas definidas por el proyecto antes de realizar cálculos o generar resultados.

## Recomendaciones

- Utilizar la excepción más específica posible.
- Validar los parámetros antes de ejecutar cálculos.
- Capturar las excepciones para mostrar mensajes claros al usuario.
- Consultar `docs/errores-comunes.md` para información complementaria sobre errores habituales.