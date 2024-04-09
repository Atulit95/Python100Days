# ..............Instructions.................

# 💪 This exercise is HARD 💪
# Take a look inside "Data Overlap file1.txt" and "Data Overlap file2.txt"
#  They each contain a bunch of numbers, each number on a new line.

# You are going to create a list called result which contains the numbers that are common in both files.

# e.g. if file1.txt contained:

# 1
# 2
# 3
# and file2.txt contained:

# 2
# 3
# 4
# result = [2, 3]
# IMPORTANT: The output should be a list of integers and not strings! Try to use List Comprehension instead of a Loop.

# Expected Output
# [3, 6, 5, 33, 12, 7, 42, 13]

# .......................Solution......................
with open("Data Overlap file1.txt") as file1:
    list1 = file1.readlines()

with open("Data Overlap file2.txt") as file2:
    list2 = file2.readlines()

result = [int(common_num) for common_num in list1 if common_num in list2]
# Write your code above 👆
print(result)
