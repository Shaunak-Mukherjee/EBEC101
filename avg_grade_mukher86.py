"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 4.2.3. Avg Grade
Date: 09/18/2024

Description:
This program asks user to input grades five times and calculates
the letter grade following average score and final letter grade.

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
   
# Check if score is valid
def get_valid_score():
    while True:
        try:
            score = float(input("Enter a score: "))
            if 0 <= score <= 100:
                return score
            else:
                print("  Invalid Input. Please try again.")
        except ValueError:
            print("  Invalid Input. Please try again.")

# Function that determines the letter grade based on the score
def determine_grade(score):
    if 92 <= score <= 100:
        return "A"
    elif 82 <= score < 92:
        return "B"
    elif 73 <= score < 82:
        return "C"
    elif 64 <= score < 73:
        return "D"
    else:
        return "F"

# Calculate the average score
def calc_average(scores):
    if not scores:
        return 0
    return sum(scores) / len(scores) 

def main():
    # Empty list to collect all 5 scores
    scores = []
    
    # Collect 5 valid scores
    for _ in range(5):
        score = get_valid_score()
        scores.append(score)
        grade = determine_grade(score)
        print(f"  The letter grade for {score} is {grade}.")
    
    # Calculate and display the average score and final letter grade
    average_score = calc_average(scores)
    average_grade = determine_grade(average_score)
    print("\nResults:")
    print(f"  The average score is {average_score:.2f}.")
    print(f"  The letter grade for {average_score:.2f} is {average_grade}.")

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
