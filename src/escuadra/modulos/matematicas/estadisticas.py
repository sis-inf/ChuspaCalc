def calcular_media(datos: list) -> float:
    if not datos:
        raise ValueError("La lista no puede estar vacia")

    return float(sum(datos) / len(datos))


def calcular_mediana(datos: list) -> float:
    if not datos:
        raise ValueError("La lista no puede estar vacia")

    datos_ordenados = sorted(datos)
    n = len(datos_ordenados)
    mitad = n // 2

    if n % 2 == 0:
        return float((datos_ordenados[mitad - 1] + datos_ordenados[mitad]) / 2)

    return float(datos_ordenados[mitad])


def calcular_moda(datos: list) -> list:
    if not datos:
        raise ValueError("La lista no puede estar vacia")

    frecuencias = {}

    for valor in datos:
        frecuencias[valor] = frecuencias.get(valor, 0) + 1

    frecuencia_maxima = max(frecuencias.values())

    return [
        valor
        for valor, frecuencia in frecuencias.items()
        if frecuencia == frecuencia_maxima
    ]


def calcular_desviacion_estandar(datos: list, poblacional: bool = False) -> float:
    if not datos:
        raise ValueError("La lista no puede estar vacia")

    n = len(datos)

    if not poblacional and n < 2:
        raise ValueError("Se requieren al menos dos datos para la desviacion muestral")

    media = sum(datos) / n

    suma_cuadrados = 0

    for valor in datos:
        suma_cuadrados += (valor - media) ** 2

    divisor = n if poblacional else n - 1

    varianza = suma_cuadrados / divisor

    return float(varianza**0.5)
