"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 3.2.2. Sum Average
Date: 09/10/2024

Description:
This simple python program asks the user to enter a series of 
positive only numbers, it appends the numbers into an empty lists
for cases its non negative and then calculates average and sum of
the numbers in the list.

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
    # Initialize an empty list to store numbers
    numbers = []
    
    while True:
        # Add user inputs
        num = float(input("Enter a non-negative number (negative to quit): "))
        
        # Check if the number is negative
        if num < 0:
            break
        # If not negative, add it to the list
        numbers.append(num)

    # Check if the list is empty
    if not numbers:
        print("  You didn't enter any numbers.")
    else:
        sum_numbers = sum(numbers)
        average = sum_numbers / len(numbers)
        
        # Print the sum and average of the list
        print(f"  You entered {len(numbers)} numbers.")
        print(f"  Their sum is {sum_numbers:.3f} and their average is {average:.3f}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()


