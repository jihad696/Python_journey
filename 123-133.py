import unittest

class MyTestCases(unittest.TestCase):

    def test_10_in_list(self):
        self.assertIn(10, [5, 7, 8, 10])

    def test_type_of_10(self):
        self.assertIsInstance(10, int)

    def test_100_is_true(self):
        self.assertTrue(100)

    def test_empty_list_is_false(self):
        self.assertFalse([])

    def test_100_greater_equal_90(self):
        self.assertGreaterEqual(100, 90)

if __name__ == "__main__":
    unittest.main()

#==============================================================================

import random
import string

def generate_serial():

    chars = string.ascii_letters + string.digits

    part1 = ''.join(random.choices(chars, k=4))
    part2 = ''.join(random.choices(chars, k=4))
    part3 = ''.join(random.choices(chars, k=6))

    serial = f"{part1}-{part2}-{part3}"
    return serial

print(generate_serial())
