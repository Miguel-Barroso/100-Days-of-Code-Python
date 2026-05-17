student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

#Looping through dictionaries:
for (key, value) in student_dict.items():
    #Access key and value
    pass

import pandas

student_data_frame = pandas.DataFrame(student_dict)

#Loop through rows of a data frame
for (index, row) in student_data_frame.iterrows():
    #Access index and row
    #Access row.student or row.score
    pass

# Keyword Method with iterrows()
# {new_key:new_value for (index, row) in df.iterrows()}

nato_alphabet_data = pandas.read_csv("nato_phonetic_alphabet.csv")
# print(nato_alphabet_data)

#TODO 1. Create a dictionary in this format:
{"A": "Alfa", "B": "Bravo"}

nato_dict = {row.letter: row.code for (index, row) in nato_alphabet_data.iterrows()}
# print(nato_dict)


#TODO 2. Create a list of the phonetic code words from a word that the user inputs.

# name = "Angela"
# name = name.upper()
word = input("Input a word to convert to NATO format: ").upper()
nato_format = [nato_dict[letter] for letter in word]

# Essentially what we want to achieve:
# for letter in name:
# if letter in nato_dict:
# print(nato_dict[letter])

print(nato_format)
