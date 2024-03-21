#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

#........................Solution.........................
import random
import art_module

def replay():
    """Ask whether player want to play again or not."""
    if input("Do you wish to play again. Type 'y' for yes and 'n' for no: ")=='y':
        print(end="\033c")
        guess_the_number_game()
    else:
        exit()

def play(attempts,real_number):
    while attempts!=0:
            print(f"You have {attempts} attempts remaining to guess the number.")
            guess=int(input("Make a guess: "))
            if guess==real_number:
                print(f"You got it!👏 The answer was {real_number}.")
                replay()
            elif guess<real_number:
                print("Too Low.😞\nWrong Guess.")
                attempts-=1
                continue
            elif guess>real_number:
                print("Too High.😞\nWrong Guess.")
                attempts-=1
                continue
    print(f"\nYou Lost the game.😞The number was {real_number}")
    replay()


def guess_the_number_game():
    print(art_module.guess_the_number_art())
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    actual_number=random.randrange(1,100)
    # print(actual_number)  # use this to test the code.
    difficulty=input("Choose a difficulty. Type 'easy' or 'hard' or 'extreme': ")
    if difficulty=="easy":
        number_of_attempts=10
        play(number_of_attempts,actual_number)
    elif difficulty=="hard":
        number_of_attempts=5
        play(number_of_attempts,actual_number)
    elif difficulty=="extreme":
        number_of_attempts=3
        play(number_of_attempts,actual_number)
    else:
        print("Invalid Choice")
        replay()

guess_the_number_game()