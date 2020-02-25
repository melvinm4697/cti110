# What is the profit from total sales?
# February 20, 2020
# CTI-110 P2T1 - Sales Prediction
# Morineki Melvin
#
# Input the total sales
# Multiply total sales by 23 percent
# Display the profit
#
# Input the total sales
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales
profit = total_sales * 0.23

# Display the annual profit
print('The profit is $', format (profit, ',.2f'))
