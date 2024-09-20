"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 2.2.2. Software Sales
Date: 09/02/2024

Description:
This python program estimates the quantity discount on a 
software package. It asks the user to enter the number of 
packages purchased and then displays the amount of the discount 
and the total amount of the purchase after the discount.

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
    packages = int(input("How many packages will be purchased: "))

    each_unit_price = 880

    # Discount rates 
    discount = [0.10, 0.15, 0.30, 0.42]
    discount_rate = 0  

    # Determine the appropriate discount and total price
    if packages < 0:
        print("  Invalid Input!")
        return
    elif packages >= 4 and packages <= 39:
        discount_rate = discount[0]
        print(f"  {int(discount_rate * 100)}% discount applied.")
    elif packages >= 40 and packages <= 199:
        discount_rate = discount[1]
        print(f"  {int(discount_rate * 100)}% discount applied.")
    elif packages >= 200 and packages <= 999:
        discount_rate = discount[2]
        print(f"  {int(discount_rate * 100)}% discount applied.")
    elif packages >= 1000:
        discount_rate = discount[3]
        print(f"  {int(discount_rate * 100)}% discount applied.")
    elif packages > 0 and packages < 4:
        print("  No discount applied.")

    # Calculate and show total price after applying discount
    total_price = round(packages * each_unit_price * (1 - discount_rate), 2)
    print(f"  The total price to purchase {packages} packages is ${total_price:,.2f}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()



