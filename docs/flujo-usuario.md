---

## 4. Diagramas de flujo de usuario

Los siguientes diagramas muestran ejemplos de interacción entre el usuario y ChuspaCalc para distintos tipos de cálculos. Cada flujo incluye un camino exitoso y un posible escenario de error.

---

## Flujo 1: Cálculo de área de una figura

### Descripción

Este flujo representa el proceso que sigue un usuario para calcular el área de una figura geométrica utilizando las herramientas del módulo de Geometría.

### Diagrama de flujo

```text
        .-------.
       ( INICIO )
        '-------'
            |
            v
   .-------------------.
   | Seleccionar       |
   | cálculo de área   |
   '-------------------'
            |
            v
   .-------------------.
   | Ingresar          |
   | dimensiones       |
   '-------------------'
            |
            v
   .-------------------.
   | Validación        |
   | de datos          |
   '-------------------'
            |
            v
      .------------.
     / ¿Datos      /
    /  válidos?   /
   '------------'
      |        |
     Sí       No
      |        |
      v        v
 .-----------.   .-------------------.
 | Calcular  |   | Mostrar error     |
 | área      |   | y solicitar       |
 '-----------'   | corrección        |
      |          '-------------------'
      |                  |
      |<-----------------'
      |
      v
 .-----------.
 | Mostrar   |
 | resultado |
 '-----------'
      |
      v
   .-------.
  (  FIN  )
   '-------'
```

### Explicación de los pasos

1. El usuario selecciona la herramienta para calcular áreas.
2. Introduce las dimensiones requeridas por la figura.
3. El sistema verifica que los datos sean válidos.
4. Si los datos son correctos, se realiza el cálculo.
5. El resultado se presenta en pantalla.
6. Si existe un error, el sistema solicita corregir los datos antes de continuar.

---

## Flujo 2: Conversión de temperatura

### Descripción

Este flujo muestra el proceso utilizado para convertir temperaturas entre diferentes unidades soportadas por la aplicación.

### Diagrama de flujo

```text
        .-------.
       ( INICIO )
        '-------'
            |
            v
   .-------------------.
   | Seleccionar       |
   | conversor de      |
   | temperatura       |
   '-------------------'
            |
            v
   .-------------------.
   | Ingresar valor    |
   | y unidades        |
   '-------------------'
            |
            v
      .------------.
     / ¿Entrada    /
    /  válida?    /
   '------------'
      |        |
     Sí       No
      |        |
      v        v
 .-----------.   .-------------------.
 | Convertir |   | Mostrar error     |
 | valor     |   | y pedir corrección|
 '-----------'   '-------------------'
      |                  |
      |<-----------------'
      |
      v
 .-----------.
 | Mostrar   |
 | resultado |
 '-----------'
      |
      v
   .-------.
  (  FIN  )
   '-------'
```

### Explicación de los pasos

1. El usuario selecciona el conversor de temperatura.
2. Introduce el valor que desea convertir.
3. Selecciona la unidad de origen y la unidad de destino.
4. El sistema valida la información ingresada.
5. Si los datos son correctos, se ejecuta la conversión.
6. El resultado convertido se muestra al usuario.
7. En caso de error, el sistema solicita una nueva entrada.

---

## Flujo 3: Análisis de viga

### Descripción

Este flujo representa el uso de una herramienta del módulo Civil para analizar una viga y obtener resultados estructurales básicos.

### Diagrama de flujo

```text
        .-------.
       ( INICIO )
        '-------'
            |
            v
   .-------------------.
   | Seleccionar       |
   | análisis de viga  |
   '-------------------'
            |
            v
   .-------------------.
   | Ingresar cargas   |
   | y dimensiones     |
   '-------------------'
            |
            v
      .------------.
     / ¿Datos      /
    / correctos?  /
   '------------'
      |        |
     Sí       No
      |        |
      v        v
 .-----------.   .-------------------.
 | Ejecutar  |   | Mostrar error     |
 | cálculo   |   | y solicitar       |
 '-----------'   | corrección        |
      |          '-------------------'
      |                  |
      |<-----------------'
      |
      v
 .-----------.
 | Mostrar   |
 | resultado |
 '-----------'
      |
      v
   .-------.
  (  FIN  )
   '-------'
```

### Explicación de los pasos

1. El usuario selecciona una herramienta de análisis de vigas.
2. Introduce las dimensiones, apoyos y cargas requeridas.
3. El sistema valida que la información ingresada sea coherente.
4. Se ejecutan los cálculos estructurales correspondientes.
5. Los resultados se generan y se muestran en pantalla.
6. Si los datos contienen errores, el sistema informa el problema y solicita correcciones.

---

## Conclusión

Los flujos anteriores representan escenarios comunes de uso dentro de ChuspaCalc. En todos los casos, el sistema sigue una secuencia similar: recepción de datos, validación, procesamiento y presentación de resultados. La validación previa ayuda a reducir errores y mejora la experiencia del usuario durante la realización de cálculos.
