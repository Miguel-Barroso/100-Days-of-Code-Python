### Import Data
## Import game data
from game_data import data
## Import artworks
from art import logo, vs
## Import random module
from random import randint
## Import clear module
import os
def clear():
    # Clear command for Windows
    if os.name == 'nt':
        os.system('cls')
    # Clear command for Unix-based systems
    else:
        os.system('clear')
    # Print newlines to push content out of view
    print("\n" * 100)

clear()

### Variables
random_index = 0 # A random index (within the range of the data)
competitor_a = 0 # The first competitor's index
competitor_b = 0 # The second competitor's index
points = 0 # The player's current standing
answer = 0 # The index of the competitor with more followers
guess = "" # The player's guess, 'A' or 'B'

## Get random number
def get_random():
    return randint(0, 49)

random_index = get_random()

## Get first competitor's index
def get_competitor_a(random_index):
    return random_index - 1 # So it's never same as competitor_b

competitor_a = get_competitor_a(random_index)

## Get second competitor's index
def get_competitor_b(random_index):
    return random_index
    
competitor_b = get_competitor_b(random_index)

## Display logo
def display_logo():
    print(logo)

display_logo()

## Display a competitor's information
def display_competitors(competitor_a, competitor_b):
    
    def display_a_competitor(competitor):
        if competitor == competitor_a:
            compare = "Compare A:"
        else: compare = "Against B:"
        print(f"{compare} {data[competitor]['name']}, a {data[competitor]['description']} from {data[competitor]['country']}")

    display_a_competitor(competitor_a)
    #print(f"Competitor A: {competitor_a}, Competitor B: {competitor_b}")

    ## Display "vs"
    def display_vs():
        print(vs)
        
    display_vs()

    display_a_competitor(competitor_b)

display_competitors(competitor_a, competitor_b)

## User Input
def get_user_input():
    return input(f"Who has more followers? Type, 'A' or 'B'? ").lower()

guess = get_user_input()

## Evaluate guess
def get_answer():
    if data[competitor_a]['follower_count'] > data[competitor_b]['follower_count']:
        answer = "a"
    else: answer = "b"
    print(f"Answer is: {answer.upper()}")
    return answer
    
answer = get_answer()

def evaluate_guess(guess):
    if guess == answer:
        print(f"You were correct! You have {points + 1} points.")
        return points + 1
    else: print(f"You were wrong, game over! Final score: {points}")

points = evaluate_guess(guess)

## Following game rounds
while guess == answer:
    clear()
    display_logo()
    evaluate_guess(guess) # Clears terminal, displays logo and the current score again
    competitor_a = competitor_b
    random_index = get_random()
    competitor_b = get_competitor_b(random_index)
    display_competitors(competitor_a, competitor_b)
    #print(f"Competitor A: {competitor_a}, Competitor B: {competitor_b}")
    guess = get_user_input()
    answer = get_answer()
    points = evaluate_guess(guess)
