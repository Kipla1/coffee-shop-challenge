import unittest
from customer import Customer
from coffee import Coffee
from order import Order

class TestCustomer(unittest.TestCase):
    def test_init_valid_name(self):
        """Test that a customer can be initialized with a valid name"""
        customer = Customer("Alice")
        self.assertEqual(customer.name, "Alice")
    
    def test_init_name_type_validation(self):
        """Test that name must be a string"""
        with self.assertRaises(TypeError):
            Customer(123)
    
    def test_init_name_min_length(self):
        """Test that name must be at least 1 character"""
        with self.assertRaises(ValueError):
            Customer("")
    
    def test_init_name_max_length(self):
        """Test that name must be at most 15 characters"""
        # Valid - exactly 15 characters
        customer = Customer("ABCDEFGHIJKLMNO")
        self.assertEqual(customer.name, "ABCDEFGHIJKLMNO")
        
        # Invalid - 16 characters
        with self.assertRaises(ValueError):
            Customer("ABCDEFGHIJKLMNOP")
    
    def test_name_setter_validation(self):
        """Test that name setter validates correctly"""
        customer = Customer("Alice")
        
        # Set to valid name
        customer.name = "Bob"
        self.assertEqual(customer.name, "Bob")
        
        # Set to invalid type
        with self.assertRaises(TypeError):
            customer.name = 123
        
        # Set to empty string (too short)
        with self.assertRaises(ValueError):
            customer.name = ""
        
        # Set to too long string
        with self.assertRaises(ValueError):
            customer.name = "ThisNameIsTooLongForTheRequirements"
    
    def test_orders_method(self):
        """Test that orders method returns all orders for the customer"""
        customer = Customer("Alice")
        coffee = Coffee("Latte")
        
        # Initially no orders
        self.assertEqual(len(customer.orders()), 0)
        
        # Add an order
        order = Order(customer, coffee, 3.5)
        self.assertEqual(len(customer.orders()), 1)
        self.assertIn(order, customer.orders())
        
        # Modifying the returned list should not affect the internal list
        orders = customer.orders()
        orders.append("Something")
        self.assertEqual(len(customer.orders()), 1)
    
    def test_coffees_method(self):
        """Test that coffees method returns unique list of coffees ordered"""
        customer = Customer("Alice")
        latte = Coffee("Latte")
        espresso = Coffee("Espresso")
        
        # Initially no coffees
        self.assertEqual(len(customer.coffees()), 0)
        
        # Add orders
        order1 = Order(customer, latte, 3.5)
        self.assertEqual(len(customer.coffees()), 1)
        self.assertIn(latte, customer.coffees())
        
        # Add another order for the same coffee
        order2 = Order(customer, latte, 4.0)
        self.assertEqual(len(customer.coffees()), 1)  # Still only one unique coffee
        
        # Add order for different coffee
        order3 = Order(customer, espresso, 3.0)
        self.assertEqual(len(customer.coffees()), 2)
        self.assertIn(espresso, customer.coffees())

if __name__ == '__main__':
    unittest.main()