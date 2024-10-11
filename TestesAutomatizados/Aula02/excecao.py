import unittest

def soma(a, b):
    if type(a) == int and type(b) == int:
        return a + b
    else:
        raise TypeError(f'Tipo incompatíveo')
    
class TesteSoma(unittest.TestCase):
    def test_funcao_soma(self):
        self.assertEqual(soma(15, 4), 19)

    def test_excecao_incompativel(self):
        self.assertRaises(TypeError, soma, 10, 'jj')

    def test_excecao_tipo_float(self):
        self.assertRaises(TypeError, soma, 10.3, 5, 15.3)

    def test_excecao_tipo_boolean(self):
        self.assertRaises(TypeError, soma, True, False)

if __name__ == '__main__':
    unittest.main