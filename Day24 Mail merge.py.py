# All the files mentioned are either in input or output folder
# TODO: Create a letter using starting_letter.txt
# for each name in invited_names.txt
# Replace the [name] placeholder with the actual name.
# Save the letters in the folder "ReadyToSend".

# Hint1: This method will help you: https://www.w3schools.com/python/ref_file_readlines.asp
# Hint2: This method will also help you: https://www.w3schools.com/python/ref_string_replace.asp
# Hint3: THis method will help you: https://www.w3schools.com/python/ref_string_strip.asp

with open("Input/Names/invited_names.txt") as names:
    name_list = names.readlines()

with open("Input/Letters/starting_letter.txt") as letter:
    content = letter.read()
# print(name_list)
# print(content)

for person in name_list:
    person = person.strip("\n")
    with open(f"Output/ReadyToSend/letter_for_{person}.txt",mode="w") as result:
        result.write(f"{content.replace("[name]", f"{person}")}")
