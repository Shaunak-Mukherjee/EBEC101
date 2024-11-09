"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 11.2.2. Garage
Date: 11/07/2024

Description:
The Garage class models a parking garage with attributes for name, total spaces, 
and current cars. 

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
# Main Class
class Garage:
    def __init__(self, name, spaces, cars):
        self.name = name
        self.spaces = spaces
        self.cars = cars

    def car_in(self):
        if self.cars < self.spaces:
            self.cars += 1
            print(f"Added a car to Lot {self.name}")
        else:
            print(f"Lot {self.name} is full. Can not add another car.")

    def car_out(self):
        if self.cars > 0:
            self.cars -= 1
            print(f"Removed a car from Lot {self.name}")
        else:
            print(f"Lot {self.name} is empty. There are no cars to remove.")

    def status(self):
        print(f"Lot {self.name}: {self.spaces - self.cars} out of {self.spaces} spaces are available.")

# Print the user statement
def main():
    print("Welcome to the Garage Manager!")
    garage_a = Garage("A", 10, 0)
    garage_b = Garage("B", 15, 0)

    while True:
        print("------------ Menu ------------")
        print("0. Exit")
        print("1. Print current status.")
        print("2. Add a car to A lot.")
        print("3. Add a car to B lot.")
        print("4. Remove a car from A lot.")
        print("5. Remove a car from B lot.")
        choice = int(input("Please choose an option (0-5): "))

        if choice == 0:
            print("End of the Day Garage Status:")
            garage_a.status()
            garage_b.status()
            break
        elif choice == 1:
            garage_a.status()
            garage_b.status()
        elif choice == 2:
            garage_a.car_in()
        elif choice == 3:
            garage_b.car_in()
        elif choice == 4:
            garage_a.car_out()
        elif choice == 5:
            garage_b.car_out()
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
