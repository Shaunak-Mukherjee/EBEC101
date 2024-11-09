"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 11.2.1. Dice
Date: 11/07/2024

Description:
To simulate dice rolls, we define a `Dice` class with attributes for 
the number of sides and methods to roll the dice and perform multiple rolls. 
We create instances of this class to represent different types of dice and 
then use them to simulate rolling those dice multiple times.


Contributors:
    Name, login@purdue.edu [NA]

My contributor(s) helped me:
    [x] understand the assignment expectations without
        telling me how they will approach it.
    [ ] understand different ways to think about a solution
        without helping me plan my solution.
    [ ] think through the meaning of a specific error or
        bug present in my code without looking at my code.
    Note that if you helped somebody else with their code, you
    have to list that person as a contributor.

Academic Integrity Statement:
    I have not used source code obtained from any unauthorized
    source, either modified or unmodified; nor have I provided
    another student access to my code.  The project I am
    submitting is my own original work.
"""

import random

# Create the main class
class Dice:
    def __init__(self, sides):
        self.sides = sides

    def roll(self):
        return random.randint(1, self.sides)

    def n_rolls(self, n):
        print(f"Rolling a {self.sides} sided die {n} times:")
        for _ in range(n):
            print(self.roll(), end=", ")
        print()

# Create three dice instances
die1 = Dice(6)
die2 = Dice(10)
die3 = Dice(20)

# Roll each die 10 times
die1.n_rolls(10)
die2.n_rolls(10)
die3.n_rolls(10)

    
# """Do not change anything below this line."""
# if __name__ == "__main__":
#     main()
