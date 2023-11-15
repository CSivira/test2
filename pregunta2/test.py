import unittest
from collections import deque
from main import prefix_eval, postfix_eval, to_infix, MODE


class TestMethods(unittest.TestCase):
    def setUp(self):
        self.e1 = "+ * + 3 4 5 7"
        self.e2 = "8 3 - 8 4 4 + * +"
        self.e3 = "* + 2 3 + 2 3"
        self.e4 = "2 3 - 2 3 - -"
        self.e5 = "1"
        self.e6 = "-1"
        self.e7 = "Carlos Sivira 15-11377"

    def test_prefix_eval(self):
        self.assertTrue(prefix_eval(deque(self.e1.split())) == 42)
        self.assertTrue(prefix_eval(deque(self.e3.split())) == 25)
        self.assertTrue(prefix_eval(deque(self.e5.split())) == 1)
        self.assertTrue(prefix_eval(deque(self.e6.split())) == -1)
        self.assertTrue(prefix_eval(deque(self.e7.split())) == "")

    def test_postfix_eval(self):
        self.assertTrue(postfix_eval(self.e2) == 69)
        self.assertTrue(postfix_eval(self.e4) == 0)
        self.assertTrue(postfix_eval(self.e5) == 1)
        self.assertTrue(postfix_eval(self.e6) == -1)
        self.assertTrue(postfix_eval(self.e7) == "")

    def test_to_infix(self):
        self.assertTrue(to_infix(self.e1, MODE.PRE) == "(3 + 4) * 5 + 7")
        self.assertTrue(to_infix(self.e2, MODE.POST) == "8 - 3 + 8 * (4 + 4)")
        self.assertTrue(to_infix(self.e3, MODE.PRE) == "(2 + 3) * (2 + 3)")
        self.assertTrue(to_infix(self.e4, MODE.POST) == "2 - 3 - 2 - 3")
