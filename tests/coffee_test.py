import unittest
from coffee import Coffee
from customer import Customer
from order import Order

class TestCoffee(unittest.TestCase):
    def test_init_valid_name(self):
        """Test that a coffee can be initialized with a valid name"""
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")
    
    def test_init_name_type_validation(self):
        """Test that name must be a string"""
        with self.assertRaises(TypeError):
            Coffee(123)
    
    def test_init_name_min_length(self):
        """Test that name must be at least 3 characters"""
        # Valid - exactly 3 characters
        coffee = Coffee("Tea")
        self.assertEqual(coffee.name, "Tea")
        
        # Invalid - 2 characters (too short)
        with self.assertRaises(ValueError):
            Coffee("Ab")
    
    def test_name_immutability(self):
        """Test that name cannot be changed after initialization"""
        coffee = Coffee("Latte")
        self.assertEqual(coffee.name, "Latte")
        
        # Verify name attribute has no setter
        with self.assertRaises(AttributeError):
            coffee.name = "Espresso"
    
    def test_orders_method(self):
        """Test that orders method returns all orders for the coffee"""
        coffee = Coffee("Latte")
        customer = Customer("Alice")
        
        # Initially no orders
        self.assertEqual(len(coffee.orders()), 0)
        
        # Add an order
        order = Order(customer, coffee, 3.5)
        self.assertEqual(len(coffee.orders()), 1)
        self.assertIn(order, coffee.orders())
        
        # Modifying the returned list should not affect the internal list
        orders = coffee.orders()
        orders.append("Something")
        self.assertEqual(len(coffee.orders()), 1)
    
    def test_customers_method(self):
        """Test that customers method returns unique list of customers who ordered"""
        coffee = Coffee("Latte")
        alice = Customer("Alice")
        bob = Customer("Bob")
        
        # Initially no customers
        self.assertEqual(len(coffee.customers()), 0)
        
        # Add orders
        order1 = Order(alice, coffee, 3.5)
        self.assertEqual(len(coffee.customers()), 1)
        self.assertIn(alice, coffee.customers())
        
        # Add another order for the same customer
        order2 = Order(alice, coffee, 4.0)
        self.assertEqual(len(coffee.customers()), 1)  # Still only one unique customer
        
        # Add order for different customer
        order3 = Order(bob, coffee, 3.0)
        self.assertEqual(len(coffee.customers()), 2)
        self.assertIn(bob, coffee.customers())

if __name__ == '__main__':
    unittest.main()