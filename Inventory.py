class Inventory:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def update_quantity(self, item, new_quantity):
        if item in self.inventory:
            self.inventory[item] = new_quantity
        else:
            print(f"{item} is not in the inventory.")

    def get_item_quantity(self, item):
        if item in self.inventory:
            return self.inventory[item]
        else:
            print(f"{item} is not in the inventory.")
            return None

    def total_quantity(self):
        return sum(self.inventory.values())


def main():
    inventory_system = Inventory()

    while True:
        print("\nInventory System Menu:")
        print("1. Add item to inventory")
        print("2. Update item quantity")
        print("3. Get item quantity")
        print("4. Total quantity of all items")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            item = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            inventory_system.add_item(item, quantity)
            print(f"{quantity} {item}(s) added to inventory.")

        elif choice == '2':
            item = input("Enter item name to update quantity: ")
            new_quantity = int(input("Enter new quantity: "))
            inventory_system.update_quantity(item, new_quantity)

        elif choice == '3':
            item = input("Enter item name to get quantity: ")
            quantity = inventory_system.get_item_quantity(item)
            if quantity is not None:
                print(f"Quantity of {item}: {quantity}")

        elif choice == '4':
            total = inventory_system.total_quantity()
            print(f"Total quantity of all items: {total}")

        elif choice == '5':
            print("Exiting the program.")
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 5.")


if __name__ == "__main__":
    main()
