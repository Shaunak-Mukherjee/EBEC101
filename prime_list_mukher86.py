"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 4.2.5. Prime List
Date: 09/20/2024

Description:
The program defines a function is_prime() to determine whether a given number is prime. 
It checks for divisibility starting from 2 up to the square root of the number. 
If the number is divisible by any number in this range, it's not prime; otherwise, it is.
The program then lists all the prime from 2 upto a specific limit defined by the user's
input.

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
        for i in range(2, int(math.sqrt(number)) + 1):  # Choice O(√number) computation cost
            if number % i == 0:
                return False
        return True

def main():
    # User input for the upper limit
    user_input = int(input("Enter a positive integer: "))
    
    # Empty list to store prime numbers
    primes = []
    
    # Loop through all numbers from 2 to the user input
    for num in range(2, user_input + 1):
        if is_prime(num):
            primes.append(num)  # Append prime numbers to the list

    # Print the results
    print(f"The primes up to {user_input} are: {', '.join(map(str, primes))}")
    

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
