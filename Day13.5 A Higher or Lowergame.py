import random
from Higher_or_lower_game_data import data
import art_module

def replay():
    """Ask whether player want to play again or not."""
    if input("Do you wish to play again. Type 'y' for yes and 'n' for no: ")=='y':
        print(end="\033c")
        game()
    else:
        print(end="\033c")
        exit()

def compare(celeb_list):
    if celeb_list[0]['follower_count']>celeb_list[1]['follower_count']:
        return 'A'
    else:
        return 'B'
    
def game():
    next_guess=True
    count=0
    while next_guess==True:
        two_celebs=random.sample(data,2)
        print(art_module.higher_or_lower())
        # print(f'{two_celebs[0]['follower_count']}  {two_celebs[1]['follower_count']}')      //To check the program or to cheat
        print(f'Compare A: {two_celebs[0]['name']}, {two_celebs[0]['description']}, {two_celebs[0]['country']}')
        print(art_module.vs())
        print(f'Against B: {two_celebs[1]['name']}, {two_celebs[1]['description']}, {two_celebs[1]['country']}')
        user_choice=input("Who has more followers? Type 'A' or 'B': ").upper()
        print(end="\033c")
        if compare(two_celebs)==user_choice:
            count+=1
            print(f"You're right! Current Score: {count}")
        else:
            print(f"Sorry, that's wrong. Final Score: {count}")
            next_guess=False
            replay()
        
print(end="\033c")
game()