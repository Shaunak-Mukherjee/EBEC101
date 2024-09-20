"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 2.2.4. Time Calculator
Date: 09/03/2024

Description:
This simple python program asks the user to enter a number in seconds 
and displays the time entered in days, hours, minutes and seconds so 
it can be a neat time calculator.

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
   
def main():
    # Input 
    time = int(input("Please enter a time in seconds: "))

    # Calculate days, hours, minutes, and seconds
    days = time // 86400
    hours = (time % 86400) // 3600
    minutes = (time % 3600) // 60
    seconds = time % 60

    # When input time is less than a minute
    if time < 60:
        print(f"  {time} seconds is less than one minute.")
        return
    elif time == 60:
        print(f"  {time} seconds equals 1 minute(s).")
        return

    # Case for time greater than 60 seconds
    print(f"  {time:,} seconds equals", end='')

    # Add days to the output 
    if days > 0:
        print(f" {days} day(s)", end='')

    # Add hours to the output 
    if hours > 0:
        if days > 0:
            if minutes > 0 or seconds > 0:
                print(", ", end='')
            else:
                print(" and ", end='')
        print(f" {hours} hour(s)", end='')

    # Add minutes to the output 
    if minutes > 0:
        if (days > 0 or hours > 0) and seconds == 0:
            print(" and", end='')
        elif days > 0 or hours > 0:
            print(", ", end='')
        print(f" {minutes} minute(s)", end='')

    # Add seconds to the output 
    if seconds > 0:
        if days > 0 or hours > 0 or minutes > 0:
            print(" and", end='')
        print(f" {seconds} second(s)", end='')

    print('.')  # End the sentence with a period

"""Do not change anything below this line."""
if __name__ == "__main__":
    main()
