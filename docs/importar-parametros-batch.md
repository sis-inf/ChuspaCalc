# Importación de parámetros desde CSV para cálculo en lote

## Introducción

ChuspaCalc permite importar parámetros desde un archivo CSV para ejecutar cálculos en lote desde la interfaz gráfica (GUI). Esta funcionalidad facilita el procesamiento de múltiples casos utilizando un único archivo de entrada, evitando el ingreso manual de datos para cada cálculo.

## Flujo general

El proceso de importación sigue las siguientes etapas:

1. Seleccionar un archivo CSV desde la interfaz gráfica.
2. Leer y validar el contenido del archivo.
3. Procesar cada fila como un conjunto independiente de parámetros.
4. Ejecutar el cálculo correspondiente para cada registro.
5. Mostrar los resultados obtenidos.

## Ejemplo de archivo CSV

El siguiente ejemplo muestra un archivo CSV válido para realizar cálculos en lote.

```csv
id,base,altura
1,5,8
2,10,4
3,7.5,6
4,12,9
```

Cada fila representa un conjunto de parámetros independiente que será procesado por la aplicación.

## Ejemplo de resultados

Después del procesamiento del archivo, la aplicación genera un resultado para cada registro.

| ID | Base | Altura | Resultado |
| -- | ---- | ------ | --------- |
| 1  | 5.0  | 8.0    | 40.0      |
| 2  | 10.0 | 4.0    | 40.0      |
| 3  | 7.5  | 6.0    | 45.0      |
| 4  | 12.0 | 9.0    | 108.0     |

## Recomendaciones

* Mantener la fila de encabezados en el archivo CSV.
* Utilizar el mismo número de columnas en todos los registros.
* Verificar que los valores numéricos tengan un formato válido.
* Revisar los resultados obtenidos después de la importación para confirmar que todos los registros fueron procesados correctamente.

## Resumen

La importación de parámetros desde CSV permite automatizar el procesamiento de múltiples cálculos desde la interfaz gráfica, mejorando la productividad y reduciendo errores asociados al ingreso manual de datos.
