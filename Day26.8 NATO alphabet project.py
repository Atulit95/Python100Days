# Our goal is to create a program where it tells us nato phonetics
# for our spelled word in format of a list
# Data required is present in nato_phonetic_alphabet.csv file


import pandas

data = pandas.read_csv("nato_phonetic_alphabet.csv")
data_dic = data.to_dict()

user_input = input("Enter Your word: ").upper()

phonetics = {row.letter: row.code for index, row in data.iterrows()}

Nato_words = [phonetics[new_item] for new_item in user_input]

print(Nato_words)
