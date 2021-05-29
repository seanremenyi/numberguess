import art
import random
import os

def check(number, guess, tries):
    if guess == number:
        print(f"You won, The answer was {guess}")
    elif guess > number:
        print(f"Too High")
        return tries -1
    else:
        print(f"Too Low")
        return tries -1

def difficulty():
    if input("Would you like easy or hard mode?\n") == "easy":
        return easy_tries
    else:
        return hard_tries



easy_tries = 10
hard_tries = 5

def game():
    number = random.randint(1,100)
    print(art.logo)
    print("Welcome to the game, I chose a number")
    tries = difficulty()
    guess = 0
    while guess != number:
        print(f"You have {tries} guesses left")
        guess = int(input("What is your guess\n"))
        tries = check(number, guess, tries)
        if tries == 0:
            print(f"Sorry, you lose, the answer was {number}")
            return
        
game()
        