"""
Author: Shaunak Mukherjee, mukher86@purdue.edu
Assignment: 9.2.3. Course Info
Date: 10/26/2024

Description:
This program retrieves and displays details for a specific course, 
including room, instructor, and time, based on a user-provided 
course number. It validates the course number and informs the user 
if the course is invalid.

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

def get_course_data():
    # Return a dictionary with course data for room, instructor, and time
    return {
        'CS101': {'room': '1461', 'instructor': 'Django', 'time': '9:00 a.m.'},
        'CS102': {'room': '4815', 'instructor': 'Idle', 'time': '11:00 a.m.'},
        'AB203': {'room': '3634', 'instructor': 'Rich', 'time': '10:00 a.m.'},
        'NT110': {'room': '1188', 'instructor': 'Marshal', 'time': '2:00 p.m.'},
        'CM241': {'room': '2451', 'instructor': 'Pickle', 'time': '12:00 p.m.'}
    }

def main():
    # Load course data
    course_data = get_course_data()
    
    # Prompt user 
    course_number = input("Enter a course number: ").strip()
    course = course_data.get(course_number)

    # Display course details 
    if course:
        print(f"  The details for course {course_number} are:")
        print(f"    Instructor: {course['instructor']}")
        print(f"          Room: {course['room']}")
        print(f"          Time: {course['time']}")
    else:
        print(f"  {course_number} is an invalid course number.")

if __name__ == "__main__":
    main()







