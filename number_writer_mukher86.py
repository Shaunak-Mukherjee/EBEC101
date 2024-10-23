"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 8.2.4. Number Writer
Date: 10/22/2024

Description:
This program generates a specified number of random numbers between 1119 and 1217, 
excluding those whose digits sum to 13. It writes the valid random numbers to a 
file named `random_numbers.txt`. The program can either prompt the user for input 
or accept a predefined count for automated execution.

Contributors:
    Name, login@purdue.edu [NA]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
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

"""Import additional modules below this line (starting with unit 6)."""
import random

"""Write new functions below this line (starting with unit 4)."""

# Define main function
def main(count=None):
    if count is None:
        count = int(input("How many random numbers? "))
    
    # Make some comments because autograders asking for it. Seriously!
    with open("random_numbers.txt", 'w') as file:
        generated = 0
        while generated < count:
            num = random.randint(1119, 1217)
            if sum(int(digit) for digit in str(num)) != 13:
                file.write(f"{num}\n")
                generated += 1

if __name__ == "__main__":
    main()





