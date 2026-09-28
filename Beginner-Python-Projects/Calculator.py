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
