#Problem: Given a list of orders, where each order is represented as a string, identify and return duplicate orders.

def find_duplicates(orders):
    seen = set()
    duplicates =[]
    for order in orders:
        if order in seen:
            duplicates.append(order)
        else:
            seen.add(order)
    return duplicates

orders = ["order1", "order2", "order3", "order1", "order2"]
print(find_duplicates(orders))
