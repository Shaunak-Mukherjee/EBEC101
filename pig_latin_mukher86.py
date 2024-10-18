"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 8.2.1. Pig Latin
Date: 10/16/2024

Description:
The function pig takes a Pig Latin string and translates each word 
back to English. To translate, it moves the third-to-last letter of 
each word to the beginning and removes the last two characters, 
which are always "ay".

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
   

def pig(pig_latin_str):
    # Split string 
    words = pig_latin_str.split()
    
    # Empty string 
    translated_words = []
    
    for word in words:
        # Move the third-to-last letter to the beginning and remove the last two characters
        translated_word = word[-3] + word[:-3]
        translated_words.append(translated_word)
    
    # Join the translated words and capitalize the first letter
    translated_sentence = ' '.join(translated_words).capitalize()
    
    return translated_sentence

def main():
    # Prompt user
    pig_latin_str = input("Enter a string in Pig Latin: ")
    
    # Translate Pig Latin string and print
    translation = pig(pig_latin_str)
    print(f"Translation: {translation}")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()

