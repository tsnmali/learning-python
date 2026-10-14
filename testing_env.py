while True: # This creates an infinite loop. The loop will continue running UNTIL break is reached.
    try:
        number_grade = float(input("Enter your grade (0-100): ")) #tries to store the user's grade as an input that is converted into a float.

        if 0 <= number_grade <= 100: # If the grade is between 0 and 100, exit the loop.
            break

        print("Your grade must be between 0 and 100.") # Runs when the input is a number but is outside the valid range.  After printing, the loop starts over and asks for input again.

    except ValueError: # Handles input that cannot be converted to a float. Prints an error message and the loop repeats UNTIL it reaches a break. Beak only happens if the input is fully valid.
        print("Your grade must be a number.")


def letter_grades(number_grade): # Determines and returns the letter grade for a numeric grade.
    if 90 <= number_grade <= 100: #Checks if the user's input exists in this letter's numeric range.
        return "A" # if valid, returns "A" and IMMEDIATELY exits the function.
    elif 80 <= number_grade <= 90: #Checks if the user's input exists in this letter's numeric range.
        return "B" #if valid, returns "B" and IMMEDIATELY exits the function.
    elif 70 <= number_grade <= 80: #Checks if the user's input exists in this letter's numeric range.
        return "C" # if valid, returns "C" and IMMEDIATELY exits the function.
    elif 60 <= number_grade <= 70: #Checks if the user's input exists in this letter's numeric range.
        return "D" # if valid, returns "D" and IMMEDIATELY exits the function.
    else:
        return "F" #Returns this letter if the user's number is less than 59.


result = letter_grades(number_grade) # Calls the function and stores the returned letter grade.
print(f"Your letter grade is: {result}") #Prints the user's letter grade.
