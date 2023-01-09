class Stock:
    def __init__(self,name,qty,price):
        self.name=name
        self.shares=qty
        self.price=price
    def __repr__(self):
        return f'Stock({self.name},{self.qty},{self.price})'
    def cost(self):
        return self.qty*self.price
    def sell(self,qty):
        self.qty-=qty