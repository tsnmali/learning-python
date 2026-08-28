this_is_a_list = ['a', 1, '5']
this_is_a_dictionary = { "Letter_A": 'a'}

print(this_is_a_list[0])
print(this_is_a_dictionary["Letter_A"])
print(this_is_a_dictionary.keys())
print(this_is_a_dictionary.values())

first_letter_in_the_alphabet = this_is_a_dictionary["Letter_A"]
print(first_letter_in_the_alphabet)

second_letter_in_the_alphabet = this_is_a_dictionary["Letter_B"] = 'b' #This is how you update a dictionary.
print(second_letter_in_the_alphabet)

a_dict_with_a_list = {"Example": [1,2,3,"4","5","6"]} #This shows you can have lists inside dictionaries+

print("======================================")
user_sentence = input("Type in a sentence to check how long it is. Remember, spaces count as characters: ")
print(f"Your sentence is {len(user_sentence)} characters long")
print("======================================")



