"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 3.2.3. Rainfall
Date: 09/10/2024

Description:
This simple python program asks the user to enter a series of 
numbers which are basically rainfall of different months of the year

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
    # List of months
    months = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
    
    # Use input for the number of years
    number_of_years = int(input("Enter the number of years: "))
    
    # For invalid entries
    if number_of_years <= 0:
        print("Invalid input; years must be greater than 0.")
        return  
    
    # Initialize 
    total_rainfall = 0
    total_months = 0
    
    # Nested loop
    for year in range(1, number_of_years + 1):
        print(f"  For year No. {year}")
        for month in months:
            while True:
                # Rainfall input for each month
                rainfall = float(input(f"    Enter the rainfall for {month}.: "))
                
                if rainfall < 0:
                    print("    Invalid input; rainfall cannot be negative.")
                else:
                
                    total_rainfall += rainfall
                    total_months += 1
                    break
    
    # Average rainfall per month
    average_rainfall = total_rainfall / total_months
    
    # Print summary
    print(f"There are {total_months} months.")
    print(f"The total rainfall was {total_rainfall:.2f} inches.")
    print(f"The monthly average rainfall was {average_rainfall:.2f} inches.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()



