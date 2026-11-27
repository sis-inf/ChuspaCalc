# Glosario técnico — ChuspaCalc

Este glosario complementa a `docs/glosario.md` con definiciones técnicas de los términos de ingeniería utilizados en los módulos de ChuspaCalc. Está orientado a estudiantes que implementan o mantienen los módulos `civil`, `electrica` y `matematicas`, y que necesitan comprender el dominio del problema sin ser especialistas en esas ramas.

---

## Módulo civil

### Momento flector

- **Símbolo:** M
- **Unidad SI:** N·m (frecuentemente kN·m en aplicaciones reales)

Es la resultante de las tensiones internas que produce el giro y la flexión de una sección transversal de una viga sometida a cargas perpendiculares a su eje longitudinal. Se calcula como la suma de los momentos de todas las fuerzas situadas a un lado de la sección analizada. Es la magnitud principal para dimensionar vigas, ya que determina las tensiones de tracción y compresión en las fibras del material.

### Viga simplemente apoyada

- **Símbolo:** no aplica (tipo de elemento estructural)
- **Unidad SI:** no aplica

Es una viga sostenida por dos apoyos: uno fijo (que restringe desplazamiento horizontal y vertical) y otro móvil o de rodillo (que solo restringe desplazamiento vertical). Es el caso más simple de análisis estructural porque es isostática, es decir, sus reacciones pueden calcularse únicamente con las ecuaciones de equilibrio estático sin necesidad de considerar la deformación.

### Deflexión

- **Símbolo:** δ (delta) o y
- **Unidad SI:** m (frecuentemente mm en aplicaciones reales)

Es el desplazamiento vertical que experimenta un punto de una viga respecto a su posición original, como consecuencia de las cargas aplicadas. Se relaciona con el momento flector y el módulo de elasticidad a través de la ecuación de la curva elástica. Los códigos de diseño suelen limitar la deflexión máxima permitida como fracción de la longitud del elemento (por ejemplo, L/250).

### Reacción de apoyo

- **Símbolo:** R (con subíndice según el apoyo, p. ej. Ra, Rb)
- **Unidad SI:** N (frecuentemente kN)

Es la fuerza (o momento, en apoyos empotrados) que un apoyo ejerce sobre una estructura para mantener el equilibrio frente a las cargas aplicadas. En vigas isostáticas, las reacciones se calculan aplicando las ecuaciones de equilibrio: suma de fuerzas verticales igual a cero, suma de fuerzas horizontales igual a cero, y suma de momentos igual a cero.

### Carga distribuida

- **Símbolo:** w o q
- **Unidad SI:** N/m (frecuentemente kN/m)

Es una carga que actúa repartida a lo largo de una longitud del elemento estructural, en lugar de concentrarse en un punto. Puede ser uniforme (mismo valor en toda su longitud) o variable (por ejemplo, triangular o trapezoidal). Para el cálculo de reacciones y momentos, una carga distribuida uniforme puede reemplazarse por una carga puntual equivalente situada en su centroide.

### Módulo de elasticidad

- **Símbolo:** E
- **Unidad SI:** Pa (frecuentemente GPa o MPa en aplicaciones reales)

También llamado módulo de Young, cuantifica la rigidez de un material: la relación entre el esfuerzo aplicado y la deformación unitaria que produce, dentro del rango elástico (donde el material recupera su forma original al retirar la carga). Es un dato característico de cada material; por ejemplo, el acero estructural tiene un módulo de elasticidad mucho mayor que la madera o el hormigón.

### Momento de inercia

- **Símbolo:** I
- **Unidad SI:** m⁴ (frecuentemente cm⁴ o mm⁴ en aplicaciones reales)

También llamado segundo momento de área, describe cómo está distribuida el área de una sección transversal respecto a un eje de referencia. A mayor momento de inercia, mayor resistencia ofrece la sección a la flexión y menor es su deflexión, para una misma carga y material. No debe confundirse con el momento de inercia de masa, usado en dinámica rotacional, que tiene unidades distintas (kg·m²).

### Esfuerzo cortante

- **Símbolo:** V o Q
- **Unidad SI:** N (frecuentemente kN)

Es la fuerza interna resultante de las tensiones tangenciales que actúan paralelas a la sección transversal de una viga, perpendiculares al eje de flexión. Junto con el momento flector, es una de las dos solicitaciones principales en el análisis de vigas, y su diagrama a lo largo del elemento se obtiene derivando la función de carga distribuida o, de forma equivalente, integrando la carga aplicada.

---

## Módulo eléctrico

### Ley de Ohm

- **Símbolo:** V = I·R
- **Unidad SI:** V (voltios), A (amperios), Ω (ohmios)

Establece que la diferencia de potencial (tensión) entre dos puntos de un conductor es directamente proporcional a la corriente que circula por él, siendo la resistencia la constante de proporcionalidad. Es la relación fundamental para el análisis de circuitos resistivos y se cumple en materiales ohmicos, donde la resistencia se mantiene constante independientemente de la tensión o corriente aplicada.

### Divisor de tensión

- **Símbolo:** no aplica (configuración de circuito)
- **Unidad SI:** V (resultado en voltios)

Es una configuración de dos o más resistencias en serie que permite obtener una fracción de la tensión total de la fuente en un punto intermedio del circuito. La tensión sobre cada resistencia es proporcional a su valor respecto a la resistencia total del divisor, según la fórmula Vx = V_total × (Rx / R_total). Es un circuito muy usado para adaptar niveles de tensión a sensores o entradas de microcontroladores.

### Circuito en serie

- **Símbolo:** no aplica (configuración de circuito)
- **Unidad SI:** no aplica

