# FileNotFound
# with open("a_file.txt") as file:
#     file.read()

# KeyError
# a_dic = {"key": "value"}
# value = a_dic["non_existent_key"]
# print(value)

# IndexError
# fruit = ["apple", "banana", "mango"]
# print(fruit[3])

# TypeError
# a = 2
# b = "3"
# print(a + b)


# >>>>>>>>>>>>>>>>>> Exception Handling <<<<<<<<<<<<<<<<<<
# Displays use of try, except(under some error), else
# try:
#     file = open("a_file.txt")
#     a_dic = {"key": "value"}
#     print(a_dic["as"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
#     print("There was a an FileNotFound Error")
# except KeyError as error_mesasge:
#     print(f"The key {error_mesasge} does not exist.")
# else:
#     content = file.read()
#     print(content)

# Displays the use of else, finally

try:
    file = open("a_file.txt")
    a_dic = {"key": "value"}
    print(a_dic["key"])
except FileNotFoundError:
    file = open("a_file.txt", "w")
    file.write("Something")
    print("There was a an FileNotFound Error")
except KeyError as error_mesasge:
    print(f"The key {error_mesasge} does not exist.")
else:
    content = file.read()
    print(content)
finally:
    file.close()
    print("File is now closed")
