#TODO: Create a letter using starting_letter.txt 
#for each name in invited_names.txt
#Replace the [name] placeholder with the actual name.
#Save the letters in the folder "ReadyToSend".

#Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# file.readlines() > Returns the returns all the lines in the file as a list
#Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# txt.replace(a, b) replaces a with b
#Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp
# txt.strip() removes all leading and trailing white spaces


# Opens the invited names document and saves them in a list
with open("./Input/Names/invited_names.txt") as file:
    names_list = file.readlines()
    print(names_list)

# Opens the starting letter and saves it to a string variable
with open("./Input/Letters/starting_letter.txt") as file:
    txt = file.read()  # Returns the contents as a string
    # print(txt)

# Replaces [name] with a name from the list, stripping it from new lines
for name in names_list:
    new_txt = txt.replace("[name]", name.strip())  # Replaces instances of 'a' in a string with a new string 'b'
    # Creates a new file with the persons name
    with open(f"./Output/ReadyToSend/letter_for_{name}.txt", mode='w') as file:
        file.write(f"{new_txt}")
