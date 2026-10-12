import math


def cartesiana_a_polar(x, y):
    """Convierte coordenadas cartesianas (x, y) a polares (r, theta_grados)."""
    r = math.sqrt(x**2 + y**2)
    theta_radianes = math.atan2(y, x)
    theta_grados = math.degrees(theta_radianes)
    if theta_grados < 0:
        theta_grados += 360.0
    if x == 0 and y == 0:
        theta_grados = 0.0
    return {"r": round(r, 2), "theta_grados": round(theta_grados, 2)}


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
    rho = math.sqrt(x**2 + y**2 + z**2)
    polar = cartesiana_a_polar(x, y)
    theta_grados = polar["theta_grados"]
    if rho == 0:
        phi_grados = 0.0
    else:
        phi_radianes = math.acos(z / rho)
        phi_grados = math.degrees(phi_radianes)
    return {
        "rho": round(rho, 2),
        "theta_grados": theta_grados,
        "phi_grados": round(phi_grados, 2),
    }
