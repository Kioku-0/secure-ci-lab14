import unittest

from app import sum_integers


class TestApp(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_integers(2, 3), 5)

    def test_rejects_string(self):
        with self.assertRaises(ValueError):
            sum_integers("2", 3)

    def test_negative_numbers(self):
        self.assertEqual(sum_integers(-2, -3), -5)

    def test_rejects_float(self):
        with self.assertRaises(ValueError):
            sum_integers(2.5, 3)

    def test_rejects_bool(self):
        with self.assertRaises(ValueError):
            sum_integers(True, 3)


if __name__ == "__main__":
    unittest.main()
