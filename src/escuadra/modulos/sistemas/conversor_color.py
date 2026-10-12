"""
Módulo conversor_color
Encargado de realizar conversiones de color entre los modelos RGB, HEX y HSL.
"""


def rgb_a_hex(r: int, g: int, b: int) -> str:
    """Convierte valores RGB (0-255) a su representación hexadecimal '#RRGGBB'."""
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise ValueError("Los valores r, g, b deben estar en el rango [0, 255]")

    return f"#{r:02X}{g:02X}{b:02X}"


def hex_a_rgb(hex_str: str) -> tuple:
    """Convierte un string hexadecimal (con o sin prefijo '#') a una tupla RGB (r, g, b)."""
    if hex_str.startswith("#"):
        hex_str = hex_str[1:]

    if len(hex_str) != 6:
        raise ValueError(
            "El formato hexadecimal debe contener exactamente 6 caracteres"
        )

    try:
        r = int(hex_str[0:2], 16)
        g = int(hex_str[2:4], 16)
        b = int(hex_str[4:6], 16)
    except ValueError:
        raise ValueError("El string contiene caracteres hexadecimales inválidos")

    return (r, g, b)


def rgb_a_hsl(r: int, g: int, b: int) -> tuple:
    """
    Convierte valores RGB (0-255) a HSL (h, s, l_pct).
    h está en el rango 0-360, s y l_pct están en el rango 0-100.
    """
    if not (0 <= r <= 255 and 0 <= g <= 255 and 0 <= b <= 255):
        raise ValueError("Los valores r, g, b deben estar en el rango [0, 255]")

    r_norm = r / 255.0
    g_norm = g / 255.0
    b_norm = b / 255.0

    max_val = max(r_norm, g_norm, b_norm)
    min_val = min(r_norm, g_norm, b_norm)
    delta = max_val - min_val

    l_calc = (max_val + min_val) / 2.0

    if delta == 0:
        s_calc = 0.0
    else:
        s_calc = delta / (1.0 - abs(2.0 * l_calc - 1.0))

    if delta == 0:
        h_calc = 0.0
    elif max_val == r_norm:
        h_calc = 60.0 * (((g_norm - b_norm) / delta) % 6)
    elif max_val == g_norm:
        h_calc = 60.0 * (((b_norm - r_norm) / delta) + 2)
    else:
        h_calc = 60.0 * (((r_norm - g_norm) / delta) + 4)

    h = round(h_calc) % 360
    s = round(s_calc * 100)
    l_pct = round(l_calc * 100)

    return (h, s, l_pct)
