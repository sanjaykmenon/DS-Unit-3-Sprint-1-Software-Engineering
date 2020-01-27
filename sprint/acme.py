from random import randint

class Product:
    """
    Creates and initializes the variables for a product.
    name (string with no default)
    price (integer with default value 10)
    weight (integer with default value 20)
    flammability (float with default value 0.5)
    identifier (integer, automatically genererated as a random number anywhere from 1000000 to 9999999)
    """
    def __init__(self, name, price=10, weight=20, flammability=0.5):
        self.name = name
        self.price = price
        self.weight = weight
        self.flammability = flammability
        self.identifier = randint(1000000,9999999)
    
    def stealability(self):
        ratio  = self.price / self.weight
        if ratio < 0.5:
            return 'Not so stealable' 
        elif ratio < 1.0:
            return 'Kinda stealable'
        else:
            return 'Very stealable!'
    
    def explode(self):
        flam_weight = self.flammability * self.weight
        if flam_weight < 10:
            return '..fizzle'
        elif flam_weight < 50:
            return '...boom!'
        else:
            return '...BABOOM!!!'

class BoxingGlove(Product):
    def __init__(self,name):
        super().__init__(name)
        self.weight = 10
    
    def explode(self):
        return "...it's a glove"

    def punch(self):
        power = self.weight
        if power < 5:
            return "That tickles"
        elif power < 15:
            return "Hey that hurt!"
        else:
            return "OUCH!"