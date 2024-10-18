"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 8.2.2. Phone Number Converter
Date: 10/18/2024

Description:
This Python program converts a telephone number containing alphabetic 
characters into its numeric equivalent. It processes each character in 
the input string, replacing letters with their corresponding digits while 
preserving any digits or punctuation. The program ensures both uppercase 
and lowercase letters are handled correctly.

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
   

# Function to convert alphabetic characters 
def convert_number(phone_number):
    # Create dictionary 
    letter_to_digit = {'A': '2', 'B': '2', 'C': '2', 'D': '3', 'E': '3', 'F': '3', 
                       'G': '4', 'H': '4', 'I': '4', 'J': '5', 'K': '5', 'L': '5', 'M': '6', 
                       'N': '6', 'O': '6', 'P': '7', 'Q': '7', 'R': '7', 'S': '7', 'T': '8', 
                       'U': '8', 'V': '8', 'W': '9', 'X': '9', 'Y': '9', 'Z': '9'}

    # Initialize empty string
    converted_phone_number = ""


    for char in phone_number:
        if char.isalpha():
            converted_phone_number += letter_to_digit[char.upper()]
        else:
            converted_phone_number += char

    return converted_phone_number


def main():
    # User input
    phone_number = input("Enter a telephone number: ")

    # Convert the phone number 
    converted_number = convert_number(phone_number)

    # Print 
    print(f"  {phone_number}")
    print(f"  {converted_number}")


"""Do not change anything below this line."""
if __name__ == "__main__":
    main()


