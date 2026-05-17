# # with open("weather_data.csv") as data_file:
# #     data = data_file.readlines()
# #     print(data)
# #     new_list = []
# #     for each in data:
# #         new_list.append(each.strip())
# #     print(new_list)
#
# # import csv
# #
# # with (open("weather_data.csv") as data_file):
# #     data = csv.reader(data_file)
# #     temperatures = []
# #     for row in data:
# #         if row[1] != "temp":
# #             temperatures.append(int(row[1]))
# #     print(temperatures)
#
# import pandas
#
# data = pandas.read_csv("weather_data.csv")
# # print(data)
# # print(data["temp"])
#
# # data_dict = data.to_dict()
# # print(data_dict)
# #
# # total = 0
# #
# # temperature_list = data["temp"].to_list()
# # print(temperature_list)
# # for temp in temperature_list:
# #     total += temp
# # mean = total/len(temperature_list)
# # print(mean)
# #
# # print(data["temp"].mean())
# # print(data["temp"].max())
#
# # print(data["condition"])  # Grabs the header with the specified name
# # print(data.condition)  # Pandas reads the headers and converts them to attributes of the DataFrame object
# # In both cases, the header name is case-sensitive!
#
# # Get a row using data frames
# # print(data[data.day == "Monday"])
# # Gets the entire data frame, looks for the header called day, and finds the row with the value of "Monday"
#
# # Gets the row where the temperature was the highest
# # print(data[data.temp == data.temp.max()])
#
# # monday = data[data.day == "Monday"]
# # print(monday)
# # monday_temp = monday.temp[0]
# # print(monday_temp)
# # farhenheit = (monday_temp * 9/5) + 32
# # print(farhenheit)
#
#
import pandas
# # Create a DataFrame from scratch
data_dict = {
    "students": ["Amy", "James", "Angela"],
    "scores": [76, 56, 65]
}

new_data = pandas.DataFrame(data_dict)
print(new_data)
new_data.to_csv("new_data.csv")



data = pandas.read_csv("../2018_Central_Park_Squirrel_Census_-_Squirrel_Data_20240728.csv")

# print(data["Primary Fur Color"].describe())

# Hard way of getting the fur color counts
squirrel_colors = data["Primary Fur Color"].to_list()
gray_count = 0
cinnamon_count = 0
black_count = 0
for color in squirrel_colors:
    if color == "Gray":
        gray_count += 1
    elif color == "Cinnamon":
        cinnamon_count += 1
    elif color == "Black":
        black_count += 1
print((gray_count, cinnamon_count, black_count,))

squirrel_colors_dict = {
    "Fur Color": ["grey", "red", "black"],
    "Count": [gray_count, cinnamon_count, black_count],
}

print(squirrel_colors_dict)

squirrel_colors_dataframe = pandas.DataFrame(squirrel_colors_dict)
squirrel_colors_dataframe.to_csv("squirrel_count_2.csv")

# # Easy way to get the fur color counts
# fur_color_counts = data["Primary Fur Color"].value_counts()
# print(fur_color_counts)
# fur_color_counts.to_csv('squirrel_count.csv')

# Angelas way of accessing the fur color counts
grey_squirrels_count = len(data[data["Primary Fur Color"] == "Gray"])
print(grey_squirrels_count)
red_squirrels_count = len(data[data["Primary Fur Color"] == "Cinnamon"])
print(red_squirrels_count)
black_squirrels_count = len(data[data["Primary Fur Color"] == "Black"])
print(red_squirrels_count)
