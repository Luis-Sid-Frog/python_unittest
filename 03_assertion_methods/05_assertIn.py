import unittest

class TestClass1(unittest.TestCase):

    def test_case_1(self):
        self.assertIn('@','mateuszsadowski24@gmail.com')

    def test_case_2(self):
        self.assertIn('@','mateuszsadowski24gmail.com')

    def test_case_3(self):
        tech_stack = ['python', 'java', 'sql']
        self.assertIn('python', tech_stack)

    def test_case_4(self):
        tech_stack = ['python','java','sql']
        self.assertIn('C++',tech_stack)

    def test_case_5(self):
        tech_stack = {'python': 'mid','java':'senior','sql' : 'junior'}
        self.assertIn('python',tech_stack)

    def test_case_6(self):
        tech_stack = {'python': 'mid','java':'senior','sql' : 'junior'}
        self.assertIn('C++',tech_stack)

# METODA PRZECIWNA assertNotIn

    def test_case_7(self):
        tech_stack = {'python': 'mid','java':'senior','sql' : 'junior'}
        self.assertNotIn('python',tech_stack)

    def test_case_8(self):
        tech_stack = {'python': 'mid','java':'senior','sql' : 'junior'}
        self.assertNotIn('C++',tech_stack)