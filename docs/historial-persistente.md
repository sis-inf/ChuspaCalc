# Historial persistente de cálculos

## Introducción

ChuspaCalc mantiene un historial de los cálculos realizados para facilitar la consulta de resultados obtenidos previamente. Esta funcionalidad permite revisar operaciones anteriores sin necesidad de volver a introducir los mismos parámetros.

El historial permanece disponible entre sesiones de la aplicación, permitiendo continuar el trabajo desde donde se dejó.

---

## Ubicación del historial

El historial persistente se almacena automáticamente por la aplicación utilizando su mecanismo interno de persistencia.

El usuario no necesita crear ni modificar manualmente el archivo del historial, ya que ChuspaCalc administra el almacenamiento de forma transparente.

---

## Registro de cálculos

Cada vez que se ejecuta un cálculo correctamente, se registra información como:

- Herramienta utilizada.
- Parámetros ingresados.
- Resultado obtenido.
- Fecha y hora de ejecución.

Esta información permite consultar posteriormente cómo se obtuvo un resultado determinado.

---

## Acceso desde el panel de historial

Para consultar cálculos anteriores:

1. Abrir la interfaz gráfica de ChuspaCalc.
2. Seleccionar el **Panel de historial**.
3. Revisar la lista de cálculos registrados.
4. Seleccionar una entrada para visualizar sus detalles.

El panel presenta primero los cálculos más recientes, facilitando el acceso a las últimas operaciones realizadas.

---

## Información mostrada

Cada registro del historial puede incluir:

| Campo | Descripción |
|--------|-------------|
| Herramienta | Módulo utilizado para realizar el cálculo |
| Parámetros | Valores ingresados por el usuario |
| Resultado | Resultado generado |
| Fecha y hora | Momento en que se ejecutó el cálculo |

---

## Ejemplo

| Herramienta | Parámetros | Resultado |
|-------------|------------|-----------|
| Área de círculo | Radio = 5 | Área = 78.54 |
| Conversión de unidades | 10 m → cm | 1000 cm |

---

## Consideraciones

- El historial se actualiza automáticamente después de cada cálculo.
- La navegación se realiza desde el panel de historial de la interfaz gráfica.
- No es necesario administrar manualmente el almacenamiento del historial.