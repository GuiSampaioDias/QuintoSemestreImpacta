import pytest
from trapezio import calcular_area_trapezio

def test1_typeVAluerror():
    with pytest.raises(ValueError):
        calcular_area_trapezio(0,1,3)

def test2_typeVAluerror():
    with pytest.raises(ValueError):
        calcular_area_trapezio(2,0,3)

def test3_typeVAluerror():
    with pytest.raises(ValueError):
        calcular_area_trapezio(1,3,-3)

def test4_typeVAluerror():
    with pytest.raises(TypeError):
        calcular_area_trapezio("5",1,3)

def test5_typeVAluerror():
    with pytest.raises(TypeError):
        calcular_area_trapezio(2,'1',3)

def test6_typeVAluerror():
    with pytest.raises(TypeError):
        calcular_area_trapezio(1,3,'4')

def test7_area_trapezio():
    assert calcular_area_trapezio(7, 3, 4) == 20

def test8_area_trapezio():
    assert calcular_area_trapezio(6, 4, 4) == 20

def test9_area_trapezio():
    assert calcular_area_trapezio(8, 6, 4) == 28