Es una conexión de componentes eléctricos uno después de otro, formando un único camino para la corriente. En esta configuración, la misma corriente circula por todos los elementos, mientras que la tensión total de la fuente se reparte entre ellos según sus resistencias individuales. La resistencia equivalente de un circuito en serie es la suma de las resistencias individuales.

### Circuito en paralelo

- **Símbolo:** no aplica (configuración de circuito)
- **Unidad SI:** no aplica

Es una conexión de componentes eléctricos donde todos comparten los mismos dos nodos, formando varios caminos posibles para la corriente. En esta configuración, la tensión es la misma en todos los elementos, mientras que la corriente total se distribuye entre las ramas según su resistencia. La resistencia equivalente de un circuito en paralelo es siempre menor que la resistencia más pequeña de las ramas individuales.

### Potencia activa

- **Símbolo:** P
- **Unidad SI:** W (vatios)

Es la potencia eléctrica que efectivamente se transforma en trabajo útil (calor, luz, movimiento), a diferencia de la potencia reactiva, que no realiza trabajo neto pero es necesaria para el funcionamiento de cargas inductivas o capacitivas. En corriente continua se calcula como P = V·I; en corriente alterna depende además del ángulo de desfase entre tensión y corriente.

### Frecuencia angular o resistencia

- **Símbolo:** ω (omega)
- **Unidad SI:** rad/s

Es la velocidad de variación de la fase de una señal periódica, como una tensión o corriente alterna. Se relaciona con la frecuencia ordinaria mediante ω = 2πf, donde f está en hercios (Hz). Es la magnitud utilizada en el análisis fasorial de circuitos de corriente alterna, especialmente al calcular la reactancia de inductores y capacitores.

---

## Métodos numéricos

### Error absoluto

- **Símbolo:** Ea
- **Unidad SI:** depende de la magnitud medida

Es la diferencia entre el valor exacto (o de referencia) de una magnitud y el valor aproximado obtenido mediante un método numérico. Se calcula como Ea = |valor exacto − valor aproximado|. Es útil para evaluar la precisión de un método, pero no permite comparar errores entre magnitudes de distinta escala.

### Error relativo

- **Símbolo:** Er
- **Unidad SI:** adimensional (frecuentemente expresado en porcentaje)

Es el error absoluto expresado como fracción del valor exacto: Er = Ea / |valor exacto|. A diferencia del error absoluto, permite comparar la precisión de aproximaciones entre magnitudes de distinta escala, ya que normaliza el error respecto al tamaño de la cantidad medida.

### Método de bisección

- **Símbolo:** no aplica (algoritmo numérico)
- **Unidad SI:** no aplica

Es un método iterativo para encontrar raíces de una función continua, que aprovecha el cambio de signo de la función en un intervalo. En cada iteración, el intervalo se divide a la mitad y se conserva la mitad donde la función cambia de signo, hasta que el intervalo es suficientemente pequeño según una tolerancia definida. Es un método robusto pero de convergencia lenta comparado con otros métodos como Newton-Raphson.

### Método de Newton-Raphson

- **Símbolo:** no aplica (algoritmo numérico)
- **Unidad SI:** no aplica

Es un método iterativo para encontrar raíces de una función, que utiliza la derivada de la función para aproximar sucesivamente el valor de la raíz mediante rectas tangentes. Converge más rápido que el método de bisección cuando el punto inicial está suficientemente cerca de la raíz, pero puede no converger si la derivada se aproxima a cero o si el punto inicial está mal elegido.

### Interpolación lineal

- **Símbolo:** no aplica (técnica numérica)
- **Unidad SI:** depende de la magnitud interpolada

Es una técnica para estimar el valor de una función en un punto intermedio entre dos puntos conocidos, asumiendo que la función varía de forma lineal entre ellos. Se calcula mediante la fórmula y = y1 + (x − x1) × (y2 − y1) / (x2 − x1). Es ampliamente utilizada en tablas de propiedades de materiales y en el procesamiento de datos experimentales.

### Tolerancia (en métodos iterativos)

- **Símbolo:** ε (épsilon) o tol
- **Unidad SI:** depende de la magnitud evaluada

Es el valor umbral que define cuándo un método iterativo se considera convergido, es decir, cuándo la diferencia entre dos aproximaciones sucesivas (o el valor del error) es suficientemente pequeña para detener el cálculo. Una tolerancia muy pequeña aumenta la precisión del resultado pero también el número de iteraciones necesarias.

### Convergencia

- **Símbolo:** No aplica
- **Unidad SI:** No aplica

Propiedad de un método numérico que indica que las aproximaciones sucesivas se acercan progresivamente al valor real de la solución. La velocidad de convergencia es un criterio importante para comparar la eficiencia de distintos algoritmos.

### Redondeo de punto flotante

- **Símbolo:** no aplica (fenómeno numérico)
- **Unidad SI:** no aplica

Es la pérdida de precisión que ocurre al representar números reales en una computadora usando un número finito de bits (estándar IEEE 754). Produce que operaciones matemáticamente exactas, como sumas o comparaciones de igualdad entre números decimales, puedan dar resultados ligeramente distintos a los esperados. Es relevante al implementar criterios de convergencia o comparaciones de valores en los módulos numéricos del proyecto.

---

## Referencias

- `docs/glosario.md` — glosario general de términos del proyecto
- `src/ChuspaCalc/modulos/civil/` — implementación del módulo civil
- `src/ChuspaCalc/modulos/electrica/` — implementación del módulo eléctrico
- `src/ChuspaCalc/modulos/matematicas/` — implementación de métodos numéricos