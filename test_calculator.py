import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(4,5), 9)
    
    def test_subtract(self):
        self.assertEqual(self.calc.subtract(5,1), 4)
        self.assertEqual(self.calc.subtract(10,3), 7)

    def test_multiply(self):
        self.assertEqual(self.calc.multiply(3,2), 6)
        self.assertEqual(self.calc.multiply(6,5), 30)

    def test_divide(self):
        self.assertEqual(self.calc.divide(8,4), 2)
        self.assertEqual(self.calc.divide(9,2), 4)

    def test_modulo(self):
        self.assertEqual(self.calc.modulo(11,2), 1)
        self.assertEqual(self.calc.modulo(21,6), 3)


    # Add the following test methods to the TestCalculator class:

if __name__ == '__main__':
    unittest.main(verbosity=2)