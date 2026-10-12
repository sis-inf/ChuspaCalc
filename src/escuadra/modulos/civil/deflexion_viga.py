def calcular_deflexion_max(
    longitud,
    carga,
    modulo_elasticidad,
    inercia,
    tipo_carga="puntual_central",
):
    """
    Calcula la deflexión máxima de una viga simplemente apoyada.

    Para carga puntual central:
        δ = P * L³ / (48 * E * I)

    Para carga distribuida:
        δ = 5 * w * L⁴ / (384 * E * I)

    Retorna un diccionario con:
    - deflexion_max (mm)
    - posicion (m)
    """

    parametros = [
        longitud,
        carga,
        modulo_elasticidad,
        inercia,
    ]

    if any(p <= 0 for p in parametros):
        raise ValueError("Todos los parámetros deben ser mayores que 0")

    if tipo_carga == "puntual_central":
        delta = (carga * longitud**3) / (48 * modulo_elasticidad * inercia)

    elif tipo_carga == "distribuida":
        delta = (5 * carga * longitud**4) / (384 * modulo_elasticidad * inercia)

    else:
        raise ValueError("Tipo de carga inválido")

    return {
        "deflexion_max": delta * 1000,
        "posicion": longitud / 2,
    }
