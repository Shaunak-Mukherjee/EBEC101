"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 10.2.4. Function plot
Date: 10/28/2024

Description:
This Python program uses `matplotlib` to plot two trigonometric sine and cosine functions, 
 over the range 0 to 2pi with labeled axes, custom ticks, and a legend. 
 Then the plot is saved as a PDF with specified visual adjustments to spines and colors.

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

import math
import matplotlib.pyplot as plt

def plot_functions():
    # Generate x values from 0 to 2π 
    x = [i * 0.01 for i in range(int(0), int(2 * math.pi * 100))]

    # Define functions
    y1 = [(3 * math.cos(val)) ** 2 + 1 for val in x]
    y2 = [2 * math.sin(val ** 2) + 5 * val - 15 for val in x]

    # Create the plot
    fig, ax = plt.subplots()

    # Add colors
    ax.plot(x, y1, color='g', label=r"$(3\cos{x})^2 + 1$")
    ax.plot(x, y2, color='b', label=r"$2\sin{(x^2)} + 5x - 15$")

    # Set the title and labels
    ax.set_title("10.4 Function Plot (mukher86)", fontsize=14)
    ax.set_xlabel("x")
    ax.set_ylim(-20, 20)
    ax.set_xlim(0, 2 * math.pi)

    # Set the x-axis tick labels without an empty string
    ax.set_xticks([math.pi / 2, math.pi, 3 * math.pi / 2, 2 * math.pi])
    ax.set_xticklabels([r"$\frac{\pi}{2}$", r"$\pi$", r"$\frac{3\pi}{2}$", r"$2\pi$"])

    # Set specific y-axis ticks
    ax.set_yticks([-20, -10, 10, 20])

    # Position the spines at 'zero' instead of ('data', 0)
    ax.spines['left'].set_position('zero')
    ax.spines['bottom'].set_position('zero')
    ax.spines['top'].set_visible(False)
    ax.spines['right'].set_visible(False)
    
    # Add the legend in the bottom right
    ax.legend(loc="lower right")

    # Save the figure as a PDF with the login in the filename
    plt.savefig("function_plot_mukher86.pdf")

    # Show the plot
    plt.show()

def main():
    plot_functions()

if __name__ == "__main__":
    main()
