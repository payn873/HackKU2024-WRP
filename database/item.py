class Item():

    def __init__(self, amount: int, name: str, price: float):
        self.amount = amount
        self.name = name
        self.price = price
    
    def restock(self, amount: int):
        self.amount += amount
    
    def remove(self, amount: int)
        self.amount -= amount
        if self.amount < 0:
            self.amount = 0
