from replit import clear
from art import logo

continue_bidding = True
blind_auction= {}
print(logo)
while continue_bidding== True:
  name = input('What is your name?: ')
  bid = int(input('What is your bid?: $'))

  #add name and their bid to the dictionary:
  blind_auction[name]= bid
  
  #if they say yes we continue otherwise we exit:
  answer = input("Are there any other bidders? Type 'yes' or 'no'\n").lower()
  if answer=='yes':
    continue_bidding = True
    clear() #clear the screen
  else:
    continue_bidding= False
    #print("the winner is: ")

#figuring out the highest bid, and the winner. 
winning_bid= 0
winner= ""
for name in blind_auction:
  if blind_auction[name] > winning_bid:
    winning_bid = blind_auction[name]
    winner = name 
print(f"The winner is {winner} with a bid of ${winning_bid}")
