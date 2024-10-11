import pytest
from src.calcular_area import CalcularArea
from src.medidas import Medida

@pytest.fixture
def calculo():
    raio = Medida(2,3)
    calculo = CalcularArea('area', raio)
    return calculo


def test_passar_valor_area_cirvunferencia(calculo):
    assert calculo.calcular_area() == 12.56

def test_passar_valor_volume(calculo):
    assert calculo.calcular_volume() == 37.68

'''
def test_passar_valor_area_cirvunferencia(calculo):
    raio = Medida(2,3)
    calcArea = CalcularArea('area', raio)
    assert calcArea.calcular_area() == 12.56

def test_passar_valor_volume():
    raio = Medida(2,3)
    calcArea = CalcularArea('area', raio)
    assert calcArea.calcular_volume() == 37.68
'''