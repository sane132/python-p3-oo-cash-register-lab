class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = 0

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = price * quantity

    def apply_discount(self):
        if self.discount > 0:
            self.total = int(self.total * (1 - self.discount / 100))
            print(f"After the discount, the total comes to ${self.total}.")
            return self.total
        else:
            print("There is no discount to apply.")
            return self.total

    def void_last_transaction(self):
        self.total -= self.last_transaction
        # Remove the last added items (simplified version)
        if self.last_transaction > 0:
            item_count = int(self.last_transaction / (self.last_transaction / len(self.items[-1:])))
            for _ in range(item_count):
                self.items.pop()
        self.last_transaction = 0