"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 8.2.5. Number Reader
Date: 10/22/2024

Description:
This program reads random numbers from a file named random_numbers.txt and calculates 
various statistics, including the total count, minimum, maximum, sum, and average of 
the numbers. It displays the results in a formatted output, making it easy to read and 
understand. The program ensures that the values are presented with appropriate comma 
separators for clarity.

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

# Reads numbers from a file and returns them as a list of integers.
def read_numbers_from_file(filename="random_numbers.txt"):
    
    with open(filename, 'r') as file:
        numbers = [int(line.strip()) for line in file]
    return numbers
# Displays the statistics for a list of numbers.
def display_statistics(numbers):
    
    count = len(numbers)
    minimum = min(numbers)
    maximum = max(numbers)
    total_sum = sum(numbers)
    average = total_sum / count

    print(f"{count:,} numbers were read from the file.")
    print(f"Min: {minimum:,}")
    print(f"Max: {maximum:,}")
    print(f"Sum: {total_sum:,}")
    print(f"Avg: {average:,.1f}")

def main():
    # Main function
    numbers = read_numbers_from_file()
    display_statistics(numbers)

if __name__ == "__main__":
    main()






