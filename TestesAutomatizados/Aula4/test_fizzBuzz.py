import pytest
from fizzBuzz import fizBuzz


@pytest.fixture
def val1():
    return fizBuzz(1)
@pytest.fixture
def val2():
    return fizBuzz(2)
@pytest.fixture
def val3():
    return fizBuzz(3)
@pytest.fixture
def val4():
    return fizBuzz(4)
@pytest.fixture
def val5():
    return fizBuzz(5)
@pytest.fixture
def val6():
    return fizBuzz(6)
@pytest.fixture
def val7():
    return fizBuzz(7)
@pytest.fixture
def val8():
    return fizBuzz(8)
@pytest.fixture
def val9():
    return fizBuzz(9)
@pytest.fixture
def val10():
    return fizBuzz(10)
@pytest.fixture
def val11():
    return fizBuzz(11)
@pytest.fixture
def val12():
    return fizBuzz(12)
@pytest.fixture
def val13():
    return fizBuzz(13)
@pytest.fixture
def val14():
    return fizBuzz(14)
@pytest.fixture
def val15():
    return fizBuzz(15)
@pytest.fixture
def val16():
    return fizBuzz(16)
@pytest.fixture
def val17():
    return fizBuzz(17)
@pytest.fixture
def val18():
    return fizBuzz(18)
@pytest.fixture
def val19():
    return fizBuzz(19)
@pytest.fixture
def val20():
    return fizBuzz(20)




def test1(val1):
    assert val1 == 1

def test2(val2):
    assert val2 == 2

def test3(val3):
    assert val3 == 'Fizz'

def test4(val4):
    assert val4 == 4

def test5(val5):
    assert val5 == 'Buzz'

def test6(val6):
    assert val6 == 'Fizz'

def test7(val7):
    assert val7 == 7

def test8(val8):
    assert val8 == 8

def test9(val9):
    assert val9 == 'Fizz'

def test10(val10):
    assert val10 == 'Buzz'

def test11(val11):
    assert val11 == 11

def test12(val12):
    assert val12 == 'Fizz'

def test13(val13):
    assert val13 == 13

def test14(val14):
    assert val14 == 14

def test15(val15):
    assert val15 == 'FizzBuzz'

def test16(val16):
    assert val16 == 16

def test17(val17):
    assert val17 == 17

def test18(val18):
    assert val18 == 'Fizz'

def test19(val19):
    assert val19 == 19

def test20(val20):
    assert val20 == 'Buzz'
