#o arquivo de pyteste tem sempre que começar com Test_
import pytest
from triangulo import triangulo

def test_triangulo_typeError1():
    with pytest.raises(TypeError):
        triangulo(2, 5, '4')

def test_triangulo_typeError2():
    with pytest.raises(TypeError):
        triangulo(2, '4', 5 )

def test_triangulo_typeError3():
    with pytest.raises(TypeError):
        triangulo('4', 2, 5,)

def test_triangulo_escaleno():
    assert triangulo(2,4,5) == 'Triângulo Escaleno' 

def test_triangulo_isoceles():
    assert triangulo(4,4,5) == 'Triângulo Isóceles' 

def test_triangulo_equilatero():
    assert triangulo(4,4,4) == 'Triângulo Equilátero'

def test_triangulo_Nao():
    assert triangulo(0, 4, 4) == 'Não é um triângulo' 

