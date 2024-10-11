from verificar_qualificacao_empregado import verificar_qualificacao_empregado
import unittest

class TestarQualificacao(unittest.TestCase):
    def test_qualifica1(self):
        self.assertRaises(ValueError,verificar_qualificacao_empregado, 0, 10)

    def test_qualifica2(self):
        self.assertRaises(ValueError,verificar_qualificacao_empregado, 20, 0)

    def test_qualifica3(self):
        self.assertRaises(TypeError,verificar_qualificacao_empregado, '65', 30)

    def test_qualifica4(self):
        self.assertRaises(TypeError,verificar_qualificacao_empregado, 10, '30')

    def test_qualica5(self):
        self.assertEqual(verificar_qualificacao_empregado( 65, 20), 'Requerer aposentadoria')
    def test_qualica6(self):
        self.assertEqual(verificar_qualificacao_empregado( 59, 30), 'Requerer aposentadoria')
    def test_qualica7(self):
        self.assertEqual(verificar_qualificacao_empregado( 60, 25), 'Requerer aposentadoria')
    def test_qualica8(self):
        self.assertEqual(verificar_qualificacao_empregado( 59, 24), 'Não requerer')


if __name__ == '__main__':
    unittest.main
    