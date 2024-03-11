#Step 1: Our task is to pick a Random Words and Check Answers
import random
word_list = ["ardvark", "baboon", "camel"]

#TODO-1 - Randomly choose a word from the word_list and assign it to a variable called chosen_word.
random_word=random.choice(word_list)

#TODO-2 - Ask the user to guess a letter and assign their answer to a variable called guess. Make guess lowercase.
user_choice=input("Guess a letter\n").lower()

#TODO-3 - Check if the letter the user guessed (guess) is one of the letters in the chosen_word.
for letter in random_word:
    if letter == user_choice:
        print("Right")
    else:
        print("Wrong")
        