from peso import obter_peso_ideal
import pytest

def test1():
    assert obter_peso_ideal(1.5, 'M') ==  pytest.approx(51.05, rel=1e-2)

def test2():
    assert obter_peso_ideal(1.5, 'F') ==  pytest.approx(48.45, rel=1e-2)

def test3():
    assert obter_peso_ideal(1.6, 'M') ==  pytest.approx(58.32, rel=1e-2)

def test4():
    assert obter_peso_ideal(1.6, 'F') ==  pytest.approx(54.66, rel=1e-2)

def test5():
    assert obter_peso_ideal(1.7, 'M') ==  pytest.approx(65.59, rel=1e-2)

def test6():
    assert obter_peso_ideal(1.7, 'F') ==  pytest.approx(60.86, rel=1e-2)

def test7():
    assert obter_peso_ideal(1.8, 'M') ==  pytest.approx(72.86, rel=1e-2)

def test8():
    assert obter_peso_ideal(1.8, 'F') ==  pytest.approx(67.08, rel=1e-2)

def test9():
    assert obter_peso_ideal(1.9, 'M') ==  pytest.approx(80.13, rel=1e-2)

def test10():
    assert obter_peso_ideal(1.9, 'F') ==  pytest.approx(73.28, rel=1e-2)

def test11():
    assert obter_peso_ideal(2.0, 'M') ==  pytest.approx(87.4, rel=1e-2)

def test12():
    assert obter_peso_ideal(2.0, 'F') ==  pytest.approx(79.5, rel=1e-2)