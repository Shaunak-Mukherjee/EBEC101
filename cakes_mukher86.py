"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 3.2.1. Cakes
Date: 09/09/2024

Description:
This simple python program asks the user to enter a number and then
the program prints out a string * like a pyramid

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

"""Import additional modules below this line (starting with unit 6)."""


"""Write new functions below this line (starting with unit 4)."""
   
def main():
    # Add user inputs 
    layers = int(input("Enter the number of layers: "))

    # Implementiung for loop
    for i in range(1, layers + 1):
        # For loop for spaces
        for j in range(layers - i):
            print(" ", end="")
        
        # For loop for stars
        print("[", end="")
        for k in range(2 * i - 1):
            print("*", end="")
        print("]")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
