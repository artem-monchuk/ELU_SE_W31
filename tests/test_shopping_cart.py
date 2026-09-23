import io
import unittest
from contextlib import redirect_stdout

from shopping_cart import calculate_total, display_total


class TestCalculateTotal(unittest.TestCase):

    def test_multiple_items_return_correct_total(self):
        cart = [
            {'name': 'Item A', 'price': 10.99},
            {'name': 'Item B', 'price': 5.99},
            {'name': 'Item C', 'price': 8.49},
        ]
        self.assertAlmostEqual(calculate_total(cart), 25.47)

    def test_empty_cart_returns_zero(self):
        self.assertEqual(calculate_total([]), 0)

    def test_single_item_returns_correct_total(self):
        cart = [{'name': 'Item A', 'price': 10.99}]
        self.assertAlmostEqual(calculate_total(cart), 10.99)

    def test_decimal_prices_are_calculated_correctly(self):
        cart = [
            {'name': 'Item A', 'price': 0.1},
            {'name': 'Item B', 'price': 0.2},
        ]
        self.assertAlmostEqual(calculate_total(cart), 0.3)


class TestDisplayTotal(unittest.TestCase):

    def test_display_total_prints_expected_output(self):
        buffer = io.StringIO()
        with redirect_stdout(buffer):
            display_total(25.47)
        self.assertEqual(buffer.getvalue(), "Total price: $25.47\n")


if __name__ == "__main__":
    unittest.main()
