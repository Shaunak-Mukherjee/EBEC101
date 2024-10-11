"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 7.2.3. Roll Analysis
Date: 10/11/2024

Description:
This program simulates rolling two six-sided dice a specified number of times 
and calculates the frequency of each possible total outcome, ranging from 2 to 12. 
It generates a detailed report displaying the percentage occurrence of each total 
in a formatted table. 

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
# Import random library
import random

# Simulates rolling a single six-sided die
def roll_d6():
    
    return random.randint(1, 6)

 # Simulates rolling two six-sided dice multiple times
def get_2d6_rolls(num_rolls):
    rolls = []
    for _ in range(num_rolls):
        roll_total = roll_d6() + roll_d6()  
        rolls.append(roll_total)
    return rolls

def main():
    num_rolls = 1000000  
    roll_results = get_2d6_rolls(num_rolls)
    
    # Calculate frequencies of each possible roll total (2 to 12)
    frequency = {total: 0 for total in range(2, 13)}
    
    for result in roll_results:
        frequency[result] += 1

    # Print header
    print("Roll  Frequency")
    
    # Print the percentage for each roll total
    for roll in range(2, 13):
        # Calculate percentage of each roll outcome
        percentage = (frequency[roll] / num_rolls) * 100  
        # Format for the output
        print(f"{roll:>3} {percentage:>8.2f}%")  # Correctly aligned with spaces


# No change 
if __name__ == "__main__":
    main()

