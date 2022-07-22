import unittest
from calculator.calc_math import SimpleMathCalculator

def setUpModule():
    print('setting up... ')
    global calc
    calc = SimpleMathCalculator()
def tearDownModule():
    print('tearing down... ')
    global calc
    del calc
class TestSimpleMathCalculator(unittest.TestCase):


    def test_add(self):
        self.assertEqual(calc.add(3,4),7)

    def test_sub(self):
        self.assertEqual(calc.sub(5,4),1)

    def test_nul(self):
        self.assertEqual(calc.nul(3,4),12)

    def test_true_div(self):
        self.assertEqual(calc.true_div(5,2),2.5)

    def test_floor_div(self):
        self.assertEqual(calc.floor_div(6,2),3)
