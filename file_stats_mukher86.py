"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 8.2.3. File Stat
Date: 10/22/2024

Description:
his program reads a text file, counts the total number of words and non-blank lines, 
and calculates the average number of words per non-blank line. It then prints these 
statistics, while handling cases where the file might not be found.

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
   

def file_stats(filename):
    try:
        # Open the file
        with open(filename, 'r') as file:
            lines = file.readlines()

        # Initialize counters
        total_words = 0
        total_lines = 0

        
        for line in lines: 
            stripped_line = line.strip()

            
            if stripped_line != "":
                total_lines += 1
                words_in_line = stripped_line.split()
                total_words += len(words_in_line)

        # Calculate the average words per line
        if total_lines > 0:
            avg_words_per_line = total_words / total_lines
        else:
            avg_words_per_line = 0

        # Print the results
        print("Total number of words:", total_words)
        print("Total number of lines:", total_lines)
        print("Average number of words per line:", round(avg_words_per_line, 1))

    except FileNotFoundError:
        print("Error: The file was not found.")

def main(filename="frontiero_v_richardson.txt"):
    file_stats(filename)

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()



