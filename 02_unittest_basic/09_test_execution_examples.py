import unittest

class TestClass_1(unittest.TestCase):

    def test_case_4(self):
        self.assertTrue('Appple'.islower())

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John','Smith'])

    def test_case_3(self):
        self.assertEqual('#'.join(['sport','gym']), '#sport#gym')

class TestClass_2(unittest.TestCase):
    def test_case_2(self):
        self.assertEqual('3.9'.split('.'), ['3','9'])
