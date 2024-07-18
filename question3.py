# Task 1

def format_orders(orders):
    for order in orders:
        customer_name, product, quantity = order
        formatted_order = f"{customer_name} ordered {quantity} of product {product}.\n"
        print(formatted_order)

format_orders(orders = [
    ("Alice", "Laptop", 1),
    ("Bob", "Camera", 2),
    ("Candice", "iPhone", 594304)
])