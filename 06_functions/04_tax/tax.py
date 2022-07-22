
def calc_tax(amount, tax_rate):
    """ The function returns the amount of income tax"""
    if not isinstance(amount, (int, float)):
        raise TypeError('The amount value must be type int or float type. ')
    if not amount >= 0:
        raise ValueError(' The amount value must be positive.')

    if not isinstance(tax_rate, float):
        raise TypeError('The tax value must be float type. ')
    if not 0 < tax_rate < 1:
        raise ValueError('The tax rate value must be between 0 and 1. ')

    return amount * tax_rate

