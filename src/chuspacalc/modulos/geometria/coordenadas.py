import math


def cartesiana_a_polar(x, y):
    """Convierte coordenadas cartesianas (x, y) a polares (r, theta_grados)."""
    r = math.hypot(x, y)
    theta_radianes = math.atan2(y, x) % math.tau
    theta_grados = round(math.degrees(theta_radianes), 2) % 360.0
    return {"r": r, "theta_grados": theta_grados, "theta_radianes": theta_radianes}


def polar_a_cartesiana(r, theta_grados):
    """Convierte coordenadas polares (r, theta_grados) a cartesianas (x, y)."""
    theta_radianes = math.radians(theta_grados)
    x = r * math.cos(theta_radianes)
    y = r * math.sin(theta_radianes)
    return {"x": round(x, 2), "y": round(y, 2)}


def cartesiana_a_cilindrica(x, y, z):
    """Convierte coordenadas cartesianas (x, y, z) a cilíndricas (r, theta_grados, z)."""
    polar = cartesiana_a_polar(x, y)
    return {"r": polar["r"], "theta_grados": polar["theta_grados"], "z": round(z, 2)}


def cartesiana_a_esferica(x, y, z):
    """Convierte coordenadas cartesianas (x, y, z) a esféricas (rho, theta_grados, phi_grados)."""
    rho = math.hypot(x, y, z)
    polar = cartesiana_a_polar(x, y)
    radio_horizontal = math.hypot(x, y)
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
