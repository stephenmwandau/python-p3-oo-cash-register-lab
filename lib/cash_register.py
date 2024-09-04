#!/usr/bin/env python3

class CashRegister:
    def __init__(self, discount=0):
        self.discount = discount
        self.total = 0
        self.items = []
        self.last_transaction = None  # Track the last transaction details

    def add_item(self, title, price, quantity=1):
        self.total += price * quantity
        self.items.extend([title] * quantity)
        self.last_transaction = (title, price, quantity)  # Save the last transaction details

    def apply_discount(self):
        if self.discount > 0:
            discount_amount = (self.total * self.discount) / 100
            self.total -= discount_amount
            print(f"After the discount, the total comes to ${int(self.total)}.")
        else:
            print("There is no discount to apply.")

    def void_last_transaction(self):
        if self.last_transaction:
            title, price, quantity = self.last_transaction
            # Remove the last transaction's items from the list and adjust the total
            for _ in range(quantity):
                self.items.remove(title)
            self.total -= price * quantity
            if self.total < 0:
                self.total = 0
            self.last_transaction = None  # Clear last transaction details

    def _item_price(self, title):
        # This function is for demonstration. You can manage item prices differently if needed.
        price_list = {
            "eggs": 0.98,
            "book": 5.00,
            "Lucky Charms": 4.5,
            "Ritz Crackers": 5.0,
            "Justin's Peanut Butter Cups": 2.50,
            "macbook air": 1000
        }
        return price_list.get(title, 0)