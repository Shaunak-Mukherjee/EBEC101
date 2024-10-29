"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 10.2.2 Gas Prices
Date: 10/29/2024

Description:
This Python script reads weekly gas prices from a text file 
and plots them on a line graph to visualize trends over the course of 2008. 
It customizes the plot with labeled axes, specified tick marks, and a grid.

Contributors:
    Name, login@purdue.edu [NA]

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

import matplotlib.pyplot as plt

# Function to read gas prices from a file and convert them to a list of floats
def get_prices():
    with open('2008_Weekly_Gas_Averages.txt', 'r') as f:
        lines = f.readlines()
        
        # Create an empty list to store the prices
        prices = []

        for line in lines:
            prices.append(float(line.strip())) 
            
        return prices

def main():
    # Define plot parameters
    prices = get_prices()
    fig, ax = plt.subplots()
    ax.plot(range(1, 53), prices)
    ax.set_title('2008 Weekly Gas Prices (mukher86)')
    ax.set_xlabel('Weeks (by number)')
    ax.set_xlim(1, 52) 
    ax.set_xticks([10, 20, 30, 40, 50])  
    ax.set_ylabel('Average Price (dollars/gallon)')
    ax.set_ylim(1.5, 4.25)  
    ax.set_yticks([1.5, 2, 2.5, 3, 3.5, 4]) 
    plt.savefig("gas_prices_mukher86.pdf")
    ax.grid()
    plt.show()


if __name__ == '__main__':
    main() 
