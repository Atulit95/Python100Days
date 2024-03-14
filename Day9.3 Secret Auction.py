# our Goal to make a program that do following task
# 1. Displays the auction_hammer_image using library import
# 2. It ask first bidder name and amount to bid
# 3. It ask are there any other bidders
# 4. If yes then clear the screen using "print(end="\033c")" and Repeat the task 2,3,4
# 5. At last clear the screen and print the name and amount of player who won the bet.

import auction_art
print(auction_art.auction_hammer_img())
bidder_available = "yes"
bidder_list={}

def find_highest_bidder(bidding_record):
  highest_bid = 0
  winner = ""
  # bidding_record = {"Jack": 123, "James": 321}
  for bidder in bidding_record:
    bid_amount = bidding_record[bidder]
    if bid_amount > highest_bid: 
      highest_bid = bid_amount
      winner = bidder
  print(f"The winner is {winner.capitalize()} with a bid of ${highest_bid}")

print("Welcome to the secret auction program.")
while bidder_available=="yes":
    bidder_name= input("What is your name?: ")
    bidding_amount= int(input("What's your bid: $"))
    bidder_list[bidder_name]= bidding_amount
    bidder_available= input("Are there any other bidders? Type 'yes' or 'no'.")
    print(end="\033c")
find_highest_bidder(bidder_list)
