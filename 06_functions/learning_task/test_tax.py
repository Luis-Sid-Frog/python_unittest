import unittest

from tax import calc_tax

class TestCalcTax(unittest.TestCase):

    def test_calc_tax_incorect_age_type_should_raise_type_error(self):
        self.assertRaises(TypeError,calc_tax, 1000,0.23, '19' )

    def test_calc_tax_age_incorect_value_should_raise_value_error(self):
        self.assertRaises(ValueError, calc_tax, 1000, 0.23, 0)

    def test_calc_age_twenty_percent_and_eighteen_age(self):
        self.assertAlmostEqual(calc_tax(60000,0.2,18), 5000)

    def test_calc_age_twenty_percent_and_nineteen_age(self):
        self.assertAlmostEqual(calc_tax(60000,0.2,19), 12000)

    def test_calc_age_twenty_percent_and_sixty_five_age(self):
        self.assertAlmostEqual(calc_tax(60000,0.2,65), 12000)

    def test_calc_age_twenty_percent_and_sixty_six_age(self):
        self.assertAlmostEqual(calc_tax(60000,0.2,66), 8000)