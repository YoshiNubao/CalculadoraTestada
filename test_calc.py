import unittest
from calculadora import Calculadora

class Test(unittest.TestCase):
    def test_multiplicacao(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.calcular(6,2, "*"),12)
        self.assertEqual(calculadora.calcular(-5,2, "*"),-10)
        self.assertEqual(calculadora.calcular(6,-1, "*"),-6)
        self.assertEqual(calculadora.calcular(1, 5, "*"),5)

    def test_divisao(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.calcular(6,2, "/"),3)
        self.assertEqual(calculadora.calcular(3,6, "/"),0.5)
        self.assertEqual(calculadora.calcular(2,0, "/"),None)
        self.assertEqual(calculadora.calcular(2,1,"/"),2)

    def test_subtracao(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.calcular(2,5, "-"),-3)
        self.assertEqual(calculadora.calcular(5,2, "-"),3)
        self.assertEqual(calculadora.calcular(2,2, "-"),0)
        self.assertEqual(calculadora.calcular(2,0, "-"),2)

    def test_soma(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.calcular(100,5, "+"),105)
        self.assertEqual(calculadora.calcular(-5,2, "+"),-3)
        self.assertEqual(calculadora.calcular(-2,2, "+"),0)
        self.assertEqual(calculadora.calcular(2,0, "+"),2)

    def test_potencia(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.calcular(2,1, "^"),2)
        self.assertEqual(calculadora.calcular(2,-2, "^"),0.25)
        self.assertEqual(calculadora.calcular(4,0.5, "^"),2)
        self.assertEqual(calculadora.calcular(2,0, "^"),1)
        self.assertEqual(calculadora.calcular(2,2, "^"),4)

    def test_invalid_op(self):
        calculadora = Calculadora()
        self.assertEqual(calculadora.calcular(1,1,"a"), None)

if __name__ == '__main__':
    unittest.main()