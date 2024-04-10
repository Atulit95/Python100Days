import pandas

students_dict = {
    "name": ["Alex", "Beth", "Caroline", "Dave", "Freddie"],
    "score": [90, 56, 35, 24, 67],
}

student_dataframe = pandas.DataFrame(students_dict)
# print(student_dataframe)

# iteration over Dataframe
for key, value in student_dataframe.items():
    print(value)
