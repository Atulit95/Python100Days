#Step 5 This is final code to make this Hangman Game user friendly

import random
import hangman_art
import hangman_word

#TODO-1: - Update the word list to use the 'word_list' from hangman_words.py
#Delete this line: word_list = ["ardvark", "baboon", "camel"]
chosen_word = random.choice(hangman_word.words())
word_length = len(chosen_word)
lives = 6
stage=hangman_art.stages()


#TODO-3: - Import the logo from hangman_art.py and print it at the start of the game.
print(hangman_art.logo())
#Testing code
print(f'Pssst, the solution is {chosen_word}.')

#Create blanks
display = []
for _ in range(word_length):
    display += "_"

while "_" in display:
    guess = input("Guess a letter: ").lower()
# This print(end="\033c") is used to clear screen of previous life lost(to make code user friendly) 
    print(end="\033c") 

    #TODO-4: - If the user has entered a letter they've already guessed, print the letter and let them know.
    if guess in display:
        print("You choose the word again")
    #Check guessed letter
    for position in range(word_length):
        letter = chosen_word[position]
        # print(f"Current position: {position}\n Current letter: {letter}\n Guessed letter: {guess}")
        if letter == guess:
            display[position] = letter

    #Check if user is wrong.
    if guess not in chosen_word:
         #TODO-5: - If the letter is not in the chosen_word, print out the letter and let them know it's not in the word.
        print(f"Your guess {guess} not in word")
        lives-=1
        if lives==0:
            break
        print(stage[lives])
    #Join all the elements in the list and turn it into a String.
    print(f"{' '.join(display)}")

    #Check if user has got all letters.
if(''.join(display)==chosen_word):
    print("You won the game")
else:
    #TODO-2: - Import the stages from hangman_art.py and make this error go away.
    print(stage[lives])
    print("You Loose")