"""
This is python module that creates products
and performs some methods on them
"""
import random


class Product:
    """
    Above is a class called Product
    This class create a product 
    with several aspects
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = random.randint(1000000, 9999999)

    def stealability(self):
        """
        This function calculates the 
        ratio of price to weight
        """
        ratio = self.price / self.weight
        if ratio < 0.5:
            return "Not so stealable..."
        if ratio >= 0.5 or ratio < 1.0:
            return "Kinda stealable."
        return "Very stealable!"

    def explode(self):
        """
        This function calculates
        the product
        """
        product = self.flammability * self.weight
        if product < 10:
            return "...fizzle."
        if 10 <= product < 50:
            return "...boom!"
        return "...BABOOM!!"

class BoxingGlove(Product):
    """
    This is child class that 
    inherits the product class
    """
    def __init__(self, name, price=10, weight=10, flammability=0.5):
        super().__init__(name, price, weight, flammability)

    def explode(self):
        return "...it's a glove."

    def punch(self):
        """
        This function checks
        the weight and returns a statement
        """
        if self.weight <= 5:
            return "That tickles."
        if self.weight > 5 and self.weight < 15:
            return "Hey that hurt!"
        return "OUCH!"
