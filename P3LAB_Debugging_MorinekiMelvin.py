# CTI-110
# P3LAB - Debugging
# Morineki Melvin
# March 24, 2020
#
# This program is to debug a previously written
# program that is not working properly.
# Orignal program was written without proper
# indentation and alignment.

# User inputs their numeric grade
# Program runs through code to find the correct alphabet grade
# Program displays user's alphabet grade

# Named constants to represent the grade threshholds
A_SCORE = 90
B_SCORE = 80
C_SCORE = 70
D_SCORE = 60

# Get a test score from the user.
score = int(input("Enter your test score: "))

#Determine the grade.
if score >=A_SCORE:
    print("Your grade is A.")
else:
    if score >=B_SCORE:
        print("Your grade is B.")
    else:
        if score >=C_SCORE:
            print("Your grade is C.")
        else:
            if score >=D_SCORE:
                print("Your grade is D.")
            else:
                print("Your grade is F.")
