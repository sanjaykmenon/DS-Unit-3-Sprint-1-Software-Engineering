import unittest
from acme import Product
from acme_report import generate_products,adjectives,nouns

class AcmeProductTests(unittest.TestCase):
    """Making sure Acme products are the tops!"""
    def test_default_product_price(self):
        """Test default product price being 10."""
        prod = Product('Test Product')
        self.assertEqual(prod.price, 10)

    def test_default_product_flammibility(self):
        """Test default product flammibility being 0.5."""
        prod = Product('Test Product')
        self.assertEqual(prod.flammability, 0.5)

    def test_product_stealability(self):
        """Test that product stealability works as it should."""
        prod = Product('Test Product', price=20)
        self.assertEqual(prod.stealability(), "Very stealable!")


class AcmeReportTests(unittest.TestCase):
    """Making Sure Inventory Reports Are Accurate"""
    def test_default_num_products(self):
        """Test that default number of products is 30"""
        products = generate_products()
        self.assertEqual(len(products), 30)

    def test_legal_names(self):
        """Test that product names are legal names."""
        products = generate_products()
        for product in products:
            adj = product.split(" ")[0]
            noun = product.split(" ")[1]
        self.assertIn(adj, adjectives)
        self.assertIn(noun, nouns)


if __name__ == '__main__':
    unittest.main()    