import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
from calculator import Calculator
import unittest

from pricing import calculate_discounted_price, apply_tax


class TestPricingFunctions(unittest.TestCase):

    # ---- Tests für calculate_discounted_price ----

    def test_discount_valid(self):
        self.assertAlmostEqual(calculate_discounted_price(100, 20), 80)

    def test_discount_zero(self):
        self.assertAlmostEqual(calculate_discounted_price(100, 0), 100)

    def test_discount_full(self):
        self.assertAlmostEqual(calculate_discounted_price(100, 100), 0)

    def test_discount_negative_price(self):
        with self.assertRaises(ValueError):
            calculate_discounted_price(-10, 10)

    def test_discount_invalid_percentage(self):
        with self.assertRaises(ValueError):
            calculate_discounted_price(100, 150)

    # ---- Tests für apply_tax ----

    def test_tax_valid(self):
        self.assertAlmostEqual(apply_tax(100, 19), 119)

    def test_tax_zero(self):
        self.assertAlmostEqual(apply_tax(100, 0), 100)

    def test_tax_negative_price(self):
        with self.assertRaises(ValueError):
            apply_tax(-50, 19)

    def test_tax_negative_rate(self):
        with self.assertRaises(ValueError):
            apply_tax(100, -5)


if __name__ == "__main__":
    unittest.main()
