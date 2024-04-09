import random 
class Product:
    
    def __init__(self, name, identifier=random.randrange(1000000, 10000000), price=10, weight=20, flammability=0.5):
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
        
class BoxingGlove(Product):
    def __init__(self, name, price=10, flammability=0.5, identifier=random.randrange(1000000, 10000000), weight=10):
        super().__init__(name, identifier, price, weight, flammability)

    def explode(self):
        return "...it's a glove."
    
    def punch(self):
        if self.weight  < 5:
            return "That tickles."
        elif self.weight >=5 and self.weight < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"


    def __repr__(self):
        return {self.name}
    
if __name__=='__main__':
    # prod = Product('A coll Toy')
    # print(prod.name)
    # print(prod.price)
    # print(prod.weight)
    # print(prod.flammability)
    # print(prod.identifier)
    # print(prod.stealability())
    # print(prod.explode())

    glove = BoxingGlove('Punchy the Third')
    print(glove.price)
    print(glove.weight)
    print(glove.punch())
    print(glove.explode())