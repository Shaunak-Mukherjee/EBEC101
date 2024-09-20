"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 4.2.2. Lucky Sum
Date: 09/18/2024

Description:
This program asks user to input two integers and then it calculates
and returns the sum of the "lucky_numbers" which are basically 
all the numbers from max vs min that are divisible by 7.

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
   
def lucky_sum(num1, num2):
    # Find the smaller and larger of the two numbers
    arg_min = min(num1, num2)
    arg_max = max(num1, num2)
    
    # Lucky sum calculation 
    total_sum= 0
    for i in range(arg_min, arg_max + 1):
        if i % 7 == 0:
            total_sum += i

    return total_sum

def main():
    # Prompt the user for input
    first = int(input("Enter the first integer: "))
    second = int(input("Enter the second integer: "))
    
    # Calculate the lucky sum
    result = lucky_sum(first, second)
    
    # Display the result
    print(f"The sum of the lucky numbers is {result:,}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
