"""
Pruebas para módulos de geometría:
- calculo_area.py
- perimetro.py
- volumen.py
"""

import pytest
import math

from escuadra.modulos.geometria.calculo_area import (
    area_triangulo,
    area_circulo,
    area_rectangulo,
)

from escuadra.modulos.geometria.perimetro import (
    perimetro_circulo,
    perimetro_cuadrado,
    perimetro_rectangulo,
    perimetro_triangulo,
    perimetro_hexagono_regular,
)

from escuadra.modulos.geometria.volumen import (
    volumen_cubo,
    volumen_esfera,
    volumen_cilindro,
    volumen_cono,
    volumen_paralelepipedo,
)


class TestCalculoArea:
    """Pruebas para el módulo calculo_area.py"""

    def test_area_triangulo(self):
        """Verifica el cálculo del área de un triángulo"""
        # Área = (base * altura) / 2
        resultado = area_triangulo(base=10, altura=5)
        assert resultado == 25.0

    def test_area_triangulo_2(self):
        """Verifica el cálculo con otros valores"""
        resultado = area_triangulo(base=7, altura=3)
        assert resultado == 10.5

    def test_area_circulo(self):
        """Verifica el cálculo del área de un círculo"""
        # Área = π * r² (usando 3.1416)
        resultado = area_circulo(radio=5)
        esperado = 3.1416 * 25
        assert resultado == esperado

    def test_area_circulo_2(self):
        """Verifica el cálculo con otro radio"""
        resultado = area_circulo(radio=3)
        esperado = 3.1416 * 9
        assert resultado == esperado

    def test_area_rectangulo(self):
        """Verifica el cálculo del área de un rectángulo"""
        # Área = base * altura
        resultado = area_rectangulo(base=8, altura=4)
        assert resultado == 32.0

    def test_area_rectangulo_2(self):
        """Verifica el cálculo con otros valores"""
        resultado = area_rectangulo(base=5.5, altura=2.5)
        assert resultado == 13.75


class TestPerimetro:
    """Pruebas para el módulo perimetro.py"""

    def test_perimetro_circulo(self):
        """Verifica el cálculo del perímetro (circunferencia) de un círculo"""
        # Perímetro = 2 * π * r
        resultado = perimetro_circulo(radio=5)
        esperado = 2 * math.pi * 5
        assert resultado == pytest.approx(esperado, rel=1e-6)

    def test_perimetro_circulo_radio_cero(self):
        """Verifica que radio cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            perimetro_circulo(radio=0)
        assert "mayor que cero" in str(excinfo.value)

    def test_perimetro_cuadrado(self):
        """Verifica el cálculo del perímetro de un cuadrado"""
        # Perímetro = 4 * lado
        resultado = perimetro_cuadrado(lado=6)
        assert resultado == 24.0

    def test_perimetro_cuadrado_lado_cero(self):
        """Verifica que lado cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            perimetro_cuadrado(lado=0)
        assert "mayor que cero" in str(excinfo.value)

    def test_perimetro_rectangulo(self):
        """Verifica el cálculo del perímetro de un rectángulo"""
        # Perímetro = 2 * (largo + ancho)
        resultado = perimetro_rectangulo(largo=8, ancho=4)
        assert resultado == 24.0

    def test_perimetro_rectangulo_largo_cero(self):
        """Verifica que largo cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            perimetro_rectangulo(largo=0, ancho=4)
        assert "mayores que cero" in str(excinfo.value)

    def test_perimetro_triangulo(self):
        """Verifica el cálculo del perímetro de un triángulo"""
        # Perímetro = a + b + c
        resultado = perimetro_triangulo(a=3, b=4, c=5)
        assert resultado == 12.0

    def test_perimetro_triangulo_lado_cero(self):
        """Verifica que lado cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            perimetro_triangulo(a=0, b=4, c=5)
        assert "mayores que cero" in str(excinfo.value)

    def test_perimetro_triangulo_desigualdad(self):
        """Verifica que violación de desigualdad triangular lanza error"""
        with pytest.raises(ValueError) as excinfo:
            perimetro_triangulo(a=1, b=1, c=3)
        assert "desigualdad triangular" in str(excinfo.value)

    def test_perimetro_hexagono_regular(self):
        """Verifica el cálculo del perímetro de un hexágono regular"""
        # Perímetro = 6 * lado
        resultado = perimetro_hexagono_regular(lado=5)
        assert resultado == 30.0

    def test_perimetro_hexagono_lado_cero(self):
        """Verifica que lado cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            perimetro_hexagono_regular(lado=0)
        assert "mayor que cero" in str(excinfo.value)


class TestVolumen:
    """Pruebas para el módulo volumen.py"""

    def test_volumen_cubo(self):
        """Verifica el cálculo del volumen de un cubo"""
        # Volumen = lado³
        resultado = volumen_cubo(lado=3)
        assert resultado == 27.0

    def test_volumen_cubo_lado_cero(self):
        """Verifica que lado cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            volumen_cubo(lado=0)
        assert "mayor que 0" in str(excinfo.value)

    def test_volumen_esfera(self):
        """Verifica el cálculo del volumen de una esfera"""
        # Volumen = (4/3) * π * r³
        resultado = volumen_esfera(radio=3)
        esperado = (4 / 3) * math.pi * 27
        assert resultado == pytest.approx(esperado, rel=1e-6)

    def test_volumen_esfera_radio_cero(self):
        """Verifica que radio cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            volumen_esfera(radio=0)
        assert "mayor que 0" in str(excinfo.value)

    def test_volumen_cilindro(self):
        """Verifica el cálculo del volumen de un cilindro"""
        # Volumen = π * r² * altura
        resultado = volumen_cilindro(radio=3, altura=5)
        esperado = math.pi * 9 * 5
        assert resultado == pytest.approx(esperado, rel=1e-6)

    def test_volumen_cilindro_radio_cero(self):
        """Verifica que radio cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            volumen_cilindro(radio=0, altura=5)
        assert "dimensiones" in str(excinfo.value)

    def test_volumen_cilindro_altura_cero(self):
        """Verifica que altura cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            volumen_cilindro(radio=3, altura=0)
        assert "dimensiones" in str(excinfo.value)

    def test_volumen_cono(self):
        """Verifica el cálculo del volumen de un cono"""
        # Volumen = (1/3) * π * r² * altura
        resultado = volumen_cono(radio=3, altura=5)
        esperado = (1 / 3) * math.pi * 9 * 5
        assert resultado == pytest.approx(esperado, rel=1e-6)

    def test_volumen_cono_radio_cero(self):
        """Verifica que radio cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            volumen_cono(radio=0, altura=5)
        assert "dimensiones" in str(excinfo.value)

    def test_volumen_paralelepipedo(self):
        """Verifica el cálculo del volumen de un paralelepípedo"""
        # Volumen = largo * ancho * alto
        resultado = volumen_paralelepipedo(largo=5, ancho=3, alto=4)
        assert resultado == 60.0

    def test_volumen_paralelepipedo_largo_cero(self):
        """Verifica que largo cero lanza error"""
        with pytest.raises(ValueError) as excinfo:
            volumen_paralelepipedo(largo=0, ancho=3, alto=4)
        assert "dimensiones" in str(excinfo.value)
