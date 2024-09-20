"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 1.2.1 - Road Trip
Date: 08/26/2024

Description:
    A simple python program to estmate the cost of road trip 

Contributors:
    Name, login@purdue.edu [repeat for each]

My contributor(s) helped me:
    [ ] understand the assignment expectations without
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
    
    print("Road trip fuel cost estimator:")

    # User inputs below:
    distance = float(input("  How far away is your destination (miles)? "))
    fuel_price = float(input("  What is the average price of gas (dollars per gallon)? "))
    fuel_efficiency = float(input("  What is the fuel efficiency of your vehicle (mpg)? "))
    
    # Calculation of trip cost
    trip_cost = int(2 * (distance) * (fuel_price) / (fuel_efficiency))
    
    # Display the trip cost
    print(f"\nThe fuel cost for this trip is approximately ${trip_cost}." )

    



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
