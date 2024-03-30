############DEBUGGING#####################

# ..Q1..Describe Problem
# Goal is to debug and display "You got it"
# def my_function():
#   for i in range(1, 20):
#     if i == 20:
#       print("You got it")
# my_function()

# ..Ans1..
# The error is in line 5 and 6. As print will run iff i=20 but the loop assign "i" value 1-19.
# As range(a,b) function outputs value in range a(inclusive) and b(exclusive)

# ...Solution..
# def my_function():
#   for i in range(1, 21):
#     if i == 20:
#       print("You got it")
# my_function()

# # ..Q2..Reproduce the Bug
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(1, 6)
# print(dice_imgs[dice_num])

# ...Ans2....
# Here randint(a,b) can return any number between a(inclusive) and b(inclusive).
# As list indexing always start from 0 and here it goes from 0-5 for dice_imgs list.
# So it generates error id dice_num gets value 6

# ...Solution.....
# from random import randint
# dice_imgs = ["❶", "❷", "❸", "❹", "❺", "❻"]
# dice_num = randint(0, 5)
# print(dice_imgs[dice_num])

# # ..Q3...Play Computer
# year = int(input("What's your year of birth?"))
# if year > 1980 and year < 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# ...Ans3....
# Here the bug is when u input year=1994 beacuse it has no condition to evaluate

# ...Solution.....
# year = int(input("What's your year of birth?"))
# if year > 1980 and year =< 1994:
#   print("You are a millenial.")
# elif year > 1994:
#   print("You are a Gen Z.")

# # ....Q4..Fix the Errors
# age = input("How old are you?")
# if age > 18:
# print("You can drive at age {age}.")

# ...Ans4.....
# Here print should be f-string like: print(f"You can drive at age {age}.")and it should be indented.
#The age must be int type for if to campare

# ....Solution.....
# age = int(input("How old are you?"))
# if age > 18:
#   print("You can drive at age {age}.")


# #..Q5..Print is Your Friend
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page == int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)

# ...Ans5...
# Here is two equals used in word_per_page

# ....Solution....
# pages = 0
# word_per_page = 0
# pages = int(input("Number of pages: "))
# word_per_page = int(input("Number of words per page: "))
# total_words = pages * word_per_page
# print(total_words)


# #...Q6..Use a Debugger
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#   b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])

# ...Ans6.....
# IndentationError in line "b_list.append(new_item)"

# ....Solution....
# def mutate(a_list):
#   b_list = []
#   for item in a_list:
#     new_item = item * 2
#     b_list.append(new_item)
#   print(b_list)

# mutate([1,2,3,5,8,13])