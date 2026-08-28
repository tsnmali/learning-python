
name = input("Enter your first and last name: ")

while len(name.split()) < 2:
    name = input("Please enter your first and last name: ")

while len(name.split()) > 2:
    name = input("Please enter your first and last name only. Try again: ")



def user_name_analysis(name):
        cleaned = name.strip()
        upper_case_version = cleaned.upper()
        lower_case_version = cleaned.lower()
        title_version = cleaned.title()
        length_version = len(cleaned)
        character_count_exclude_spaces = len(cleaned.replace(" ", ""))
        word_count_exclude_spaces = len(cleaned.split(" "))
        initials = cleaned.split(" ")[0][0].upper() + "." + cleaned.split(" ")[1][0].upper()


        return {
            "WhitespaceRemoval": cleaned,
            "UpperCase": upper_case_version,
            "LowerCase": lower_case_version,
            "TitleVersion": title_version,
            "CharacterLength": length_version,
            "CharacterLengthWithoutSpace": character_count_exclude_spaces,
            "TotalWordCountWithoutSpace": word_count_exclude_spaces,
            "Initials": initials

        }

result = user_name_analysis(name)


print(f"""
--- Name Analysis ---

Cleaned text: {result["WhitespaceRemoval"]}
Uppercase: {result["UpperCase"]}
Lowercase: {result["LowerCase"]}
Title case: {result["TitleVersion"]}
Total characters: {result["CharacterLength"]}
Characters excluding spaces: {result["CharacterLengthWithoutSpace"]}
Number of words: {result["TotalWordCountWithoutSpace"]}
Initials: {result["Initials"]}
""")




