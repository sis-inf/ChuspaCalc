from statistics import mean, median, stdev


def calcular_media(numeros: list[float]) -> float:
    if len(numeros) == 0:
        raise ValueError("La lista está vacía")

    resultado = mean(numeros)
    return float(resultado)

def calcular_mediana(numeros: list[float]) -> float:
    if len(numeros) == 0:
        raise ValueError("La lista está vacía")

    resultado = median(numeros)
    return float(resultado)

def calcular_desviacion_estandar(numeros: list[float]) -> float:
    if len(numeros) == 0:
        raise ValueError("La lista está vacía")

    resultado = stdev(numeros)
    return float(resultado)
