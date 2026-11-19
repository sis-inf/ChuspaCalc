import math

from chuspacalc.modulos.matematicas.error_validacion import ErrorValidacion


def _validar_coordenada(nombre: str, valor: float) -> None:
    """Exige una coordenada real, finita y representable como flotante."""
    try:
        if isinstance(valor, (int, float)) and not isinstance(valor, bool):
            if math.isfinite(valor):
                return
    except OverflowError:
        raise ErrorValidacion(f"{nombre} excede el rango numérico") from None
    raise ErrorValidacion(f"{nombre} debe ser un número real finito")


def _radio(*coordenadas: float) -> float:
    """Calcula un radio representable a partir de coordenadas ya validadas."""
    radio = math.hypot(*coordenadas)
    if not math.isfinite(radio):
        raise ErrorValidacion("El radio excede el rango numérico")
    return radio


def cartesiana_a_polar(x: float, y: float) -> dict[str, float]:
    """Convierte coordenadas cartesianas a radio y ángulo en grados y radianes."""
    _validar_coordenada("x", x)
    _validar_coordenada("y", y)
    r = _radio(x, y)
    theta_radianes = math.atan2(y, x) % math.tau
    theta_grados = round(math.degrees(theta_radianes), 2) % 360.0
    return {"r": r, "theta_grados": theta_grados, "theta_radianes": theta_radianes}


def polar_a_cartesiana(r: float, theta_grados: float) -> dict[str, float]:
    """Convierte coordenadas polares (r, theta_grados) a cartesianas (x, y)."""
    _validar_coordenada("r", r)
    _validar_coordenada("theta_grados", theta_grados)
    if r < 0:
        raise ErrorValidacion("r debe ser mayor o igual a cero")
    theta_radianes = math.radians(theta_grados)
    x = r * math.cos(theta_radianes)
    y = r * math.sin(theta_radianes)
    return {"x": round(x, 2), "y": round(y, 2)}


def cartesiana_a_cilindrica(x: float, y: float, z: float) -> dict[str, float]:
    """Convierte coordenadas cartesianas (x, y, z) a cilíndricas (r, theta_grados, z)."""
    _validar_coordenada("z", z)
    polar = cartesiana_a_polar(x, y)
    return {"r": polar["r"], "theta_grados": polar["theta_grados"], "z": round(z, 2)}


def cartesiana_a_esferica(x: float, y: float, z: float) -> dict[str, float]:
    """Convierte a radio, azimut, inclinación polar y elevación."""
    _validar_coordenada("z", z)
    polar = cartesiana_a_polar(x, y)
    rho = _radio(x, y, z)
    radio_horizontal = polar["r"]
    elevacion_radianes = math.atan2(z, radio_horizontal) if rho else 0.0
    phi_radianes = math.atan2(radio_horizontal, z) if rho else 0.0
    return {
        "rho": rho,
        "theta_grados": polar["theta_grados"],
        "phi_grados": round(math.degrees(phi_radianes), 2),
        "theta_radianes": polar["theta_radianes"],
        "phi_radianes": phi_radianes,
        "elevacion_grados": math.degrees(elevacion_radianes),
        "elevacion_radianes": elevacion_radianes,
    }
