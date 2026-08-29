user_input = input("Enter in your grade as a whole number: ")

while True:
    try:
        comeback = int(user_input)

        if comeback < 0 or comeback > 100:
            user_input = input("Please enter in a whole number between 0 and 100: ")

            continue

        break

    except ValueError:
        user_input = input("You must enter in a whole number: ")

print("That's all for now.")




































