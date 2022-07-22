import unittest
from tax import calc_tax

class TestCalsTax(unittest.TestCase):

    def test_calc_tax_with_ten_percent(self):
        self.assertEqual(10,calc_tax(100,0.1))

    # def test_calc_tax_with_fourteen_percent(self):
    #     self.assertEqual(14,calc_tax(100,0.14))

    def test_calc_tax_with_fourteen_percent_with_assert_almost_equal(self):
        self.assertAlmostEqual(14,calc_tax(100,0.14))

    def test_calc_tax_with_incorect_amount_type_should_raise_error(self):
        self.assertRaises(TypeError,calc_tax,'ten',0.23)

    def test_calc_tax_with_incorect_tax_rate_type_should_raise_error(self):
        self.assertRaises(TypeError,calc_tax,100,'0.23')

    def test_calc_tax_with_incorect_tax_rate_should_raise_error(self):
        self.assertRaises(ValueError,calc_tax,100, 1.0)
        self.assertRaises(ValueError,calc_tax,100, 0.0)

    def test_calc_tax_with_incorect_negative_amount_type_should_raise_error(self):
        self.assertRaises(ValueError,calc_tax,-100,0.23)

