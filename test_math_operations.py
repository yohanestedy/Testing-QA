# test_math_operations.py
import math_operations
import unittest

class TestMathOperations(unittest.TestCase):
    def test_add(self):
        self.assertEqual(math_operations.add(2, 3), 5)
        self.assertEqual(math_operations.add(0, 0), 0)
        self.assertEqual(math_operations.add(-1, 1), 0)

if __name__ == '__main__':
    unittest.main()
