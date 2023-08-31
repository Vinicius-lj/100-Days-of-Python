from os import system
from art import logo

print(logo)

print("Welcome to the secret auction program.")
bid_dic = {}
new_guess = "yes"
while new_guess == "yes":
  name = input("What`s your name?: ")
  bid = int(input("What`s your bid?: $"))
  bid_dic[name] = bid
  new_guess = input("Are there any other bidders? Type 'yes' or 'no': ").lower()
  print(new_guess)
  system("cls")
  
winner = {"name":"", "bid":0}
for name in bid_dic:
  if bid_dic[name] > winner["bid"]:
    winner["name"] = name
    winner["bid"] = bid_dic[name]

print(f"The winner is {winner['name']} with a bid of ${winner['bid']}.")
  