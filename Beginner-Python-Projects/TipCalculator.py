# A simple program that calculates your total bill.

# As the user for the total bill. Cents included!
bill = float(input("Welcome to the tip calculator! \nWhat was the total bill? $ "))

# Ask the user for the amount of tips they wish to pay.
tip = int(input("How much tip would you like to give in tips? 10, 12, or 15? "))

# As the user for how many will split the bill.
split_bill = int(input("How many people split the bill? "))

# Calculate the total bill by multiplying the original bill by the tip and dividing that sum by 100. Add the output to the bill and then divide
# by the total number of people.
total_bill = (bill + (bill * tip / 100)) / split_bill

# Print the total bill rounded to 2 decimal places.
print(f"Each person should pay: ${total_bill:.2f} - We hope you enjoyed your meal!")
