#  name.upper() = All uppercase
#  name.lower() = All lowercase
# name.title () = Title case
#  len() = Total characters including spaces
#  .strip() (all versions) = removes spaces
# text.count() = Counts how many times that specific substring is present
# .split() = Creates a list out of the string with each character-separated (you choose what) content being added to the list individually
# .startswith() (.endswith()) = Find whether or not a string begins or ends with specific substring
# Use the above to get initials.
# Use the above to check if the sentence starts with certain words or contains numbers.

user_statement = input("Please enter a sentence of your choice: ")

def user_sentence():
    upper_user_statement = user_statement.upper()
    lower_user_statement = user_statement.lower()
    title_user_statement = user_statement.title()
    length_lower_user_statement_no_spaces = len(user_statement.replace(" ",""))
    length_user_statement_with_spaces = len(user_statement)
    return upper_user_statement, lower_user_statement, title_user_statement, length_lower_user_statement_no_spaces, length_user_statement_with_spaces

results = user_sentence()
print(f"Here is your sentence in Python's upper, lower, and title cases. Along with the length with/without spaces: {results[0], results[1], results[2], results[3], results[4]}") #Remember, when you have functions that return more than one value, the result is stored as a tuple. You can use "*" to unpack the tuple instead of doing it manually.I

def user_sentence_word_count():
    word_count = user_statement.split(" ")
    return word_count

word_count_user_statement = user_sentence_word_count()
print(f"The length of your sentence is: {len(word_count_user_statement)} words.")


def get_users_name_initials():
    while True:
        users_name = input("Please enter your name: ")
        split_users_name = users_name.split(" ")

        if len(split_users_name) > 2:
            print("Please enter in your first and last name only: ")
            continue
        else:
            users_initials = split_users_name[0][0].upper(), split_users_name[1][0].upper()
            return users_initials

complete_results = get_users_name_initials()
print(f"Your initials are: {complete_results[0]}.{complete_results[1]}")








