## Casos de Uso — ChuspaCalc

### Actores del sistema

**1. Estudiante de ingeniería:** Persona que cursa una carrera de ingeniería y utiliza ChuspaCalc como apoyo académico para resolver ejercicios, verificar cálculos y aplicar conceptos teóricos vistos en clase. Puede tener conocimientos básicos o intermedios según el semestre en curso.

**2. Docente:**Profesional del área de ingeniería que imparte clases y utiliza ChuspaCalc como recurso didáctico para demostrar procedimientos, plantear ejemplos prácticos y apoyar la enseñanza de conceptos técnicos.

### Casos de uso

## CU-01: Calcular propiedades geométricas de una figura

**Actor:** Estudiantes
**Descripcion:** El usuario selecciona una figura geométrica (triángulo, círculo, rectángulo, etc.), ingresa sus dimensiones y obtiene propiedades como área, perímetro o volumen.
**Flujo principal:** 
1. El usuario accede a la herramienta de geometría.  
2. Selecciona el tipo de figura.  
3. Ingresa los valores de las dimensiones requeridas.  
4. El sistema calcula y muestra los resultados (área, perímetro, etc.).  
5. El usuario puede copiar o reingresar nuevos valores.

## CU-02: Resolver un sistema de ecuaciones lineales

**Actor:** Estudiante de ingeniería / Docente
**Descripcion:** El usuario ingresa los coeficientes de un sistema de ecuaciones lineales y el sistema devuelve la solución mediante métodos como Gauss-Jordan o sustitución.
**Flujo principal:**
1. El usuario accede a la herramienta de álgebra lineal.  
2. Selecciona el número de ecuaciones e incógnitas.  
3. Ingresa los coeficientes de cada ecuación.  
4. El sistema aplica el método seleccionado y muestra la solución paso a paso.  
5. El usuario revisa el procedimiento y el resultado final.

## CU-03: Consultar fórmulas técnicas por área de ingeniería

**Actor:** Docente / Estudiante de ingeniería
**Descripcion:** El usuario navega por un repositorio de fórmulas organizadas por rama de ingeniería (civil, mecánica, sistemas, etc.) para consultar, entender y aplicar las expresiones matemáticas relevantes a su área.
**Flujo principal:** 
1. El usuario accede al módulo de referencia técnica.  
2. Selecciona la rama de ingeniería de interés.  
3. Explora las categorías de fórmulas disponibles.  
4. Selecciona una fórmula para ver su descripción, variables y ejemplo de aplicación.  
5. Puede usar la fórmula directamente en una herramienta de cálculo vinculada.

## CU-04: Convertir unidades de medida entre sistemas

**Actor:** Estudiante de ingeniería
**Descripcion:** El usuario ingresa un valor con su unidad de origen y selecciona la unidad destino. El sistema realiza la conversión de forma inmediata (longitud, masa, presión, temperatura, etc.).
**Flujo principal:** 
1. El usuario accede a la herramienta de conversión de unidades.  
2. Selecciona la categoría (longitud, masa, temperatura, etc.).  
3. Ingresa el valor y la unidad de origen.  
4. Selecciona la unidad destino.  
5. El sistema muestra el resultado convertido.

## CU-05: Analizar un circuito eléctrico básico

**Actor:** Estudiante de ingeniería 
**Descripcion:**El usuario ingresa los componentes de un circuito (resistencias, voltaje, corriente) y el sistema calcula magnitudes como resistencia equivalente, corriente total y caída de tensión, aplicando las leyes de Ohm y Kirchhoff.
**Flujo principal:** 
1. El usuario accede a la herramienta de ingeniería electrónica.  
2. Selecciona el tipo de circuito (serie, paralelo o mixto).  
3. Ingresa los valores de los componentes.  
4. El sistema calcula las magnitudes eléctricas correspondientes.  
5. El usuario visualiza los resultados y puede modificar los valores para nuevos análisis.

## CU-Geo-01: Calcular área de figura geométrica

Actor: Estudiante de ingeniería

Descripción: El usuario selecciona una figura geométrica del módulo de geometría, ingresa sus dimensiones y obtiene el área calculada de forma inmediata.

Precondición: El usuario tiene acceso al módulo de geometría y conoce las dimensiones de la figura a calcular.

Flujo principal:

1. El usuario accede al módulo de geometría.
2. Selecciona el tipo de figura (triángulo, círculo, rectángulo, trapecio, etc.).
3. Ingresa los valores de las dimensiones requeridas según la figura seleccionada.
4. El sistema valida que los valores ingresados sean numéricos y positivos.
5. El sistema calcula y muestra el área de la figura.
6. El usuario puede copiar el resultado o reingresar nuevos valores.

Flujo alternativo:

