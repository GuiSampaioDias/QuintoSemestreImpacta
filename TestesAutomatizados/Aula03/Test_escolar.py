import pytest
from escolar import calcular_dosagem

def test1_typeValueerror():
    with pytest.raises(ValueError):
        calcular_dosagem(-1, 5)

def test2_typeValueerror():
    with pytest.raises(ValueError):
        calcular_dosagem(250, 5)

def test3_typeValueerror():
    with pytest.raises(ValueError):
        calcular_dosagem(1, -1)

def test4_typeValueerror():
    with pytest.raises(ValueError):
        calcular_dosagem(1, 250)

def test1_dosagem():
    assert calcular_dosagem(20,60) == 1000

def test2_dosagem():
    assert calcular_dosagem(12,60) == 1000

def test3_dosagem():
    assert calcular_dosagem(20,59) == 875

def test4_dosagem():
    assert calcular_dosagem(12, 59) == 875

def test5_dosagem():
    assert calcular_dosagem(1, 5) == 125

def test6_dosagem():
    assert calcular_dosagem(1, 9) == 125

def test7_dosagem():
    assert calcular_dosagem(2, 9.1) == 250

def test8_dosagem():
    assert calcular_dosagem(2, 16) == 250

def test9_dosagem():
    assert calcular_dosagem(3, 16.1) == 375

def test10_dosagem():
    assert calcular_dosagem(3, 24) == 375

def test11_dosagem():
    assert calcular_dosagem(4, 24.1) == 500

def test12_dosagem():
    assert calcular_dosagem(5, 30) == 500

def test13_dosagem():
    assert calcular_dosagem(6, 30.1) == 750