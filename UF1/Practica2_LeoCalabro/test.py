import unittest
from Practica import SolucionadorEcuacions


class TestEquacio(unittest.TestCase):

    def test_positiu(self):
        eq = SolucionadorEcuacions("2x + 3 = 7")
        self.assertEqual(eq.calcula(),2)

    def testincorrecte(self):
        eq = SolucionadorEcuacions("2x / 3 = 7")
        self.assertEqual(eq.calcula(),"Operador no valid: "+eq.operador)
        self.assertIsInstance(eq.operador, basestring)

    def test_negatiu(self):
        eq = SolucionadorEcuacions("2x - 3 = 7")
        self.assertEqual(eq.calcula(),5)

    def test_float(self):
        eq = SolucionadorEcuacions("2.3x - 8.4 = 9.8")
        self.assertEqual(eq.calcula(),7.913043478260872)

    def test_caracterErroni(self):
        eq = SolucionadorEcuacions("2x - p = 7")
        self.assertEqual(eq.calcula(),"l'equacio conte caracter no calculables: "+eq.c)

    def test_fromat_erroni(self):
        eq = SolucionadorEcuacions("3 - 2x = 7")
        self.assertEqual(eq.calcula(),"l'equacio no segueix el format: ax + b = c")



if __name__ == '__main__':
    unittest.main()
