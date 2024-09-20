"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 2.2.3. Roulette Colors
Date: 09/03/2024

Description:
This python program is called roulette color and it 
asks users to choose a pocket number, and then displays 
the color of the pocket. The pocket is between 0 and 36.

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

# user input
    pocket = int(input("Please choose a pocket number: "))

    # Determine the color based on the pocket number
    if pocket < 0 or pocket > 36:
        print("  Invalid Input!")

    elif pocket == 0:
        print(f"  Pocket number {pocket} is green.")

    elif 1 <= pocket <= 10 or 19 <= pocket <= 28:
        if pocket % 2 == 0:
            print(f"  Pocket number {pocket} is black.")
        else:
            print(f"  Pocket number {pocket} is red.")
            
    elif 11 <= pocket <= 18 or 29 <= pocket <= 36:
        if pocket % 2 == 0:
            print(f"  Pocket number {pocket} is red.")
        else:
            print(f"  Pocket number {pocket} is black.")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()



