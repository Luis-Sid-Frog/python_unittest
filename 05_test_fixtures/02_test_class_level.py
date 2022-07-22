import unittest


def setUpModule():
    print(('setting up module... '))

def tearDownModule(cls):
    print(f'tearing down module...{cls.__name__} ')

class TestClass_1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print('setting up class... ')

    @classmethod
    def tearDownClass(cls):
        print('tearing down class...')

    def test_case_4(self):
        self.assertTrue('appPle'.islower())

    def test_case_1(self):
        self.assertEqual('John Smith'.split(), ['John','Smith'])

class TestClass_2(unittest.TestCase):


    def test_case_2(self):
        self.assertEqual('3.9'.split('.'), ['3','9'])

class TestClass_3(unittest.TestCase):

    def test_case_3(self):
        self.assertEqual('#'.join(['sport','gym']), 'sport#gym')