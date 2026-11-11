#Dice

import random


class Die:
    """A class to represent a die."""

    def __init__(self, sides=6):
        """Initialize the die with given number of sides."""
        self.sides = sides

    def roll_die(self):
        """Print a random number between 1 and the number of sides."""
        result = random.randint(1, self.sides)
        print(result)


print("Rolling a 6-sided die 10 times:")
d6 = Die()
for _ in range(10):
    d6.roll_die()

print("\nRolling a 10-sided die 10 times:")
d10 = Die(sides=10)
for _ in range(10):
    d10.roll_die()

print("\nRolling a 20-sided die 10 times:")
d20 = Die(sides=20)
for _ in range(10):
    d20.roll_die()
