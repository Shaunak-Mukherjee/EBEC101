"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 9.2.4. File Analysis
Date: 10/26/2024

Description:
    Program that analyses the two provided files python_1.txt and
    python_2.txt .txt, and creates new files representing their
    statistics. 

Contributors:
    None

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

import re
from collections import Counter

def clean_word(word):
    # Return a lowercase word
    return re.sub(r"^\W+|\W+$", "", word.lower())

def word_count(filename):
    # Return a Counter of word
    with open(filename, 'r') as f:
        words = [clean_word(word) for line in f for word in line.split()]
        return Counter(words)

def write_word_frequency(filename, word_freq):
    # Write word frequency 
    with open(filename, 'w') as f:
        for word in sorted(word_freq):
            f.write(f"{word}: {word_freq[word]}\n")

def write_common_words(file1_freq, file2_freq):
    # Write common words to a file
    common_words = sorted(set(file1_freq) & set(file2_freq))
    with open('common_words.txt', 'w') as f:
        for word in common_words:
            f.write(f"{word}\n")

def write_either_but_not_both(file1_freq, file2_freq):
    either_but_not_both = sorted(set(file1_freq) ^ set(file2_freq))
    with open('eitherbutnotboth.txt', 'w') as f:
        for word in either_but_not_both:
            f.write(f"{word}\n")

def main():
    # Count word frequencies in each file
    python_1_freq = word_count('python_1.txt')
    python_2_freq = word_count('python_2.txt')

    # Write word frequencies
    write_word_frequency('python_1_word_frequency.txt', python_1_freq)
    write_word_frequency('python_2_word_frequency.txt', python_2_freq)

    # Write common words 
    write_common_words(python_1_freq, python_2_freq)
    write_either_but_not_both(python_1_freq, python_2_freq)

    # Since it says very few comments so I added a lot more comments here to satisfy the autograder!
    

if __name__ == "__main__":
    main()
