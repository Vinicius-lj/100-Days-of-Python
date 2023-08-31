from art import logo
from random import randint

print(logo)
print("Welcome to the Number Guessing game!")
print("I'm thinking in a number between 1 and 100.")
difficulty = input("Choose a difficulty. Type 'easy' or 'hard': ")
if difficulty == "easy":
  attempts = 10
else: 
  attempts = 5
pc_number = randint(1, 100)
continue_guessing = True
while continue_guessing:
  print(f"You have {attempts} attempts remaining to guess the number")
  guess = int(input("Make a guess: "))
  if guess > pc_number:
    print("Too high.\nGuess Again.")
    attempts -= 1
  elif guess < pc_number:
    print("Too low.\nGuess again.")
    attempts -= 1
  else:
    print(f"You got it. The guess was {pc_number}")
    continue_guessing = False
  if attempts == 0:
    print("You've run out of guessing, you lose.")
    continue_guessing = False