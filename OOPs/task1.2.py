from TASK1 import Product
from task13 import shipping

class Phproduct(Product, shipping):

    def __init__(self, name, price,weight):
        super().__init__(name, price)
        self.weight=weight

    def display(self):
        basic = super().display()
        return f"{basic} \nWeight :{self.weight}KG"

    def get_price(self):
        return self.price + ph.calculate(weight=100)


ph = Phproduct("apple", 100,1000)

print(ph.display())
print(f"Shipping cost of the product $ {ph.calculate(weight=100)}")
print(f"Original Price of the product ${ph.price} \nFinal price of the product $ {ph.get_price()}")