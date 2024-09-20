"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 1.2.2. Interest
Date: 08/27/2024

Description:
    A simple python program for calculation of compound interest calculation. 
    It requires user inputs of principle, years, frequency of compounding and interest rate.

Contributors:
    Not Applicable

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
    print("Enter the following parameters.")

    # User inputs below:
    principal  = int(input("  The initial deposit? "))
    rate = float(input("  The annual interest rate in percent? "))
    years = float(input("  The number of years the account earn interest? "))
    time_compounded = int(input("  The number of times interest is compounded each year: "))

    # Convert interest rate from percentage to decimal
    converted_rate = rate / 100

    # Calculation of comp interest
    future_balance = principal*(1+ converted_rate/time_compounded)**(time_compounded*years)
    
    # Display the Future value
    print(f"The balance of this account will be ${future_balance:,.2f} after {years:.1f} years.")
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
