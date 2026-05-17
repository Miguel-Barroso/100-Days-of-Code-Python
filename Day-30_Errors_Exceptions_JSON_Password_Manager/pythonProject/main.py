# # FileNotFoundError
# with open("a_file.txt") as file:
#     file.read()

# # KeyError
# a_dictionary = {"key": "value"}
# value = a_dictionary["non-existent"]

# # IndexError
# fruit_list = ["Apple", "Banana", "Pear"]
# fruit = fruit_list[3]

# # TypeError
# text = "abc"
# print(text + 5)

# try:  # Will try a block of code that may throw an exception
# except:  # Will execute another block of code if there was an exception in the try block
# else:  # Will execute a block of code if there were no exceptions in the try block
# finally:  # Will always execute a given block of code regardless of outcome

# FileNotFoundError part 2
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["non-existent"])
# except:  # Using except will move on from any error in the try block to the except block without obvious reasons why
#     print("There was an error opening the file.")  # By using except FileNotFound error, you can specify the error!
#     file = open("a_file.txt", "w")
#     file.write("Something")

# # FileNotFoundError part 3
# try:
#     file = open("a_file.txt")
#     a_dictionary = {"key": "value"}
#     print(a_dictionary["non-existent"])
# except FileNotFoundError:
#     print("There was an error opening the file.")  # By using except FileNotFoundError, you can specify the error!
#     file = open("a_file.txt", "w")
#     file.write("Something")
# except KeyError as error_message:  # By using as, you can access the normal error message
#     print(f"The {error_message} key does not exist!")
# else:
#     content = file.read()  # This block of code will only get triggered if there were no errors
#     print(content)
# finally:
#     file.close()  # This will always occur no matter what which is good for cleanup
#     print("File was closed.")

# How to raise your own errors
height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height should not be over 3 meters.")  # Can add error message directly here

bmi = weight / height ** 2
print(bmi)