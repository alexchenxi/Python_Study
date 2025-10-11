import unittest

from shopping_list import ShoppingList


class TestShoppingList(unittest.TestCase):
    def setUp(self):
        self.shopping_list = ShoppingList({"Toothbrush": 19, "Towel": 15})

    def test_get_item_cont(self):
        self.assertEqual(self.shopping_list.get_item_count(), 2)  # add assertion here

    def test_get_total_price(self):
        self.assertEqual(
            self.shopping_list.get_total_price(), 324
        )  # add assertion here
