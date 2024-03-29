import unittest


def setUpModule():
    print(('setting up module...'))

def tearDownModule():
    print('tearing down module...')

class TestClass_1(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print(f'setting up class...{cls.__name__}  ')

    @classmethod
    def tearDownClass(cls):
        print(f'tearing down class...{cls.__name__} ')

    def setUp(self):
        print('setting up...')

    def tearDown(self):
        print('tearing down...')

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