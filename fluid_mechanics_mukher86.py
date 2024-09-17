"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 2.2.5. Fluid Mechanics
Date: 09/05/2024

Description:
This simple python program asks the user to enter a number in seconds 
and displays the time entered in days, hours, minutes and seconds so 
it can be a neat time calculator.

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
    # Add user inputs for temp, vel and dia 
    temperature = int(input("Enter the temperature in °C as 5, 20, or 50: "))
    velocity = float(input("Enter the velocity of water in the pipe (m/s): "))
    diameter = float(input("Enter the pipe's diameter (m): "))

    # Conditions for temp vs viscocity 
    if temperature == 5:
        viscosity = 1.52E-6
    elif temperature == 20:
        viscosity = 1.00E-6
    elif temperature == 50:
        viscosity = 5.54E-7    


    # Calculation of Re
    r_e = (velocity * diameter)/viscosity
    
    # Final output
    print(f"At {temperature:.1f}\u00b0C, the Reynolds number for flow at {velocity} m/s in a {diameter} m diameter pipe is {r_e:.2e}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
