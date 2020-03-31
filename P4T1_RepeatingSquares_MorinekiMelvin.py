# This program draws 100 squares using nested loop
# March 24, 2020
# CTI-110 P4T1 - Repeating Squares
# Morineki Melvin
#
# Using nested loop, input the number of squares
# Input the sizes of the squares from smallest to largest
# Python turtle will draw 100 squares nested inside each other

import turtle

animation_speed = 100
distance = 3

turtle.hideturtle()
turtle.speed(animation_speed)

for count in range(100):
    for x in range(4):
        turtle.left(90)
        turtle.forward(distance)
    distance+=3
