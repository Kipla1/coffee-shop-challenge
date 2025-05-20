import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestOrder(unittest.TestCase):
    def setUp(self):
        """Set up test objects for the tests"""
        self.customer = Customer("Alice")
        self.coffee = Coffee("Latte")
    
    def test_init_valid_parameters(self):
        """Test that an order can be initialized with valid parameters"""
        order = Order(self.customer, self.coffee, 3.5)
        self.assertEqual(order.customer, self.customer)
        self.assertEqual(order.coffee, self.coffee)
        self.assertEqual(order.price, 3.5)
    
    def test_init_customer_validation(self):
        """Test that customer must be a Customer instance"""
        with self.assertRaises(TypeError):
            Order("Not a customer", self.coffee, 3.5)
    
    def test_init_coffee_validation(self):
        """Test that coffee must be a Coffee instance"""
        with self.assertRaises(TypeError):
            Order(self.customer, "Not a coffee", 3.5)
    
    def test_init_price_type_validation(self):
        """Test that price must be a number"""
        # Valid - integer (converted to float)
        order = Order(self.customer, self.coffee, 5)
        self.assertEqual(order.price, 5.0)
        self.assertIsInstance(order.price, float)
        
        # Valid - float
        order = Order(self.customer, self.coffee, 5.5)
        self.assertEqual(order.price, 5.5)
        
        # Invalid - string
        with self.assertRaises(TypeError):
            Order(self.customer, self.coffee, "5.5")
    
    def test_init_price_range_validation(self):
        """Test that price must be between 1.0 and 10.0"""
        # Valid - minimum price
        order = Order(self.customer, self.coffee, 1.0)
        self.assertEqual(order.price, 1.0)
        
        # Valid - maximum price
        order = Order(self.customer, self.coffee, 10.0)
        self.assertEqual(order.price, 10.0)
        
        # Invalid - below minimum
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 0.99)
        
        # Invalid - above maximum
        with self.assertRaises(ValueError):
            Order(self.customer, self.coffee, 10.01)
    
    def test_price_immutability(self):
        """Test that price cannot be changed after initialization"""
        order = Order(self.customer, self.coffee, 3.5)
        self.assertEqual(order.price, 3.5)
        
        # Verify price attribute has no setter
        with self.assertRaises(AttributeError):
            order.price = 4.5
    
    def test_relationships(self):
        """Test that relationships are properly set up"""
        order = Order(self.customer, self.coffee, 3.5)
        
        # Order should be in customer's orders
        self.assertIn(order, self.customer.orders)
        
        # Order should be in coffee's orders
        self.assertIn(order, self.coffee.orders)

if __name__ == '__main__':
    unittest.main()