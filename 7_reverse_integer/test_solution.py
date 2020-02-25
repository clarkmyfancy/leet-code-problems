import unittest 
from solution import *

class TestSolution(unittest.TestCase):

    def setUp(self):
        self.s = Solution()

    def tearDown(self):
        del self.s 

    def test_reverse(self):
        self.assertEqual(self.s.reverse(321), 123)
        self.assertEqual(self.s.reverse(-123), -321)


if __name__ == "__main__":
    unittest.main()