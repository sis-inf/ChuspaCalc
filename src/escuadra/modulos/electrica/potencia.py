def potencia_vi(voltaje, corriente) -> float:
    """
    Calcula la potencia eléctrica usando la fórmula P = V·I.

    Fórmula:
        P = V·I

    Unidades:
        - V: voltaje en Volts (V)
        - I: corriente en Amperes (A)
        - P: potencia en Watts (W)
    """
    if voltaje <= 0:
        raise ValueError("voltaje debe ser mayor que 0")

    if corriente <= 0:
        raise ValueError("corriente debe ser mayor que 0")

    return float(voltaje * corriente)


def potencia_ir(corriente, resistencia) -> float:
    """
    Calcula la potencia eléctrica usando la fórmula P = I²·R.

    Fórmula:
        P = I²·R

    Unidades:
        - I: corriente en Amperes (A)
        - R: resistencia en Ohms (Ω)
        - P: potencia en Watts (W)
    """
    if corriente <= 0:
        raise ValueError("corriente debe ser mayor que 0")

    if resistencia <= 0:
        raise ValueError("resistencia debe ser mayor que 0")

    return float((corriente**2) * resistencia)


def potencia_vr(voltaje, resistencia) -> float:
    """
    Calcula la potencia eléctrica usando la fórmula P = V²/R.

    Fórmula:
        P = V²/R

    Unidades:
        - V: voltaje en Volts (V)
        - R: resistencia en Ohms (Ω)
        - P: potencia en Watts (W)
    """
    if voltaje <= 0:
        raise ValueError("voltaje debe ser mayor que 0")

    if resistencia <= 0:
        raise ValueError("resistencia debe ser mayor que 0")

    return float((voltaje**2) / resistencia)
