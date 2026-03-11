class InventoryTracker:

    def __init__(self):
        self.inventory = {}

    def add_item(self, item_name: str, quantity: int, price: float):
        self.inventory[item_name] = {
            "quantity": quantity,
            "price": price
        }
        print(f"Added '{item_name}': qty={quantity}, price=${price:.2f}")

    def remove_item(self, item_name: str):
        if item_name in self.inventory:
            del self.inventory[item_name]
            print(f"Removed '{item_name}' from inventory.")
        else:
            print(f"Item '{item_name}' not found.")

    def get_inventory(self) -> dict:
        return self.inventory

    def display_inventory(self):
        if not self.inventory:
            print("Inventory is empty.")
            return
        print("\n--- Current Inventory ---")
        for name, details in self.inventory.items():
            print(f"  {name}: qty={details['quantity']}, price=${details['price']:.2f}")
        print("-------------------------\n")

    def checkStockLevel(self, item_name: str) -> int:
        if item_name in self.inventory:
            quantity = self.inventory[item_name]["quantity"]
            print(f"Stock level for '{item_name}': {quantity} units")
            return quantity
        else:
            print(f"Item '{item_name}' not found in inventory.")
            return 0