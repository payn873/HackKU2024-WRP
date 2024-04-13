class Item():

    def __init__(self, amount: int, name: str, price: float):
        self.amount = amount
        self.name = name
        self.price = price
    
    def restock(self, amount: int):
        # Increments amount by the amount entered.
        self.amount += amount
    
    def remove(self, amount: int):
        # Lowers amount by the amount entered, but if amount is then less than zero it is set to 0.
        self.amount -= amount
        if self.amount < 0:
            self.amount = 0
