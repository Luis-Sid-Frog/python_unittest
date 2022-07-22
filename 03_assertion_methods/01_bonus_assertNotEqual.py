import unittest


class TestClass_1(unittest.TestCase):

    def test_case_1(self):
        self.assertNotEqual('aws'.upper(), 'AWS')

    def test_case_2(self):
        self.assertNotEqual('aws'.upper(), 'aWS')

    def test_case_3(self):
        self.assertNotEqual('3.9.0'.split('.'), ['3', '9', '0'])

    def test_case_4(self):
        self.assertNotEqual('3.9.0'.split('.'), ['3', '9', 0])
