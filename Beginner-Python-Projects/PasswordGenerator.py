# This is a password generator
import random

# Character lists
uppercase_letters = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T',
                     'U', 'V', 'W', 'X', 'Y', 'Z']
lowercase_letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
                     'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '_', '=', '+',
           '[', ']', '{', '}', '\\', '|', ';', ':', '\'', '"', ',', '<', '>', '.', '/', '?', '`', '~']


# Function to generate a password
def generate_password(length=12):
    # Ensure at least one character from each category
    password = [
        random.choice(uppercase_letters),
        random.choice(lowercase_letters),
        random.choice(numbers),
        random.choice(symbols)
    ]

    # Fill the rest randomly from all categories
    all_characters = uppercase_letters + lowercase_letters + numbers + symbols
    password += random.choices(all_characters, k=length - len(password))

    # Shuffle to randomize order
    random.shuffle(password)

    return "".join(password)


# Welcome message
print("Welcome to Password Generator! \n")
user_name = input("To begin, please enter a username:  ")

# Validate username input
if (any(char in user_name for char in uppercase_letters) and
        any(char in user_name for char in lowercase_letters) and
        any(char in user_name for char in numbers)):

    print("Now the system will generate a custom password. \n")
    print("==== \n")

    # Generate password
    password = generate_password()

    # Create hashed version of the password
    hashed_password = "*" * len(password)

    # Display the hashed password
    print(f"Your password: {hashed_password}")
    print(f"It is {len(password)} characters long.")

    # Ask user if they want to unveil their password
    unveil = input("Would you like to see your password? (yes/no): ").strip().lower()

    if unveil == "yes":
        print(f"Your password is: {password}")
    elif unveil == "no":
        print("Thank you for using the password generator!")
    else:
        print("Invalid output!")

else:
    print("Invalid input! Username must contain at least one uppercase letter, one lowercase letter, and one number.")
