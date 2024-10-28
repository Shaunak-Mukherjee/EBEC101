"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 9.2.1. Capital Quiz
Date: 10/22/2024

Description:
This program quizzes users on U.S. state capitals by randomly asking 
them to name the capital of each state. 

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

import random

# Function to load state and capital data from a file
def get_state_data(filename="state_capitals.txt"):
    state_capitals = {}  
    with open(filename, 'r') as file:
        for line in file:
            
            capital, state = line.strip().split(', ')
        
            state_capitals[state] = capital
    return state_capitals

# Main function 
def main():
    state_capitals = get_state_data() 
    states = list(state_capitals.keys())  
    random.shuffle(states)  

    correct_answers = 0  
    total_questions = 0 
    incorrect_states = [] 

    # Loop until all states are answered 
    while states or incorrect_states:
        if states:
            state = states.pop(0)
        else:
            state = incorrect_states.pop(0)

        # Prompt the user for the capital of the current state
        answer = input(f"What is the capital of {state} (enter 0 to quit)? ").strip()
        
        if answer == '0':
            break       

        total_questions += 1
        if answer.lower() == state_capitals[state].lower():
            print("  That is correct!")
            correct_answers += 1  
        else:
            print(f"  That is incorrect.\n  The capital of {state} is {state_capitals[state]}.")
            incorrect_states.append(state)

    if total_questions == 0:
        print("You didn't answer any questions.")
    else:
        accuracy = (correct_answers / total_questions) * 100
        print(f"You answered {accuracy:.1f}% of the questions correctly.")

# No need to make changes below this line
if __name__ == "__main__":
    main()




