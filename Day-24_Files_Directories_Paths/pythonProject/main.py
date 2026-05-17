# file = open("my_file.txt")  # Opens file using built in method
# contents = file.read()  # Returns contents as a string
# print(contents)
# file.close()  # To free up the file resource


with open("../../../../../Desktop/my_file.txt") as file:  # Alternative way of opening files which does not require
    # file.close()
    contents = file.read()  # Returns contents as a string
    print(contents)

# with open("my_file.txt", mode="w") as file:  # Alternative way of opening files which does not require file.close()
#     file.write("Ahmed")  # mode = write erases the content of the file
#     print(contents)

# For each '../' the parent folder is traversed(!) so you can get paths relative to the working directory
