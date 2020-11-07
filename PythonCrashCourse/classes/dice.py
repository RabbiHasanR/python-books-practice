from random import randint

class Dice:
    """A simple model for dice"""

    def __init__(self, sides=6):
        """Initialize dice attributes"""
        self.sides = sides
    
    def roll_dice(self):
        """rool for dice"""
        random_number = randint(1, self.sides)
        return random_number

def multiple_dice_roll(limit, dice):
    """Roll multiple time"""
    for value in range(limit):
        print(f"{value} dice score: {dice.roll_dice()}")

dice = Dice()
multiple_dice_roll(10, dice)


print("\n 10-sided dice:")
dice_1 = Dice(10)
multiple_dice_roll(10, dice_1)

print("\n 20-sided dice:")
dice_2 = Dice(20)
multiple_dice_roll(10, dice_2)


