# ..............................Instructions...........................
# You are going to use Dictionary Comprehension to create a dictionary called weather_f that takes each temperature in degrees Celsius and converts it into degrees Fahrenheit.

# To convert temp_c into temp_f use this formula:

# (temp_c * 9/5) + 32 = temp_f
# Do NOT Create a dictionary directly. Try to use Dictionary Comprehension instead of a Loop.

# The eval() function will help us convert the string input into a Python dictionary, provided that the inputs are already formatted with the correct syntax.

# Example Input
# {"Monday": 4, "Tuesday": 5, "Wednesday": 10, "Thursday": 11, "Friday": 12, "Saturday": 14, "Sunday": 16}
# Example Output
# {'Monday': 39.2, 'Tuesday': 41.0, 'Wednesday': 50.0, 'Thursday': 51.8, 'Friday': 53.6, 'Saturday': 57.2, 'Sunday': 60.8}

# .............................Solution....................................
weather_c = eval(input())
# 🚨 Don't change code above 👆


# Write your code 👇 below:

weather_f = {day: (temp_c * 9 / 5) + 32 for (day, temp_c) in weather_c.items()}

print(weather_f)
