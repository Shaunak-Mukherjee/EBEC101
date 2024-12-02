"""
Assignment: 12.2.1. Final Project
Author: Shaunak Mukherjee, mukher86@purdue.edu
Date: 11/27/2024

Description:
This is the final project - Code Breakers. 

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

import random
import os
import json
import textwrap
from datetime import datetime
import re

# Define function to generate the secret code
def generate_solution(min_length=4, max_length=6):
    length = random.randint(min_length, max_length)
    return ''.join(random.choices('012345', k=length))
    

class CodeBreakerGame:
    def __init__(self):
        self.solution = None
        self.attempts_left = 10
        self.history = []


    def save_game(self):
        save_manager = SaveManager()
        save_slots, file_map = save_manager.list_save_files()

        print("\nFiles:")
        print("--------------------------------------------------------------------------")
        for idx, slot in enumerate(save_slots, start=1):
            print(f"   {idx}: {slot}")
        

        while True:
            choice = input("What save would you like to overwrite (1, 2, 3, or c to cancel): ").strip().lower()

            if choice == 'c':
                print("cancelled")
                display_board(self.solution, self.history, attempts_left_none=False)

                initial_guess = input("What is your guess (q to quit, s to save and quit): ").strip()
                return 
                
            


            if not choice.isdigit() or int(choice) < 1 or int(choice) > len(save_slots):
                print("That is an invalid selection.")
                continue

            # Prompt for player name
            while True:
                player_name = input("What is your name (no special characters): ").strip()
                if re.match(r'^[a-zA-Z0-9 ]+$', player_name):
                    break
                else:
                    print("That is an invalid name.")

            # Save game details
            slot_index = int(choice) - 1
            filename = f"save_slot_{slot_index + 1}.json"
            save_data = {
                "name": player_name,
                "date": datetime.now().isoformat(timespec="seconds"),
                "solution": self.solution,
                "attempts_left": self.attempts_left,
                "history": self.history,
            }

            with open(filename, "w") as file:
                json.dump(save_data, file)
            # print(f"Game saved to slot {choice} as '{player_name}' at {save_data['date']}.")
            print(f"Game saved in slot {choice} as {player_name}.")
            return



                
    def load_game(self):
        save_slots, file_map = SaveManager.list_save_files()

        if not save_slots:
            print("No saved games found.")
            return None, None, None

        print("\nFiles:")
        print("--------------------------------------------------------------------------")

        for idx, slot in enumerate(save_slots, start=1):
            print(f"   {idx}: {slot}")
        # print("   c: Cancel")

        while True:
            choice = input("What save would you like to load (1, 2, 3, or c to cancel): ").strip().lower()
            if choice == 'c':
                print("cancelled")
                return None, None, None

            if choice.isdigit() and 1 <= int(choice) <= len(save_slots):
                selected_slot = save_slots[int(choice) - 1]
                filename = file_map.get(selected_slot, None)
            if filename:
                try:
                    if not os.path.isfile(filename) or os.stat(filename).st_size == 0:
                        print("That file is empty!")
                        continue

                    with open(filename, "r") as file:
                        data = json.load(file)

                    return data.get('solution'), data.get('attempts_left'), data.get('history')
                except (IOError, json.JSONDecodeError) as e:
                    print(f"Error loading game: {e}")
                    return None, None, None

            else:
                print("That file is empty!")



class SaveManager:
    @staticmethod
    def list_save_files():
        save_files = [f for f in os.listdir('.') if f.startswith('save_slot_') and f.endswith('.json')]
        slots = []
        file_map = {}
        for i in range(1, 4): 
            filename = f"save_slot_{i}.json"
            if filename in save_files:  
                with open(filename, "r") as file:
                    data = json.load(file)
                display_name = f"{data['name']} - Time: {data['date']}"
                slots.append(display_name)
                file_map[display_name] = filename
            else:
                slots.append("empty")
                file_map[f"empty_{i}"] = filename  

        return slots, file_map


class GameMenu:
    def __init__(self):
        self.game = CodeBreakerGame()

    # Display the main menu
    def display_menu(self):
        print("\nMenu:")
        print("--------------------------------------------------------------------------")
        print("   1: Rules")
        print("   2: New Game")
        print("   3: Load Game")
        print("   4: Quit")

    # Display the game rules
    def display_rules(self):
        print("\nRules:")
        print("--------------------------------------------------------------------------")
        print("1. You get 10 guesses to break the lock.")
        print("\n2. Guess the correct code to win the game.")
        print("\n3. Codes can be either 4, 5, or 6 digits in length.")
        print("\n4. Codes can only contain digits 0, 1, 2, 3, 4, and 5.")
        print("\n5. Clues for each guess are given by a number of red and white pins.")
        print()
        print("   a. The number of red pins in the R column indicates the number of digits")
        print("      in the correct location.")
        print("   b. The number of white pins in the W column indicates the number of")
        print("      digits in the code, but in the wrong location.")
        print("   c. Each digit of the solution code or guess is only counted once in the")
        print("      red or white pins.")

    # Get player's choice from the menu
    def get_player_choice(self):
        while True:
            choice = input("Choice: ")
            if choice in ['1', '2', '3', '4']:
                return int(choice)
            print("Please enter 1, 2, 3, or 4.")
            self.display_menu()


def display_board(solution, history, attempts_left_none=False):
    
    print("   ==================+=====")
    
    
    if not attempts_left_none:
        if not history or solution != history[-1][0]:
            print("    o  o  o  o  o  o | R W  ")  
        else:
            print("    " + "  ".join(k for k in list(solution.ljust(6, 'o'))) + " | R W  ")
        # print("   ==================+=====")
    else:
        print("    " + "  ".join(k for k in list(solution.ljust(6, 'o'))) + " | R W  ")
        # print("   ==================+=====")
    print("   ==================+=====")

    

    # If there is a winning guess
    if history and history[-1][0] == solution:
        
        guess, feedback = history[-1]
        guess_display = "    " + "  ".join(guess.ljust(6, 'o'))
        feedback_display = f"{feedback[0]} {feedback[1]}"
        # print(f"{guess_display} | {feedback_display}  ")
        # history = history[1:]  # Remove the winning guess from the history

    # Print empty rows for remaining guesses (if needed)
    for _ in range(11 - len(history)-1):  
        print("    " + "  ".join("o" for _ in range(6)) + " | 0 0  ")  

    # Print guesses from bottom to top 
    for guess, feedback in reversed(history):
        guess_display = "    " + "  ".join(guess.ljust(6, 'o'))
        feedback_display = f"{feedback[0]} {feedback[1]}"
        print(f"{guess_display} | {feedback_display}  ")  

    print("   ==================+=====")



# Validate the player's guess
def validate_guess(guess, solution_length):

    if guess is None or guess == "":
        return False, "This is too short.\nGuess lengths must be between 4 and 6."

    if not guess.isdigit():
        return False, "It must be only numbers!"
    
    if len(guess) < 4:
        return False, "This is too short.\nGuess lengths must be between 4 and 6."
    
    if len(guess) > 6:
        return False, "This is too long.\nGuess lengths must be between 4 and 6."
    
    if any(char not in '012345' for char in guess):
        return False, "It must be only numbers 0 through 5."
    
    if len(guess) < 6:
        guess = guess.ljust(6, 'o')
    
    return True, guess



# Calculate feedback (red and white pins) based on the guess
def calculate_feedback(guess, solution):
    reds = sum(1 for g, s in zip(guess, solution) if g == s)
    unmatched_guess = [g for g, s in zip(guess, solution) if g != s]
    unmatched_solution = [s for g, s in zip(guess, solution) if g != s]
    whites = 0
    for digit in set(unmatched_guess):
        whites += min(unmatched_guess.count(digit), unmatched_solution.count(digit))
    return reds, whites


def game_loop(game):
    while game.attempts_left > 0:    
        # Pass the solution to the display_board function
        display_board(game.solution, game.history)
        # print(game.solution)     

        guess = None
        while not guess:  
            initial_guess = input("What is your guess (q to quit, s to save and quit): ").strip()

            if initial_guess.lower() == 'q':
                print("Ending Game.")
                return  

            elif initial_guess.lower() == 's':
                game.save_game()
                
                print("Ending Game.")
                return  # Save and exit

            valid, message = validate_guess(initial_guess, len(game.solution))
            if not valid:
                print(f"Your guess was \"{initial_guess}\". {message}")
            else:
                guess = initial_guess
                

        feedback = calculate_feedback(guess, game.solution)
        game.history.append((guess, feedback))
        game.attempts_left -= 1

        if feedback[0] == len(game.solution):
            display_board(game.solution, game.history)
            game.history.insert(0, (guess, (feedback[0], feedback[1])))  
            print("Congratulations, you broke the lock!")
            print("The grades are safe!")

            
            
            break  # Exit if won

    if game.attempts_left == 0:
        display_board(game.solution, game.history,attempts_left_none=True)

   
        
        print("You hear a machine yell OUT OF TRIES!")
        print("  ...")
        print("Is that burning you smell?")
        print("  ...")
        print("OH, NO! It looks like IU has destroyed all the EBEC grades!")
        print()

        
       

# Main function
def main():
    intro_text = """
    You are a member of the Unladened Swallow Society, tasked with cracking
    the notorious Holy Grail lock. This lock secures a vault containing all
    the EBEC grades, locked away by IU. To retrieve your grades, you'll need
    to break through this lock. Fortunately, the creators at IU made an error
    when building it, so the lock will provide hints about the code. However,
    you don't know the passcode length and only have 10 guesses. Use them
    wisely--if you fail, you could be turned into a newt, the grades might be
    destroyed, or, even worse, you might have to rewrite the time calculator!
    
    Will you be able to break this lock before your grades are lost forever?
    """
    print(textwrap.dedent(intro_text).strip())

    menu = GameMenu()
    while True:
        menu.display_menu()
        choice = menu.get_player_choice()

        if choice == 1:
            menu.display_rules()
        elif choice == 2:
            menu.game.solution = generate_solution(min_length=4, max_length=6)
            
            menu.game.history = []
            menu.game.attempts_left = 10
            print("\nNew Game:")
            print("--------------------------------------------------------------------------")
            game_loop(menu.game)
        elif choice == 3:
            solution, attempts_left, history = menu.game.load_game()
            if solution:
                menu.game.solution = solution
                menu.game.attempts_left = attempts_left
                menu.game.history = history
                # print("\nLoaded Game:")
                print("\nResume Game:")
                print("--------------------------------------------------------------------------")
                game_loop(menu.game)

        elif choice == 4:
            print("Goodbye")                  
            break

# Start the game
if __name__ == "__main__":
    main()
