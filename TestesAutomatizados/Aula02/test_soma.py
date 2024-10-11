import unittest
from soma import soma


class TesteDaSoma(unittest.TestCase):
    def test_funcao_soma(self):
        self.assertEqual(soma(10,5),15)

if __name__ == '__main__':
    unittest.main()
