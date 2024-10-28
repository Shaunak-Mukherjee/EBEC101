"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 9.2.2. World Series
Date: 10/26/2024

Description:
This program loads and organizes World Series winner data into dictionaries 
for team win counts and yearly winners. It allows users to input a year to see 
the winning team and the total number of times that team has won, handling 
special cases where the Series was not played.

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

def load_winners_data(filename="WorldSeriesWinners.txt"):
    # Dictionary to store each team's win count
    team_wins = {}  
    # Dictionary to store the winning team for each year
    year_winner = {}  

    with open(filename) as file:
        lines = file.read().splitlines()

        # Starting year for the World Series
        current_year = 1903

        for team in lines:
            # Skip the years when the World Series wasn't held
            if current_year == 1904 or current_year == 1994:
                current_year += 1

            # Increment the team's win count
            if team not in team_wins:
                team_wins[team] = 0
            team_wins[team] += 1

            # Record the winner
            year_winner[current_year] = team
            current_year += 1  

    return team_wins, year_winner


def main():
    # Load data
    team_wins, year_winner = load_winners_data()
    
    # Prompt user for a year
    year = int(input("Enter a year in the range 1903 -- 2023: "))

    # Check 
    if year in year_winner:
        team = year_winner[year]
        print(f"  The {team} won the World Series in {year}.")
        print(f"  They have won the World Series {team_wins[team]} times.")
    elif year == 1904 or year == 1994:
        print(f"  The World Series wasn't played in the year {year}.")
    else:
        print(f"  Data for the year {year} is not included in this system.")


if __name__ == "__main__":
    main()





