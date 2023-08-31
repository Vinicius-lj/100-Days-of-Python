from art import logo
from random import choice
from replit import clear

def black_jack():
  print(logo)
  should_continue = True
  cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
  player_cards = [choice(cards)]
  pc_cards = [choice(cards), choice(cards)]
  pc_score = sum(pc_cards)
  
  while should_continue:
    player_cards.append(choice(cards))
    player_score = sum(player_cards)
    if player_score > 21 and 11 in player_cards:
      player_cards.remove(11)
      player_cards.append(1)
      player_score = sum(player_cards)
    print(f"Your cards: {player_cards}, current score: {player_score}")
    print(f"Computer's first card: {pc_cards[0]}")
    if player_score < 21:
      key_continue = input("Type 'y' to get another card, type 'n' to pass: ")
      if key_continue != "y":
        should_continue = False
    else:
      should_continue = False
      
  while pc_score < 17:
    pc_cards.append(choice(cards))
    pc_score = sum(pc_cards)
    
  print(f"Your final hand: {player_cards}, final score: {player_score}")
  print(f"Computer's final hand: {pc_cards}, final score: {pc_score}")  
  
  if player_score > 21:
    print("You went over. You lose.")
  elif pc_score > 21:
    print("Pc went over. You won!")
  elif pc_score == player_score:
    print("Draw")
  elif player_score > pc_score:
    print("You won!")
  else:
    print("Computer wins")
    
  play = input("Do you want to play another game of Blackjack? Type 'y' or 'n':")
  if play == "y":
    clear()
    black_jack()

black_jack()