- A1 (valor inválido): Si el usuario ingresa un valor no numérico, negativo o igual a cero en algún campo, el sistema muestra un mensaje de error indicando el campo afectado y no realiza el cálculo hasta que el valor sea corregido.
- A2 (figura sin todos los parámetros): Si la figura seleccionada requiere un parámetro adicional (por ejemplo, un trapecio con dos bases distintas) y el usuario no lo ingresa, el sistema solicita el dato faltante antes de calcular.

Postcondición: El área de la figura geométrica es calculada y mostrada al usuario, con la posibilidad de reiniciar el cálculo con nuevos valores.

## CU-Elec-02: Analizar circuito resistivo simple

Actor: Estudiante de ingeniería

Descripción: El usuario ingresa los valores de un circuito resistivo (resistencias y fuente de tensión) configurado en serie o en paralelo, y el sistema calcula la resistencia equivalente, la corriente total y la caída de tensión en cada componente aplicando la ley de Ohm.

Precondición: El usuario tiene acceso al módulo eléctrico y conoce los valores de tensión de la fuente y de las resistencias del circuito.

Flujo principal:

1. El usuario accede al módulo eléctrico.
2. Selecciona la configuración del circuito (serie o paralelo).
3. Ingresa el valor de la tensión de la fuente.
4. Ingresa los valores de cada resistencia del circuito.
5. El sistema calcula la resistencia equivalente del circuito.
6. El sistema calcula la corriente total aplicando la ley de Ohm.
7. El sistema muestra la caída de tensión y la corriente en cada resistencia.

Flujo alternativo:

- A1 (resistencia con valor cero o negativo): Si el usuario ingresa una resistencia con valor cero o negativo, el sistema muestra un mensaje de error y no realiza el cálculo.
- A2 (circuito sin resistencias): Si el usuario intenta calcular sin haber ingresado al menos una resistencia, el sistema solicita agregar al menos un componente antes de continuar.

Postcondición: Las magnitudes eléctricas del circuito (resistencia equivalente, corriente total y caídas de tensión) son calculadas y mostradas al usuario.

## CU-Civ-03: Verificar momento máximo en viga

Actor: Estudiante de ingeniería / Docente

Descripción: El usuario ingresa los datos de una viga simplemente apoyada (longitud, tipo y magnitud de carga) y el sistema calcula el momento flector máximo a lo largo del elemento, indicando la posición donde ocurre.

Precondición: El usuario tiene acceso al módulo civil y conoce la longitud de la viga, así como el tipo y magnitud de la carga aplicada.

Flujo principal:

1. El usuario accede al módulo civil.
2. Selecciona la herramienta de análisis de vigas.
3. Ingresa la longitud de la viga.
4. Selecciona el tipo de carga (puntual, distribuida uniforme, etc.) y su magnitud.
5. El sistema calcula las reacciones en los apoyos.
6. El sistema calcula el momento flector máximo y la posición a lo largo de la viga donde se produce.
7. El sistema muestra el resultado, incluyendo el diagrama de momento flector.

Flujo alternativo:

- A1 (longitud no válida): Si el usuario ingresa una longitud igual o menor a cero, el sistema muestra un mensaje de error y no realiza el cálculo.
- A2 (carga fuera del rango de la viga): Si el usuario ingresa la posición de una carga puntual fuera de los límites de la longitud de la viga, el sistema solicita corregir la posición antes de continuar.

Postcondición: El momento flector máximo de la viga es calculado y mostrado junto con su posición, permitiendo al usuario verificar si la sección cumple con los requisitos de diseño.

## CU-Sis-01: Convertir número entre bases

Actor: Estudiante de ingeniería

Descripción: El usuario ingresa un número en una base numérica de origen (binaria, decimal, octal o hexadecimal) y el sistema lo convierte a la base destino seleccionada.

Precondición: El usuario tiene acceso al módulo de sistemas y conoce el número a convertir junto con su base de origen.

Flujo principal:

1. El usuario accede al módulo de sistemas.
2. Selecciona la herramienta de conversión entre bases.
3. Selecciona la base de origen (binaria, decimal, octal o hexadecimal).
4. Ingresa el número a convertir.
5. Selecciona la base destino.
6. El sistema valida que el número ingresado sea válido para la base de origen seleccionada.
7. El sistema realiza la conversión y muestra el resultado en la base destino.

Flujo alternativo:

- A1 (dígito no válido para la base): Si el usuario ingresa un dígito que no corresponde a la base de origen seleccionada (por ejemplo, un "2" en un número binario), el sistema muestra un mensaje de error indicando el dígito inválido.
- A2 (campo vacío): Si el usuario intenta convertir sin haber ingresado ningún número, el sistema solicita completar el campo antes de continuar.

Postcondición: El número es convertido correctamente a la base destino y mostrado al usuario, quien puede realizar una nueva conversión con otros valores o bases.
