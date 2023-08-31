import random

class Dice:
    def __init__(self, sides=6):
        self.sides = sides
        
        
    def roll(self):
        return random.randint(1, self.sides)
    

dice = Dice(6)


dice2 = Dice()

print(dice2.roll())