import pytest
from src.medidas import Medida


def test_passar_valor_raio():
    raio = Medida(2,3)
    assert raio.get_raio()== 2

def test_passar_valor_altura():
    raio = Medida(2,3)
    assert raio.get_altura()== 3