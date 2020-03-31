# CTI-110
# P3HW2 - BasicMath
# Morineki Melvin
# March 17, 2020
#
# This program will take two numbers that the user inputs
# as well as a menu choice to either
# add, multiply, subtract the numbers, exit the program
# or display an error if the correct menu choice is not chosen
#
# User inputs two numbers
# User chooses a menu number (1 - 4)
# Menu choice will add (1), multiply (2) or
# subtract (3) numbers and show the result
# menu choice 4 will exit the program and no answer will display
# If menu choice is not 1 - 4, then an error will display
#
# User inputs their numbers
input_1 = float(input("Enter your first number: "))
input_2 = float(input("Enter your second number: "))

# User is shown menu
print("Choose a menu option")
print (" 1. add")
print (" 2. multiply")
print (" 3. subtract")
print (" 4. end")
choice = int(input("What operation would you like to perform? "))

# User chooses a menu option
if choice == 1:
    answer1 = input_1 + input_2
    print("Your answer is: ", format(answer1, " .2f"))
elif choice == 2:
    answer2 = input_1 * input_2
    print("Your answer is: ", format(answer2, " .2f"))
elif choice == 3:
    answer3 = input_1 - input_2
    print("Your answer is: ", format(answer3, " .2f"))
elif choice == 4:
    print("You have chosen to exit program.")
else:
    print("You have chosen an incorrect menu option.")
