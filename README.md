# Coffee Shop Challenge

This repository implements a simple domain model for a coffee shop, demonstrating object-oriented programming principles in Python.

## Domain Model

The application models a coffee shop with three main entities:
- `Customer` - People who order coffee
- `Coffee` - Different types of coffee drinks
- `Order` - Represents a purchase of a specific coffee by a customer

### Relationships
- A Coffee has many Orders
- A Customer has many Orders
- An Order belongs to a Customer and to a Coffee
- Coffee and Customer have a many-to-many relationship through Order

## Object Relationships

The model implements the following relationships:
- `Order.customer` → returns the Customer instance
- `Order.coffee` → returns the Coffee instance
- `Customer.orders()` → all Order instances for that customer
- `Customer.coffees()` → unique list of Coffee instances they've ordered
- `Coffee.orders()` → all Order instances for that coffee
- `Coffee.customers()` → unique list of Customer instances who've ordered it

## Project Structure

```
coffee-shop-challenge/
├── Pipfile
├── debug.py            # Demo script showing usage
├── customer.py         # Customer class implementation
├── coffee.py           # Coffee class implementation
├── order.py            # Order class implementation
└── tests/
    ├── customer_test.py    # Tests for Customer class
    ├── coffee_test.py      # Tests for Coffee class
    └── order_test.py       # Tests for Order class
```

## Getting Started

1. Clone the repository
```bash
git clone git@github.com:<Kipla1>/coffee-shop-challenge.git
cd coffee-shop-challenge
```

2. Set up Python environment
```bash
pipenv install
pipenv shell
```

3. Run the demo script
```bash
python debug.py
```

4. Run the tests
```bash
python -m unittest discover tests
```

## Requirements

### Customer
- Name must be a string between 1-15 characters

### Coffee
- Name must be a string with at least 3 characters
- Name is immutable after initialization

### Order
- Must reference a valid Customer and Coffee instance
- Price must be a float between 1.0 and 10.0
- Price is immutable after initialization