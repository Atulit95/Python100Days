# try:
#     file = open("a_file.txt")
#     a_dic = {"key": "value"}
#     print(a_dic["key"])
# except FileNotFoundError:
#     file = open("a_file.txt", "w")
#     file.write("Something")
#     print("There was a an FileNotFound Error")
# except KeyError as error_mesasge:
#     print(f"The key {error_mesasge} does not exist.")
# else:
#     content = file.read()
#     print(content)
# finally:
#     file.close()
#     print("File is now closed")


# We can raise our own errors using keyword 'raise'.

height = float(input("Height: "))
weight = float(input("Weight: "))

if height > 3:
    raise ValueError("Human height shouls not be more than 3 meter")
bmi = weight / height**2
print(bmi)
