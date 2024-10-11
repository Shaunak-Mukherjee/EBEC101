"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 7.2.4. Magic Square
Date: 10/11/2024

Description:
This Python program checks if a 3x3 grid of numbers is a Lo Shu Magic Square, 
where each row, column, and diagonal sums to 15 and contains unique numbers 
from 1 to 9. It prints the grid and displays whether or not it qualifies as 
a Lo Shu Magic Square for a given set of squares. 

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
# This function prints the 3x3 grid of the square
def print_square(square):
    print("Your square is:")
    for row in square:
        print(" ", " ".join(str(num) for num in row))

def is_magic(square):
    """This function checks if the square is a Lo Shu magic square."""
    magic_sum = 15  
    
    # Check if all elements are unique and between 1 and 9
    flat_square = [num for row in square for num in row]
    if sorted(flat_square) != list(range(1, 10)):
        return False
    
    # Check sums of rows, columns, and diagonals
    for row in square:
        if sum(row) != magic_sum:
            return False
    
    for col in range(3):
        if sum(square[row][col] for row in range(3)) != magic_sum:
            return False
    
    if (square[0][0] + square[1][1] + square[2][2]) != magic_sum:
        return False
    
    if (square[0][2] + square[1][1] + square[2][0]) != magic_sum:
        return False
    
    return True

def main():
    # Provided squares
    squares = [
        [[1, 2, 3], [4, 5, 6], [7, 8, 9]],
        [[5, 5, 5], [5, 5, 5], [5, 5, 5]],
        [[4, 9, 2], [3, 5, 7], [8, 1, 6]]
    ]
    
    # Iterate through each square, print and check if it is a Lo Shu Magic Square
    for square in squares:
        print_square(square)
        if is_magic(square):
            print("It is a Lo Shu magic square!\n")
        else:
            print("It is not a Lo Shu magic square.\n")

# No change to this block done 
if __name__ == "__main__":
    main()
