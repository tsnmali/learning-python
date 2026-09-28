# asks for two numbers
# asks for an operation (+ - * /)
# performs the calculation
# handles invalid input safely

# Skills Tested
# input()
# functions
# if/elif/else
# float conversion
# try/except
# ZeroDivisionError
# ValueError
# validation logic
# f-strings

# Requirements
# Must:
# reject invalid operators
# reject non-numeric input
# prevent divide-by-zero crashes
# print user-friendly error messages
# round results to 2 decimals
# Bonus
# Add:
# continuous loop until user types "quit"

#  ================================================================ #

# Use input to ask for 2 numbers but reject any non-numerical values,
# Use input to ask for an operation, reject invalid operators
# Perform the calcuation of the 2 numbers based on the chosen operation, prevent division by zero, round any results to 2 decimals
#
while True:
    def chosen_numbers():
        while True:
            try:
                user_number_1 = float(input("Enter a number: "))
                user_number_2 = float(input("Enter another number: "))
                break

            except ValueError:
                print("That's not a valid number.")
                continue

        return user_number_1, user_number_2
    user_number = chosen_numbers()

    def get_operator():
        correct_operators = ["+", "-", "*", "/"]
        while True:
            user_operator = input("Enter an operation. Choose either +. -, *, /: ")
            if user_operator in correct_operators:
                break
            else:
                print("That's not a valid operator. ")

        return user_operator
    chosen_operator = get_operator()

    def operators():

        operations = {
            "+": lambda user_number_1, user_number_2: user_number_1 + user_number_2,
            "-": lambda user_number_1, user_number_2: user_number_1 - user_number_2,
            "*": lambda user_number_1, user_number_2: user_number_1 * user_number_2,
            "/": lambda user_number_1, user_number_2: user_number_1 / user_number_2,

        }
        return operations
    my_operations = operators()

    try:
        equation_result = my_operations[chosen_operator](user_number[0], user_number[1])
        print(f"The result for this equation is: {round(equation_result, 2)} ") #You can also do (*user_number). The use of "*" unpacks several iterable types without you having to manually do it yourself.
        break

    except ZeroDivisionError:
        print("You can't divide by zero. ")
        continue











# make a new variable that combines the users operator and numbers and use the function's dictionary to choose the correct operations based on the users chosen operator















