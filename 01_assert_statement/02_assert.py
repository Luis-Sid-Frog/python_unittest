# amount = -1000
amount = 1000

# tax_rate = 1.15
tax_rate = 0.15

assert amount >= 0, 'The amount should not be negative'
assert 0 < tax_rate < 1, 'Tax rate shoud be between 0 and 1'