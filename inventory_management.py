#Problem: Write a program to track and update the inventory of a store. The program should:

# Add items to the inventory.
# Update the quantity of existing items.
# Retrieve the current stock of an item.

class Inventory:
    def __init__(self):
        self.stock = {}

    def add_item(self, item_name, quantity):
        if item_name in self.stock:
            self.stock[item_name] += quantity
        else:
            self.stock[item_name] = quantity

    def update_item(self, item_name, quantity):
        if item_name in self.stock:
            self.stock[item_name] = quantity

    def get_stock(self, item_name):
        return self.stock.get(item_name, 0)

inventory = Inventory()
inventory.add_item("Apple", 10)
inventory.add_item("orange", 20)
inventory.update_item("Apple",15)
print(inventory.get_stock("Apple"))
