"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 8.2.6. Step Counter
Date: 10/22/2024

Description:
This program reads daily step counts from a file named steps.txt 
and calculates the average number of steps taken for each month of 
a non-leap year. It formats and displays the results with precise alignment 
and two decimal places for clarity. The output includes the average steps for 
each month, ensuring easy readability and consistency.

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


"""Write new functions below this line (starting with unit 4)."""

# Read the number of steps from a file and returns a list of integers
def read_steps_from_file(filename="steps.txt"):
    with open(filename, 'r') as file:
        steps = [int(line.strip()) for line in file]
    return steps

# Calculates the average steps for each month and returns a dictionary
def calculate_monthly_averages(steps):    
    days_in_month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    monthly_averages = {}
    month_names = [
        "January", "February", "March", "April", "May", "June",
        "July", "August", "September", "October", "November", "December"
    ]

    day_index = 0
    for month, days in enumerate(days_in_month):
        monthly_steps = sum(steps[day_index:day_index + days])
        monthly_average = monthly_steps / days
        monthly_averages[month_names[month]] = monthly_average
        day_index += days

    return monthly_averages

# Displays the monthly averages formatted with specified precision
def display_monthly_averages(monthly_averages):
    print("The average steps taken each month were:")
    for month, average in monthly_averages.items():
        print(f"{month:>11} : {average:8.2f}")


# Main function to read steps and display monthly averages
def main():    
    steps = read_steps_from_file()
    monthly_averages = calculate_monthly_averages(steps)
    display_monthly_averages(monthly_averages)

if __name__ == "__main__":
    main()










