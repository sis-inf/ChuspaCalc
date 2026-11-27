# Documentación de API

## Base URL

http://localhost:5000

---

## Endpoints

### GET /

**Descripción:** Endpoint raíz para verificar que la API está en funcionamiento.
**Parámetros:** Ninguno
**Respuesta:**

```json
{
  "mensaje": "API ChuspaCalc en funcionamiento"
}
```

---

## Módulo Mecánica

### GET /api/mecanica/fuerza

**Descripción:** Calcula la fuerza utilizando la segunda ley de Newton.
**Parámetros:**

* masa (float)
* aceleracion (float)

**Respuesta:**

```json
{
  "fuerza": 20
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/mecanica/fuerza?masa=10&aceleracion=2"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/mecanica/fuerza", params={"masa": 10, "aceleracion": 2})
# retorna: {"fuerza": 20}
```

---

### GET /api/mecanica/trabajo

**Descripción:** Calcula el trabajo realizado.
**Parámetros:**

* fuerza (float)
* distancia (float)

**Respuesta:**

```json
{
  "trabajo": 100
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/mecanica/trabajo?fuerza=10&distancia=10"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/mecanica/trabajo", params={"fuerza": 10, "distancia": 10})
# retorna: {"trabajo": 100}
```

---

### GET /api/mecanica/velocidad

**Descripción:** Calcula la velocidad.
**Parámetros:**

* distancia (float)
* tiempo (float)

**Respuesta:**

```json
{
  "velocidad": 20
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/mecanica/velocidad?distancia=100&tiempo=5"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/mecanica/velocidad", params={"distancia": 100, "tiempo": 5})
# retorna: {"velocidad": 20}
```

---

## Módulo Sistemas

### GET /api/sistemas/binario

**Descripción:** Convierte un número decimal a binario.
**Parámetros:**

* numero (int)

**Respuesta:**

```json
{
  "binario": "1010"
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/sistemas/binario?numero=10"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/sistemas/binario", params={"numero": 10})
# retorna: {"binario": "1010"}
```

---

### GET /api/sistemas/ordenar

**Descripción:** Ordena una lista de números.
**Parámetros:**

* lista (array)

**Respuesta:**

```json
{
  "ordenado": [1,2,3,4]
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/sistemas/ordenar?lista=4,2,3,1"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/sistemas/ordenar", params={"lista": "4,2,3,1"})
# retorna: {"ordenado": [1,2,3,4]}
```

---

### GET /api/sistemas/buscar

**Descripción:** Busca un elemento en una lista.
**Parámetros:**

* lista (array)
* objetivo (int)

**Respuesta:**

```json
{
  "encontrado": true
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/sistemas/buscar?lista=1,2,3,4&objetivo=3"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/sistemas/buscar", params={"lista": "1,2,3,4", "objetivo": 3})
# retorna: {"encontrado": true}
```

---

## Módulo Industrial

### GET /api/industrial/productividad

**Descripción:** Calcula la productividad.
**Parámetros:**

* produccion (float)
* recursos (float)

**Respuesta:**

```json
{
  "productividad": 2.5
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/industrial/productividad?produccion=100&recursos=40"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/industrial/productividad", params={"produccion": 100, "recursos": 40})
# retorna: {"productividad": 2.5}
```

---

### GET /api/industrial/eficiencia

**Descripción:** Calcula la eficiencia en porcentaje.
**Parámetros:**

* salida (float)
* entrada (float)

**Respuesta:**

```json
{
  "eficiencia": 80
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/industrial/eficiencia?salida=80&entrada=100"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/industrial/eficiencia", params={"salida": 80, "entrada": 100})
# retorna: {"eficiencia": 80}
```

---

### GET /api/industrial/tiempo_produccion

**Descripción:** Calcula el tiempo de producción total.
**Parámetros:**

* unidades (int)
* tiempo_unitario (float)

**Respuesta:**

```json
{
  "tiempo_total": 200
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/industrial/tiempo_produccion?unidades=100&tiempo_unitario=2"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/industrial/tiempo_produccion", params={"unidades": 100, "tiempo_unitario": 2})
# retorna: {"tiempo_total": 200}
```

---

## Módulo Civil

### GET /api/civil/area_rectangulo

**Descripción:** Calcula el área de un rectángulo.
**Parámetros:**

* base (float)
* altura (float)

**Respuesta:**

```json
{
  "area": 50
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/civil/area_rectangulo?base=10&altura=5"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/civil/area_rectangulo", params={"base": 10, "altura": 5})
# retorna: {"area": 50}
```

---

### GET /api/civil/volumen_concreto

**Descripción:** Calcula volumen de concreto.
**Parámetros:**

* largo (float)
* ancho (float)
* alto (float)

**Respuesta:**

```json
{
  "volumen": 100
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/civil/volumen_concreto?largo=10&ancho=5&alto=2"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/civil/volumen_concreto", params={"largo": 10, "ancho": 5, "alto": 2})
# retorna: {"volumen": 100}
```

---

### GET /api/civil/resistencia

**Descripción:** Calcula la resistencia de un material.
**Parámetros:**

* carga (float)
* area (float)

**Respuesta:**

```json
{
  "resistencia": 25
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/civil/resistencia?carga=100&area=4"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/civil/resistencia", params={"carga": 100, "area": 4})
# retorna: {"resistencia": 25}
```

---

## Módulo Eléctrica

### GET /api/electrica/ohm

**Descripción:** Calcula la corriente usando la ley de Ohm.
**Parámetros:**

* voltaje (float)
* resistencia (float)

**Respuesta:**

```json
{
  "corriente": 2
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/electrica/ohm?voltaje=10&resistencia=5"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/electrica/ohm", params={"voltaje": 10, "resistencia": 5})
# retorna: {"corriente": 2}
```

---

### GET /api/electrica/potencia

**Descripción:** Calcula la potencia eléctrica.
**Parámetros:**

* voltaje (float)
* corriente (float)

**Respuesta:**

```json
{
  "potencia": 50
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/electrica/potencia?voltaje=10&corriente=5"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/electrica/potencia", params={"voltaje": 10, "corriente": 5})
# retorna: {"potencia": 50}
```

---

### GET /api/electrica/resistencia

**Descripción:** Calcula la resistencia.
**Parámetros:**

* voltaje (float)
* corriente (float)

**Respuesta:**

```json
{
  "resistencia": 2
}
```

**Ejemplo:**

```bash
curl "http://localhost:5000/api/electrica/resistencia?voltaje=10&corriente=5"
```

**Ejemplo en Python:**

```py
import requests

response = requests.get("http://localhost:5000/api/electrica/resistencia", params={"voltaje": 10, "corriente": 5})
# retorna: {"resistencia": 2}
```

---

## Códigos de error

| Código | Descripción           |
| ------ | --------------------- |
| 200    | OK                    |
| 400    | Bad Request           |
| 500    | Internal Server Error |