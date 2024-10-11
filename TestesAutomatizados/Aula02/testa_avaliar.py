from avaliar_notas import avaliar_notas
import unittest

class TestNotas(unittest.TestCase):
    def test_media1(self):
        self.assertRaises(ValueError, avaliar_notas, -1, 0, 0, 0)

    def test_media2(self):
        self.assertRaises(ValueError, avaliar_notas, 0, -1, 0, 0)

    def test_media3(self):
        self.assertRaises(ValueError, avaliar_notas, 0, 0, -1, 0)
    def test_media4(self):
        self.assertEqual(avaliar_notas( 10, 10, 10, 10), 'A')
    def test_media5(self):
        self.assertEqual(avaliar_notas( 9, 9, 9, 9),'A')
    def test_media6(self):
        self.assertEqual(avaliar_notas( 8.9, 8.9, 8.9,8.9), 'B')
    def test_media7(self):
        self.assertEqual(avaliar_notas( 7.5, 7.5, 7.5, 7.5),'B')
    def test_media8(self):
        self.assertEqual(avaliar_notas( 7.4, 7.4, 7.4, 7.4),'C')
    def test_media9(self):
        self.assertEqual(avaliar_notas( 6, 6, 6, 6),'C')
    def test_media10(self):
        self.assertEqual(avaliar_notas( 5.9, 5.9, 5.9, 5.9),'D')
    def test_media11(self):
        self.assertEqual(avaliar_notas( 0, 0, 0, 0),'D')


if __name__ == '__main__':
    unittest.main