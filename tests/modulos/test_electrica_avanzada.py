"""
Pruebas para módulos eléctricos avanzados:
- caida_tension.py
- circuito_serie_paralelo.py
"""

import pytest

from escuadra.modulos.electrica.caida_tension import (
    calcular_caida,
    RESISTIVIDADES,
    TENSION_REFERENCIA_V,
    PORCENTAJE_ADMISIBLE,
)

from escuadra.modulos.electrica.circuito_serie_paralelo import (
    resistencia_serie,
    resistencia_paralelo,
)


class TestCaidaTension:
    """Pruebas para el módulo caida_tension.py"""

    def test_calcular_caida_cobre(self):
        """Verifica el cálculo de caída de tensión con cobre"""
        # Fórmula: DV = 2 * 0.0172 * 100 * 15 / 4 = 12.9V
        resultado = calcular_caida(
            longitud=100, corriente=15, seccion=4, material="cobre"
        )

        assert resultado["caida_v"] == 12.9
        assert resultado["porcentaje"] == pytest.approx(5.8636, rel=1e-4)
        assert resultado["admisible"] is False

    def test_calcular_caida_aluminio(self):
        """Verifica el cálculo de caída de tensión con aluminio"""
        # Fórmula: DV = 2 * 0.0282 * 100 * 15 / 4 = 21.15V
        resultado = calcular_caida(
            longitud=100, corriente=15, seccion=4, material="aluminio"
        )

        assert resultado["caida_v"] == 21.15
        assert resultado["porcentaje"] == pytest.approx(9.6136, rel=1e-4)
        assert resultado["admisible"] is False

    def test_calcular_caida_admisible(self):
        """Verifica que detecta caída admisible (<= 3%)"""
        # Con longitud pequeña, caída será menor al 3%
        resultado = calcular_caida(
            longitud=10, corriente=5, seccion=10, material="cobre"
        )

        assert resultado["admisible"] is True

    def test_calcular_caida_longitud_cero(self):
        """Verifica que longitud cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            calcular_caida(longitud=0, corriente=15, seccion=4)
        assert "positivo" in str(excinfo.value)

    def test_calcular_caida_corriente_cero(self):
        """Verifica que corriente cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            calcular_caida(longitud=100, corriente=0, seccion=4)
        assert "positivo" in str(excinfo.value)

    def test_calcular_caida_seccion_cero(self):
        """Verifica que sección cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            calcular_caida(longitud=100, corriente=15, seccion=0)
        assert "positivo" in str(excinfo.value)

    def test_calcular_caida_material_invalido(self):
        """Verifica que material inválido lanza error"""
        with pytest.raises(ValueError) as excinfo:
            calcular_caida(longitud=100, corriente=15, seccion=4, material="plomo")
        assert "no reconocido" in str(excinfo.value)

    def test_resistividades(self):
        """Verifica que las resistividades están definidas correctamente"""
        assert RESISTIVIDADES["cobre"] == 0.0172
        assert RESISTIVIDADES["aluminio"] == 0.0282

    def test_tension_referencia(self):
        """Verifica que la tensión de referencia es 220V"""
        assert TENSION_REFERENCIA_V == 220.0

    def test_porcentaje_admisible(self):
        """Verifica que el porcentaje admisible es 3%"""
        assert PORCENTAJE_ADMISIBLE == 3.0


class TestCircuitoSerieParalelo:
    """Pruebas para el módulo circuito_serie_paralelo.py"""

    def test_resistencia_serie_dos(self):
        """Verifica el cálculo de resistencia equivalente en serie con 2 resistencias"""
        resultado = resistencia_serie(10, 20)
        assert resultado == 30.0

    def test_resistencia_serie_tres(self):
        """Verifica el cálculo de resistencia equivalente en serie con 3 resistencias"""
        resultado = resistencia_serie(10, 20, 30)
        assert resultado == 60.0

    def test_resistencia_serie_cuatro(self):
        """Verifica el cálculo de resistencia equivalente en serie con 4 resistencias"""
        resultado = resistencia_serie(10, 20, 30, 40)
        assert resultado == 100.0

    def test_resistencia_paralelo_dos(self):
        """Verifica el cálculo de resistencia equivalente en paralelo con 2 resistencias"""
        resultado = resistencia_paralelo(10, 10)
        assert resultado == 5.0

    def test_resistencia_paralelo_tres(self):
        """Verifica el cálculo de resistencia equivalente en paralelo con 3 resistencias"""
        resultado = resistencia_paralelo(10, 20, 30)
        # 1/10 + 1/20 + 1/30 = 0.18333 → 1/0.18333 = 5.4545
        assert resultado == pytest.approx(5.45454545, rel=1e-4)

    def test_resistencia_serie_error_una_resistencia(self):
        """Verifica que menos de 2 resistencias lanza error en serie"""
        with pytest.raises(ValueError) as excinfo:
            resistencia_serie(10)
        assert "al menos 2" in str(excinfo.value)

    def test_resistencia_paralelo_error_una_resistencia(self):
        """Verifica que menos de 2 resistencias lanza error en paralelo"""
        with pytest.raises(ValueError) as excinfo:
            resistencia_paralelo(10)
        assert "al menos 2" in str(excinfo.value)

    def test_resistencia_serie_error_resistencia_cero(self):
        """Verifica que resistencia cero lanza error en serie"""
        with pytest.raises(ValueError) as excinfo:
            resistencia_serie(10, 0, 20)
        assert "mayores que 0" in str(excinfo.value)

    def test_resistencia_paralelo_error_resistencia_cero(self):
        """Verifica que resistencia cero lanza error en paralelo"""
        with pytest.raises(ValueError) as excinfo:
            resistencia_paralelo(10, 0, 20)
        assert "mayores que 0" in str(excinfo.value)

    def test_resistencia_serie_error_resistencia_negativa(self):
        """Verifica que resistencia negativa lanza error en serie"""
        with pytest.raises(ValueError) as excinfo:
            resistencia_serie(10, -5, 20)
        assert "mayores que 0" in str(excinfo.value)

    def test_resistencia_paralelo_error_resistencia_negativa(self):
        """Verifica que resistencia negativa lanza error en paralelo"""
        with pytest.raises(ValueError) as excinfo:
            resistencia_paralelo(10, -5, 20)
        assert "mayores que 0" in str(excinfo.value)
