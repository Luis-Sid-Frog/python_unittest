import unittest
from calculator.calc_math import SimpleMathCalculator

class TestSimpleMathCalculator(unittest.TestCase):

    def test_add(self):
        # calc = SimpleMathCalculator()
        self.assertEqual(calc.add(3,4),7)

    def test_add(self):
        # calc = SimpleMathCalculator()
        self.assertEqual(calc.add(3,4),7)

    def test_sub(self):
        # calc = SimpleMathCalculator()
        self.assertEqual(calc.sub(5,4),1)

    def test_nul(self):
        # calc = SimpleMathCalculator()
        self.assertEqual(calc.nul(3,4),12)

    def test_true_div(self):
        # calc = SimpleMathCalculator()
        self.assertEqual(calc.true_div(5,2),2.5)

    def test_floor_div(self):
        calc = SimpleMathCalculator()
        self.assertEqual(calc.floor_div(6,2),3)
