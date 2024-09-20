"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 2.2.1. Leap Year
Date: 09/02/2024

Description:
This python program prompts the user to input a year then, 
it display the number of days in February for that year and 
from that criteria the program will help to determine if it 
is a leap year

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
    
    # User input
    year = int(input("Enter a year: "))

    # Leap year validation 
    if year % 4 == 0: # Check if divisible by 4
        if year % 100 == 0: # Check if divisible by 100
            if year % 400 == 0: # Check if divisible by 3400
                print(f"The year {year} is a leap year.")
                print(f"February of {year} has 29 days.")
            else:
                print(f"The year {year} is not a leap year.")
                print(f"February of {year} has 28 days.")
        else:
            print(f"The year {year} is a leap year.")
            print(f"February of {year} has 29 days.")
    else:
        print(f"The year {year} is not a leap year.")
        print(f"February of {year} has 28 days.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
