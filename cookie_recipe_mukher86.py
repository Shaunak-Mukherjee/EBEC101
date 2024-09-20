"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 1.2.3. Cookie Recipe
Date: 08/27/2024

Description:
    This python program asks the user how many cookies they want to bake 
    and then calculates and displays the amount of each ingredient needed 
    to make that specific number of cookies.

Contributors:
    Name, login@purdue.edu [repeat for each]

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
    cookies = int(input("How many cookies do you want to make? "))

    # Ingredient for 48 cookies
    butter_per_cookie = 1.25 / 48
    sugar_per_cookie = 1.5 / 48
    flour_per_cookie = 2.5 / 48

    # Calculate the ingredients needed
    butter_need = butter_per_cookie * cookies
    sugar_need = sugar_per_cookie * cookies
    flour_need = flour_per_cookie * cookies

    # Format and display the results
    print(f"To make {cookies:,} cookies, you will need:")
    print(f"{butter_need:10,.2f} cups of butter")
    print(f"{sugar_need:10,.2f} cups of sugar")
    print(f"{flour_need:10,.2f} cups of flour")
    


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
