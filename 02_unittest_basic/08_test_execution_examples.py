import unittest

class TestClass_1(unittest.TestCase):

    def test_case_4(self):
        self.assertTrue('appple'.islower())

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John','Smith'])

class TestClass_2(unittest.TestCase):
    def test_case_2(self):
        self.assertEqual('3.9'.split('.'), ['3','9'])

class TestClass_3(unittest.TestCase):
    def test_case_3(self):
        self.assertEqual('#'.join(['sport','gym']), 'sport#gym')


#  ŻEBY DOSTAĆ SIĘ /  WYKONAĆ TYLKO TESTY Z KONKRETNEJ KLASY WPISUJEMY W TERMINAL :
# py -m unittest 08_test_execution_examples.TestClass_1 -v

#  ŻEBY WYKONAĆ KONRETNY 1 TEST WPISUJEMY W TERMINAL:
# py -m unittest 08_test_execution_examples.TestClass_1.test_case_4 -v