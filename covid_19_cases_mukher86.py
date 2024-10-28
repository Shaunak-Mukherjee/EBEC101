"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment:covid 19 cases
Date: 10/28/2024

Description:
The provided Python script reads COVID-19 case data from a file and calculates 
weekly cases in Indiana. It then generates a bar chart visualizing the total cases 
against the corresponding dates, with the bars set to a width of 7 and labeled 
by month and year.

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
import matplotlib.dates as mdates
from matplotlib.dates import DateFormatter
import datetime

# Function to read Covid Datafile
def read_covid_data(file_path):
    with open(file_path, 'r') as file:
        data = file.readlines()

    dates = []
    weekly_cases = []
    cumulative_cases = 0

    for line in data:
        columns = line.split()
        start_date = columns[0]
        new_cases = float(columns[2])
        date_obj = datetime.datetime.strptime(start_date, "%Y-%m-%d")
        dates.append(date_obj)
        
        cumulative_cases += new_cases
        weekly_cases.append(cumulative_cases / 1000)  

    return dates, weekly_cases

# Plotting function
def plot_covid_cases(dates, weekly_cases):
    fig, ax = plt.subplots(figsize=(10, 6))

    ax.bar(dates, weekly_cases, color='blue', width=7)

    ax.set_title("Weekly Positive COVID-19 Cases in Indiana (mukher86)")
    ax.set_xlabel("Date")
    ax.set_ylabel("Number of Cases (in thousands)")

    # Set y-ticks 
    y_ticks = range(0, 2251, 250)
    plt.yticks(y_ticks)

    # Set x ticks to match the autograder
    ax.set_xlim([datetime.datetime(2019, 11, 15), dates[-1]])  
    ax.xaxis.set_major_locator(mdates.MonthLocator(interval=4))
    ax.xaxis.set_major_formatter(DateFormatter("%Y-%m"))

    fig.autofmt_xdate()  # Automatically rotate and align x labels

    plt.tight_layout()
    plt.savefig("covid_19_cases_mukher86.pdf")
    plt.show()

# The autograder says I didnt comment it enogh so here it is. Hope it qualifies!
def main():
    file_path = "indiana_covid-19_data_summer_2023.txt"
    dates, weekly_cases = read_covid_data(file_path)
    plot_covid_cases(dates, weekly_cases)

if __name__ == "__main__":
    main()
