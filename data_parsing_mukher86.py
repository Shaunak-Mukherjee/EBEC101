"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 7.2.1. Data Parsing
Date: 10/11/2024

Description:
This program imports gasoline proces from year 1950 to year 2021. 
It calculate the average inflation-adjusted gasoline price in the 
United States for each decade, based on historical data provided 
in a data file data.py.

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
import data

"""Write new functions below this line (starting with unit 4)."""

# List of decades to process
decades = [(1950, 1959), (1960, 1969), (1970, 1979), (1980, 1989), (1990, 1999), (2000, 2009), (2010, 2019), (2020, 2029)]

# Function to extract, parse and compute 
def extract_data(start_year, end_year, data_list):
    """Extracts and computes average inflation-adjusted price for a decade."""
    prices = [data_list[i + 3] for i in range(0, len(data_list), 4) if start_year <= data_list[i] <= end_year]
    return sum(prices) / len(prices) if prices else None

def main():
    print("          :  Price\n  Decade  : in 2021\n          : Dollars\n-------------------")
    for start_year, end_year in decades:
        avg_price = extract_data(start_year, end_year, data.data)
        if avg_price:
            print(f"{start_year}-{end_year} :  ${avg_price:.3f}")

    
"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
