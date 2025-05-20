from customer import Customer
from coffee import Coffee
from order import Order

if __name__ == "__main__":
    customer1 = Customer("Alice")
    customer2 = Customer("Bob")
    coffee1 = Coffee("Espresso")
    coffee2 = Coffee("Latte")

    order1 = customer1.create_order(coffee1, 5.0)
    order2 = customer1.create_order(coffee2, 6.0)
    order3 = customer2.create_order(coffee1, 4.5)

    print(f"{customer1.name}'s orders: {len(customer1.orders())}")
    print(f"{coffee1.name}'s average price: {coffee1.average_price()}")
    print(f"Most aficionado for {coffee1.name}: {Customer.most_aficionado(coffee1).name}")