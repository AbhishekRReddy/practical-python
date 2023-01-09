class Stock:
    def __init__(self,name,qty,price):
        self.name=name
        self.shares=qty
        self.price=price
    def __repr__(self):
        return f'Stock({self.name},{self.shares},{self.price})'
    def cost(self):
        return self.shares*self.price
    def sell(self,qty):
        self.shares-=qty