"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 3.2.4. Organism
Date: 09/10/2024

Description:
This simple python program asks the user to 3 inputs such as initial
population, daily increase and a multiplication factor to estimate
the growth of an organism.

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
    starting_population = float(input("Starting population, in thousands: "))
    average_daily_increase = int(input("Average daily increase, in percent: "))
    number_of_days = int(input("Number of days to multiply: "))
   
    # Initial population
    population = starting_population

    # Setting up output 
    print(f"Day   Approx. Pop")
    # Calculate and print the population for each day
    for day in range(0, number_of_days + 1):
        print(f"{day:>3}    {f"{population:,.3f}":>10}")
        population = population * (1 + average_daily_increase / 100)

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()



