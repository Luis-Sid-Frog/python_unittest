import unittest
from calculator.calc_math import SimpleMathCalculator


class TestSimpleMathCalculatorAdd(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Setting up class... ')
        cls.calc = SimpleMathCalculator()

    @classmethod
    def tearDownClass(cls):
        print('Tearing down class... ')
        cls.calc = SimpleMathCalculator()

    def test_add_int(self):
        self.assertEqual(self.calc.add(3, 4), 7)

    def test_add_float(self):
        self.assertEqual(self.calc.add(3.0,4.0),7.0)

    def test_add_both_negative(self):
        self.assertEqual(self.calc.add(-3,-4),-7)


class TestSimpleMathCalculatorSub(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('Setting up class... ')
        cls.calc = SimpleMathCalculator()

    @classmethod
    def tearDownClass(cls):
        print('Tearing down class... ')
        cls.calc = SimpleMathCalculator()

    def test_sub_int(self):
        self.assertEqual(self.calc.sub(5,4),1)

    def test_nul_float(self):
        self.assertEqual(self.calc.nul(3.0,4.0),12.0)

    def test_true_div(self):
        self.assertEqual(self.calc.true_div(5,2),2.5)

    def test_floor_div(self):
        self.assertEqual(self.calc.floor_div(6,2),3)