# ❓ Preguntas Frecuentes - Fórmulas y Cálculos Matemáticos

Este documento responde a las dudas más comunes sobre el uso de las herramientas de cálculo de ChuspaCalc, especialmente aquellas relacionadas con **fórmulas matemáticas, resultados numéricos y advertencias**.

> **Nota:** Este FAQ está orientado a **dudas de uso de las herramientas de cálculo**. Si buscás información sobre cómo contribuir al proyecto, consultá [preguntas-frecuentes.md](preguntas-frecuentes.md).

---

## 📋 Preguntas Frecuentes

### 1. ¿Por qué mi cálculo de pandeo de Euler muestra una advertencia?

**Respuesta:** La advertencia aparece cuando la relación de esbeltez de la columna está fuera del rango de validez de la fórmula de Euler (generalmente cuando la relación esbeltez < 50). En ese caso, se recomienda utilizar la fórmula de Johnson para materiales con esbeltez intermedia.

**Solución:** Verificar que la longitud efectiva y el radio de giro de la columna sean correctos. Si la esbeltez es baja, considerá usar la fórmula de Johnson.

---

### 2. ¿Qué significa que mi sistema lineal NxN no tenga solución única?

**Respuesta:** Un sistema lineal no tiene solución única cuando el determinante de la matriz de coeficientes es igual a cero (matriz singular). Esto puede deberse a:

- Ecuaciones redundantes (linealmente dependientes).
- Número de ecuaciones menor que el número de incógnitas.

**Solución:** Revisar los coeficientes del sistema. Asegurarse de que todas las ecuaciones sean independientes.

---

### 3. ¿Por qué el resultado de mi viga muestra un error de convergencia?

**Respuesta:** El error de convergencia ocurre cuando el método numérico utilizado (ej. iterativo) no logra alcanzar una solución dentro del número máximo de iteraciones permitido.

**Solución:** Verificar que los parámetros de entrada sean realistas y que el modelo sea adecuado para el método seleccionado.

---

### 4. ¿Cómo interpreto una advertencia de rango de validez?

**Respuesta:** Las advertencias de rango de validez indican que los parámetros ingresados están fuera del rango para el cual la fórmula es precisa. Por ejemplo, una fórmula de resistencia de materiales puede no ser precisa para cargas extremadamente altas.

**Solución:** Revisar los valores de entrada y ajustarlos a rangos razonables. Consultar la documentación de la herramienta para conocer los límites recomendados.

---

### 5. ¿Qué significa que mi resultado sea `inf` o `NaN`?

**Respuesta:**

- `inf` (infinito) indica que el resultado es demasiado grande para ser representado (ej. división por un número muy cercano a cero).
- `NaN` (Not a Number) indica un resultado indefinido (ej. raíz cuadrada de un número negativo).

**Solución:** Verificar los parámetros de entrada. Asegurarse de que no haya divisiones por cero o raíces de números negativos.

---

### 6. ¿Por qué mi cálculo de factor de potencia no se puede realizar?

**Respuesta:** El cálculo de factor de potencia requiere que el sistema tenga una carga activa y reactiva definida. Si alguna de ellas es cero o negativa, el cálculo puede fallar.

**Solución:** Verificar que la potencia activa (P) y reactiva (Q) sean valores positivos y realistas.

---

### 7. ¿Qué hacer si el resultado de mi integración numérica es inexacto?

**Respuesta:** La precisión de la integración numérica depende del método utilizado (ej. Simpson, trapecios) y del número de intervalos. Si el resultado parece impreciso, se recomienda:

- Aumentar el número de intervalos.
- Utilizar un método más preciso (ej. Simpson en lugar de trapecios).

**Solución:** Ajustar los parámetros de integración y verificar que la función sea continua en el intervalo.

---

### 8. ¿Cómo sé si el resultado de mi cálculo es confiable?

**Respuesta:** Para verificar la confiabilidad de un resultado, se recomienda:

1. Realizar una estimación de orden de magnitud (ej. ¿tiene sentido el resultado?).
2. Comparar con resultados de otros métodos (ej. solución analítica vs. numérica).
3. Verificar que no haya advertencias o errores en el cálculo.

**Solución:** Usar el sentido común y, si es posible, validar con una herramienta externa (ej. Excel, MATLAB).

---

### 9. ¿Qué debo hacer si recibo un mensaje de error de convergencia en sistemas no lineales?

**Respuesta:** Los sistemas no lineales pueden requerir una buena estimación inicial para converger. Si el método no converge, se recomienda:

- Probar con diferentes valores iniciales.
- Verificar que las ecuaciones estén bien definidas.
- Reducir la tolerancia del método.

**Solución:** Ajustar los parámetros de entrada y las opciones del método numérico.

---

### 10. ¿Por qué mi cálculo de carga crítica de Euler varía entre diferentes secciones?

**Respuesta:** La carga crítica de Euler depende del momento de inercia de la sección (`I`) y de la longitud efectiva (`L`). Diferentes secciones tienen diferentes momentos de inercia, lo que afecta el resultado.

**Solución:** Asegurarse de que la sección seleccionada tenga el momento de inercia correcto (ej. IPN, HEB, etc.). Consultar la documentación de la herramienta para más detalles.

---

## 📚 Referencias

- [Guía de herramientas disponibles](herramientas.md)
- [Documentación de módulos de cálculo](modulos/README.md)
- [FAQ de contribución](preguntas-frecuentes.md)
