#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0):
      self.discount = discount
      self.total = 0
      self.items = []
      self.previous_transactions = []

  @property
  def discount(self):
     return self._discount

  @discount.setter
  def discount(self, value):

# discount must be a whole number between 0 and 100
      if isinstance(value, int) and not isinstance(value, bool) and 0 <= value <= 100:
          self._discount = value
      else:
          print("Not valid discount")
# keep whatever discount we already had (or 0 if none yet)
          self._discount = getattr(self, "_discount", 0)
 
  def add_item(self, title, price, quantity=1):
# add this item's cost to the running total
      self.total += price * quantity
 
# add the item name once per unit bought
      for _ in range(quantity):
          self.items.append(title)
 
# remember this transaction so we can void it later
      self.previous_transactions.append({
          "title": title,
          "price": price,
          "quantity": quantity,
        })
 
  def apply_discount(self):
        if self.discount == 0:
# nothing to discount
            print("There is no discount to apply.")
        else:
# subtract the discount % from the total
            discount_amount = self.total * self.discount / 100
            new_total = self.total - discount_amount
 
# show a clean number, e.g. 800 instead of 800.0
            if new_total == int(new_total):
                new_total = int(new_total)
 
            self.total = new_total
            print(f"After the discount, the total comes to ${self.total}.")
 
  def void_last_transaction(self):
      if not self.previous_transactions:
            # nothing to undo
            print("There is no transaction to void.")
            return
 
# grab and remove the most recent transaction
      last_transaction = self.previous_transactions.pop()
 
        
      self.total -= last_transaction["price"] * last_transaction["quantity"]
 
# remove the matching number of that item from the items list
      for _ in range(last_transaction["quantity"]):
          if self.items and self.items[-1] == last_transaction["title"]:
              self.items.pop()
 