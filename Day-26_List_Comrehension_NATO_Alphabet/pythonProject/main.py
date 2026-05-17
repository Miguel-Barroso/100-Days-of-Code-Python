import pandas

student_dict = {
    "student": ["Angela", "James", "Lily"],
    "score": [56, 76, 98]
}

# for (key, value) in student_dict.items():
#     print(key)
#     print(value)

student_data_frame = pandas.DataFrame(student_dict)
print(student_data_frame)

# Loop through a DataFrame, basically the same as with a dictionary (see the above) however not very useful
# for (key, value) in student_data_frame.items():
    # print(key)
    # print(value)

# Loop through rows of a DataFrame
for (index, row) in student_data_frame.iterrows():
    # print(index)
    # print(row)
    # print(row.student)
    # print(row.score)
    if row.student == "Angela":
        print(row.score)
