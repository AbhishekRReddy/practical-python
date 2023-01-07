class Stock:
    def __init__(self,name,qty,price):
        self.name=name
        self.qty=qty
        self.price=price
    def cost(self):
        return self.qty*self.price
    def sell(self,qty):
        self.qty-=qty