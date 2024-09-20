import random
from hangman_art import logo, stages
import hangman_words
end_of_game = False
lives = 6
word_list = ["aardvark", "baboon", "camel"]
 
choosen_word = random.choice(hangman_words.word_list)
word_lenght = len(choosen_word)
print(logo)
# Testing Code
print(f"computer chose {choosen_word}")

 
display = []
for _ in range(word_lenght):
  display += "_"
print(display)

while not end_of_game:
  guess = input("Guess a letter: ").lower()
  if guess in display:
    print(f"You have already guessed {guess}")
  for position in range(word_lenght):
    letter = choosen_word[position]
    if letter == guess:
      display[position] = letter
    print(display)
      
  if "_" not in display:
    end_of_game = True
    print("You Won!")

  if guess not in choosen_word:
    lives -= 1
    print(f"you have left with {lives} lives") 
    if lives == 0:
      end_of_game = True
      print("You Lose!")

  
  print(hangman_art.stages[lives])

