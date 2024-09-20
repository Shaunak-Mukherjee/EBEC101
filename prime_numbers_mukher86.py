"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 4.2.4. Prime Numbers
Date: 09/19/2024

Description:
The program defines a function is_prime() to determine whether a given number is prime. 
It checks for divisibility starting from 2 up to the square root of the number. 
If the number is divisible by any number in this range, it's not prime; otherwise, it is.

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
import math

"""Write new functions below this line (starting with unit 4)."""
   
# Function that determines if a number is prime
def is_prime(number):
    if number < 2:
        return False
    else:
        for i in range (2, int(math.sqrt(number))+1): # Choice O(√number) computation cost
            if number % i == 0:
                return False
        return True
def main():
    while True:
        # User input 
        number = int(input("Enter a positive integer (-1 to quit): "))
        # Exit the loop if the user enters -1
        if number == -1:
            break
        
        # Check if the number is prime
        if is_prime(number):
            print(f"  {number} is prime!")
        else:
            print(f"  {number} is not prime.")
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
