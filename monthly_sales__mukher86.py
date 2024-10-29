"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment:10.2.1. Monthly Sales
Date: 10/28/2024

Description:
This Python program collects monthly sales data from the user, stores it, and visualizes the data 
as a pie chart using Purdue’s secondary color palette. The chart displays each month as a labeled 
slice, with percentages shown, and saves the output as a PDF file.

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
import matplotlib.pyplot as plt

# Define the Purdue secondary color palette with proper hex formatting
colors = [
    '#5B6870',  # EverTrueBlue
    '#6E99B4',  # SlayterSkyBlue
    '#A3D6D7',  # AmeliaSkyBlue
    '#085C11',  # LandGrantGreen
    '#849E2A',  # RossAdeGreen
    '#C3BE0B',  # CeleryBogGreen
    '#E9E45B',  # SpringFestGreen
    '#6B4536',  # OakenBucketBrown
    '#B46012',  # BellTowerBrick
    '#FF9B1A',  # MackeyOrange
    '#FFD100',  # YellowWalk
    '#29A592'   # FountainRunTeal
]

# Define the months with full names for labeling
months = [
    "January", "February", "March", "April", "May", "June", "July", 
    "August", "September", "October", "November", "December"
]

# Define function to capture sales data
def get_sales_data():
    sales_data = []
    for month in months:
        d = int(input(f'Enter the sales for {month[0:3]}: '))
        sales_data.append(d)
    return sales_data

# Main function
def main():
    sales_data = get_sales_data()
    fig, ax = plt.subplots()
    ax.set_title('Monthly Sales Values (mukher86)')
    ax.pie(sales_data, labels= months, colors=colors)
    plt.savefig("monthly_sales_mukher86.pdf")  
    plt.show()
 
# No need to change below
if __name__ == '__main__':
    main()

