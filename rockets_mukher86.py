"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 11.2.3. Rockets
Date: 11/08/2024

Description:
The Rocket class calculates the total cost of a launch by summing the booster, upper stage, and fuel costs. 
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
class Rocket:
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost):
        self.name = name
        self.booster_cost = booster_cost
        self.upper_stage_cost = upper_stage_cost
        self.fuel_cost = fuel_cost

    def cost_per_launch(self):
        total_cost = self.booster_cost + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost ${total_cost:.2f} million per launch.")


class ReusableRocket(Rocket):
    def __init__(self, name, booster_cost, upper_stage_cost, fuel_cost, uses):
        super().__init__(name, booster_cost, upper_stage_cost, fuel_cost)
        self.uses = uses

    def cost_per_launch(self):
        # Calculate the cost of the booster 
        booster_cost_per_launch = self.booster_cost / self.uses
        total_cost = booster_cost_per_launch + self.upper_stage_cost + self.fuel_cost
        print(f"This {self.name} cost ${total_cost:.2f} million per launch.")


def main():
    # Creating instances of Rocket (non-reusable)
    atlas_v = Rocket("Atlas V", 65.4, 42.6, 0.23)
    ariane_5 = Rocket("Ariane 5", 83.5, 55.6, 0.69)
    long_march_3b = Rocket("Long March 3B", 28.5, 19.0, 2.38)
    soyuz_2 = Rocket("Soyuz 2", 20.9, 13.9, 0.24)

    # Creating an instance of ReusableRocket (reusable)
    falcon_9 = ReusableRocket("Falcon 9", 43.0, 18.6, 0.45, 23)

    # Calling cost_per_launch for each rocket
    atlas_v.cost_per_launch()
    ariane_5.cost_per_launch()
    long_march_3b.cost_per_launch()
    soyuz_2.cost_per_launch()
    falcon_9.cost_per_launch()


if __name__ == "__main__":
    main()

