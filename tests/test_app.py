import unittest

from app import sum_integers


class TestApp(unittest.TestCase):
    def test_sum(self):
        self.assertEqual(sum_integers(2, 3), 5)


if __name__ == "__main__":
    unittest.main()
