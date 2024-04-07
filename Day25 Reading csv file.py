# Add tempratuire present in weather_data.csv in integer format into a new list using csv module
#  with open("weather_data.csv") as file1:
#     data = file1.readlines()

# print(data)

#                  Or
import csv

with open("weather_data.csv") as file1:
    data = csv.reader(file1)
    temprature = []
    for row in data:
        if row[1] != "temp":
            temprature.append(int(row[1]))
print(temprature)

import pandas  # Use this library for complex Analysis
