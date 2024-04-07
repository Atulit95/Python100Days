# Add tempratuire present in weather_data.csv in integer format into a new list using csv module
#  with open("weather_data.csv") as file1:
#     data = file1.readlines()

# print(data)

#                  Or
# import csv

# with open("weather_data.csv") as file1:
#     data = csv.reader(file1)
#     temprature = []
#     for row in data:
#         if row[1] != "temp":
#             temprature.append(int(row[1]))
# print(temprature)

#                      Or

import pandas  # Use this library for complex data analysis

data = pandas.read_csv("weather_data.csv")
# print(data["temp"])
data_dict = data.to_dict()
# print(data_dict)

temp_list = data["temp"].to_list()
# calculation of avg temp using pandas library
avg = data["temp"].mean()
# print(avg)

# Find maximum tempratute throughout the week
max_temp = data["temp"].max()
# print(max_temp)

# how to retrive data in row
# print(data[data.day == "Monday"])

# retrive the row with max temp
# print(data[data.temp == data.temp.max()])


# Convert monday's temp to Fahrenheit
def to_fahrenheit(temp):
    return temp * (9 / 5) + 32


monday_temp = data[data.day == "Monday"].temp[0]

# print(to_fahrenheit(monday_temp))

# How to create dataframe from scratch save it as new_data.csv
data_dict_2 = {"students": ["Amy", "James", "Sameer"], "scores": [76, 56, 65]}

data_2 = pandas.DataFrame(data_dict_2)
data_2.to_csv("new_data.csv")
