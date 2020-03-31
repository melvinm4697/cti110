# This program will calculate total bugs collected over 5 days
# March 31, 2020
# CTI-110 P4T2 - Bug Collector
# Morineki Melvin
#
# Set total to 0
# Enter bugs collected each day for five days
# Add the bugs collected for the five days
# Display the total amount of bugs collected

total = 0

for day in range(1, 6):
    print('Day', day, 'bugs collected: ')
    bugs = int(input())
    total = total + bugs

print('Total bugs collected: ', total)
