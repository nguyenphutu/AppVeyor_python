import unittest
from Source.add_function import add_fun

class FunTest(unittest.TestCase):
    def test_add_fun(self):
        self.assertEquals(add_fun(2, 5), 7)

    def test_add_fun_false(self):
        self.assertNotEqual(add_fun(2, 5), 8)

    # test hound


if __name__ == '__main__':
    unittest.main()