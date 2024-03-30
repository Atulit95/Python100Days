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

def compare(account_1,account_2):
    if account_1['follower_count']>account_2['follower_count']:
        return 'A'
    else:
        return 'B'

    
def game():
    print(art_module.higher_or_lower())
    next_guess=True
    count=0
    account_a=random.choice(data)
    while next_guess==True:
        account_b=random.choice(data)
        if account_a==account_b:
            account_b=random.choice(data)
        # print(f'{account_a['follower_count']}  {account_b['follower_count']}')      //To check the program or to cheat
        print(f'Compare A: {account_a['name']}, a {account_a['description']}, {account_a['country']}')
        print(art_module.vs())
        print(f'Against B: {account_b['name']}, a {account_b['description']}, {account_b['country']}')
        user_choice=input("Who has more followers? Type 'A' or 'B': ").upper()
        print(end="\033c")
        if compare(account_a,account_b)==user_choice:
            count+=1
            print(art_module.higher_or_lower())
            print(f"You're right! Current Score: {count}")
            account_a=account_b
        else:
            print(f"Sorry, that's wrong. Final Score: {count}")
            next_guess=False
            replay()
        
print(end="\033c")
game()