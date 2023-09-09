import random
from hangman_art import stages, logo
from hangman_words import word_list

print(logo)
chosen_word = random.choice(word_list)
chosen_word = list(chosen_word)
word_list = []
lives = 6
for x in chosen_word:
  word_list += "_"
print(stages[lives])
print("".join(word_list))

while lives > 0 and word_list != chosen_word:
  chosen_letter = input("Guess a letter: ").lower()
  if chosen_letter in word_list:
    print(f"You alredy guessed {chosen_letter}. Please try a diferent letter")
  else:
    count = 0
    position = 0
    for letter in chosen_word:         
      if chosen_letter == letter:
        word_list[position] = chosen_letter    
      else:
        count += 1
      position += 1
    if count == len(chosen_word):
      lives -= 1
      print(f"You guessed {chosen_letter}, that is not in the word. You lose a life")
    print(stages[lives])
    print("".join(word_list))
  
if lives > 0:
  print("You Won!!")
else:
  print("Game Over")  