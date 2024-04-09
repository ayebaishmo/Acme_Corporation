import random 
class Product:
    
    def __init__(self, name, identifier=99999, price=10, weight=20, flammability=0.5):
        self.name = name
        self.identifier = identifier
        self.price = price
        self.weight = weight
        self.flammability = flammability

    def stealability(self):
        ratio_steal = self.price/self.weight
        if ratio_steal < 0.5:
            return "Not so stealable..."
        elif ratio_steal >= 0.5 and ratio_steal < 1.0:
            return "Kinda stealable."
        else:
            return "Very stealable!"
    
    def explode(self):
        flamma_weight = self.flammability * self.weight
        if flamma_weight < 10:
            return "...fizzle."
        elif flamma_weight >=10 and flamma_weight < 50:
            return "...boom!"
        else:
            return "...BABOOM!!"
        
        
    
