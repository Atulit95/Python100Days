############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size. 
## There are no jokers. 
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game: 
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here: 
#   https://appbrewery.github.io/python-day11-demo/

#Hint 2: Read this breakdown of program requirements: 
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created: 
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input 
#and returns the score. 
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
import random

def calculate_sum_of_cards(card_list):
    """returns sum of card drawn"""
    sum_of_card=0
    for card in card_list:
        sum_of_card+=card
    return sum_of_card

def check_blackjack(user_card_list,comp_card_list):
    if (10  in user_card_list and 11 in user_card_list):
        return "Player"
    if (10 in comp_card_list and 11 in comp_card_list):
        return "Computer"

def check_win(u_total,c_total):
    if u_total>21:
        return "Oops! Computer Won 😞"
    elif c_total>21:
        return "You Won 😎"
    elif u_total>c_total:
        return "You won 😎"
    elif c_total>u_total:
        return "Oops! Computer Won 😞"
    else:
        return "Draw 🤝"
    
def draw(card_list,u_card):
    u_total=calculate_sum_of_cards(u_card)
    drawn_card=random.choice(card_list)
    u_card.append(drawn_card)
    
    if drawn_card==11 and drawn_card+u_total>21:
        return [u_total+1,u_card]
    else:
        u_total+=drawn_card
        return [u_total,u_card]


def blackjack():
    user_cards=[]
    computer_cards=[]
    list_of_cards=[11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
    initial_hand=0
    if input("Do you want to play blackjack game 'y' or 'n': ")=="y":
        print(end="\033c")
        while initial_hand!=2:
            user_cards.append(random.choice(list_of_cards))
            computer_cards.append(random.choice(list_of_cards))
            initial_hand+=1
        user_total=calculate_sum_of_cards(user_cards)
        comp_total=calculate_sum_of_cards(computer_cards)

        print(f"Your cards:{user_cards}, current score: {user_total}")
        print(f"Computer's first card: {computer_cards[0]}")

        if check_blackjack(user_cards,computer_cards)=="Player":
            print(end="\033c")
            print(f"Your final hand: {user_cards}, final score: {0}")
            print(f"Computer's final hand: {computer_cards}, final score: {comp_total}")
            print("You Won with a Blackjack 😎")
            blackjack()
        elif check_blackjack(user_cards,computer_cards)=="Computer":
            print(end="\033c")
            print(f"Your final hand: {user_cards}, final score: {user_total}")
            print(f"Computer's final hand: {computer_cards}, final score: {0}")
            print("Oops! Computer Won with a Blackjack 😞")
            blackjack()
        while user_total< 22:
            if input("Type 'y' to get another card, type 'n' to pass: ")=="y":
                user_draw_result=draw(list_of_cards,user_cards)
                user_total=user_draw_result[0]
                user_cards=user_draw_result[1]
                print(f"Now your cards: {user_cards}, current score: {user_total}")
            else:
                while comp_total<17:
                    comp_draw_result=draw(list_of_cards,computer_cards)
                    computer_cards=comp_draw_result[1]
                    comp_total=comp_draw_result[0]
                break
        
        print(f"{check_win(user_total,comp_total)}\n Computer cards were: {computer_cards}")
        blackjack()
blackjack()