#Number Guessing Game Objectives:

# Include an ASCII art logo.
# Allow the player to submit a guess for a number between 1 and 100.
# Check user's guess against actual answer. Print "Too high." or "Too low." depending on the user's answer. 
# If they got the answer correct, show the actual answer to the player.
# Track the number of turns remaining.
# If they run out of turns, provide feedback to the player. 
# Include two different difficulty levels (e.g., 10 guesses in easy mode, only 5 guesses in hard mode).

# Imports system function "clear" ("cls" on Windows) and clears the screen
import os
def clear():
  os.system('cls||clear')

clear()

# Display logo
from art import artwork
print(artwork)

# Generate the target number
import random
target_number = random.randint(1, 100)

# Welcome Message
print("Welcome to the Number Guessing Game!\nI'm thinking of a number between 1 and 100.")

# Print target number for debug purposes
print(f"Psst, the correct answer is {target_number}.")

# Choosing difficulty
tries = 0
i = 1
while i > 0:
  i = 0
  difficulty = input("Choose difficulty: 'Easy' or 'Hard'\n--> ").lower()
  if difficulty == "easy":
    tries = 10
    print(f"So, you choose 'Easy' huh? You get {tries} tries.")
  elif difficulty == "hard":
    tries = 5
    print(f"As if life isn't 'Hard' enough? You get {tries} tries.")
  else:
    print("That is not a valid difficulty.")
    i = 1

# Starting Game
while tries > 0:
  guess = int(input(f"Your guess:\n--> "))
  tries -= 1
  if guess > target_number:
    print(f"Too high, you have {tries} tries left.")
  elif guess < target_number:
    print(f"Too low, you have {tries} tries left.")
  else:
    print(f"Your answer {guess} was correct! Congratulations!")
if tries == 0:
  print("Sorry, you did not make it. Better luck next time!")