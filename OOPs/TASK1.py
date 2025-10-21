from abc import ABC, abstractmethod

class Product(ABC):
    category = "General"
    def __init__(self,name,price):
        self.name=name
        self.price=price



    def display(self):
        return f"Name: {self.name}\nPrice: {self.price}"


    @abstractmethod
    def get_price(self):
        pass