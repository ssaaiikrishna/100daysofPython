from replit import clear
from art import logo
print(logo)
print("Wecome to secret auction program")
bids = {}
bidding_finish = False

def find_highest_bid(bids):
  max = 0
  winner=''
  for name in bids:
    bid = bids[name]
  if bid > max:
    max = bid
    winner = name
  print(f"The winner of the auction is {winner}!, with the heighest bid of ${max}")

while not bidding_finish :
  name = input('what is your name? : ')
  bid = int(input('what is your bid amount? : '))
  bids[name]=bid
  should_continue = input('Are there any more bidders? yes or no. \n')
  if should_continue == 'no':
    bidding_finished = True
    find_highest_bid(bids)
  elif should_continue == 'yes':
    clear()



    