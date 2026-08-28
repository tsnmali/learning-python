import random

# User input
user_choice = int(input("What do you choose? Choose 0 for Rock, 1 for Paper, and 2 for Scissors. \n"))

# Computer's choices
choices = ["Rock", "Paper", "Scissors"]
computer_choice = random.randint(0, 2)  # Randomly select 0, 1, or 2

# ASCII art for display
ascii_art = [
    '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
    '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
    '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]

# Check user input validity
if user_choice not in [0, 1, 2]:
    print("That's not an option. Restart the program to try again.")
else:
    # Display user's choice
    print(f"You chose:\n{ascii_art[user_choice]}")

    # Display computer's choice
    print(f"The computer chose:\n{ascii_art[computer_choice]}")

    # Determine winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (user_choice == 0 and computer_choice == 2) or \
            (user_choice == 1 and computer_choice == 0) or \
            (user_choice == 2 and computer_choice == 1):
        print("You win!")
    else:
        print("You lose!")
