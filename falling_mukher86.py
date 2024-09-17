"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 4.2.1. Falling
Date: 09/17/2024

Description:
In below code, task is to use functions in python to calculate
distance fallen by an object with different time at a given
acceleration

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
   
# Define a constant for the gravitational force
g = 8.87

# Function to calculate the falling distance
def falling_dist(time):
    # Formula to calculate the distance fallen
    distance = 0.5 * g * (time ** 2)
    return distance

# Main function
def main():
    print("Time (s)  Distance (m)")
    print("----------------------")
    
    # Loop through time values from 5 to 50 in increments of 5
    for time in range(5, 55, 5):
        distance = falling_dist(time)
        # Print 
        print(f" {time:>7} {distance:>13.1f}")



"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
