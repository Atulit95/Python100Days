# let say we have have to increase every no of list by 1

# ..............using Loops...................
numbers = [1, 2, 3]
new_list = []
for n1 in numbers:
    add_1 = n1 + 1
    new_list.append(add_1)

# print(new_list)


# ..............Using List Comprehension..............

new_list2 = [n2 + 1 for n2 in numbers]
# print(new_list2)

# ...........List Comp. for strings..............

name = "Sammer"
letter_list = [letter for letter in name]
# print(letter_list)

# .........use of range() in list Compre............

range_list = [double * 2 for double in range(1, 5)]
# print(range_list)

# ..........Conditional List Comprehension............
name = ["Alex", "Beth", "Caroline", "Dave", "Freddie"]

short_names = [names.upper() for names in name if len(names) > 5]
print(short_names)
