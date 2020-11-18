import random
import cmath
from pathlib import Path
import datetime

def try_again_easy():
    play_again = input("Do you want to play again? (y/n): ")
    while True:
        if play_again == "y":
            easy()
        else:
            break

def try_again_medium():
    play_again = input("Do you want to play again? (y/n): ")
    while True:
        if play_again == "y":
            medium()
        else:
            break

def try_again_difficult():
    play_again = input("Do you want to play again? (y/n): ")
    while True:
        if play_again == "y":
            difficult()
        else:
            break

#difficult version of game
def difficult():
    MIN_NUM = 1
    MAX_NUM = 1000
    SECRET = random.randint(MIN_NUM, MAX_NUM)
    number_of_guesses = 10
    guessed = False
    # save top score in txt file / read top score from txt file
    score = Path(".", "data", "scores_difficult")
    top_score = score.read_text()

    print("Welcome to the difficult level! You have only 10 guesses to get to the secret number!")
    print(f"The current high score is {top_score}")
    #print(SECRET) #testing purposes only

    while not guessed:
        guess = int(input(f"Guess the secret number between {MIN_NUM} and {MAX_NUM}: "))
        number_of_guesses -= 1
        print(f"Number of guesses remaining: {number_of_guesses}!")

        #re-prompts (dumbass) user to enter valid number within range
        while guess < 1 or guess > 1000:
            print(f"Between {MIN_NUM} and {MAX_NUM}, DUMBASS!")
            guess = int(input(f"Guess the secret number between {MIN_NUM} and {MAX_NUM}: "))

        if guess == SECRET:
            print(f"You guessed it! The number was {SECRET}.")
            if number_of_guesses > int(top_score):
                score.write_text(str(number_of_guesses))
                print(f"Congratulations! You broke the high score with {number_of_guesses} guesses remaining!")
            try_again_difficult()
            break
        elif guess < SECRET:
            print("Wrong number. Try higher!")
        else:
            print("Wrong number. Go lower!")
        if number_of_guesses == 0:
            print(f"Sorry, you have no more guesses! The secret number was {SECRET}")
            try_again_difficult()
            break


#game in medium difficulty
def medium():
    MIN_NUM = 1
    MAX_NUM = 1000
    SECRET = random.randint(MIN_NUM, MAX_NUM)
    guessed = False
    number_of_guesses = 12
    score = Path(".", "data", "scores_medium")
    top_score = score.read_text()
    print("Welcome to medium difficulty! You will have 12 guesses and a tolerance of +/- 5 numbers!")
    print(f"The current high score is {top_score}")
    #print(SECRET) #testing purposes only

    while not guessed:
        guess = int(input(f"Guess the secret number between {MIN_NUM} and {MAX_NUM}: "))
        number_of_guesses -= 1
        print(f"Number of guesses remaining: {number_of_guesses}")
        tolerance = cmath.isclose(guess, SECRET, abs_tol=5)

        while guess < 1 or guess > 1000:
            print(f"Between {MIN_NUM} and {MAX_NUM}, DUMBASS!")
            guess = int(input(f"Guess the secret number between {MIN_NUM} and {MAX_NUM}: "))

        if guess == SECRET: #if player guesses the exact number
            print(f"You guessed it! The secret number was {SECRET}!")
            if number_of_guesses > int(top_score):
                score.write_text(str(number_of_guesses))
                print(f"Congratulations! You broke the high score with {number_of_guesses} guesses remaining!")
            try_again_medium()
            break
        elif tolerance: #if player guesses within a 5 point tolerance
            number_of_guesses -= 1
            print(f"Close enough to win! The secret number was {SECRET}")
            if number_of_guesses > int(top_score):
                score.write_text(str(number_of_guesses))
                print(f"Congratulations! You broke the high score with {number_of_guesses} guesses remaining!")
            try_again_medium()
            break
        else:
            if guess > SECRET:
                print("Incorrect! Try a lower number!")
            elif guess < SECRET:
                print("Incorrect! Try a higher number!")
        if number_of_guesses == 0: #if player runs out of guesses
            print(f"Sorry, you have no more guesses! The secret number was {SECRET}")
            try_again_medium()
            break

#easy version of guessing game
def easy():
    MIN_NUM = 1
    MAX_NUM = 1000
    SECRET = random.randint(MIN_NUM, MAX_NUM)
    guessed = False
    number_of_guesses = 10
    score = Path(".", "data", "scores_easy")
    top_score = score.read_text()
    print("Welcome to easy difficulty! You will have 10 guesses and a tolerance of +/- 20 numbers!")
    print(f"The current high score is {top_score}")
    #print(SECRET)  # testing purposes only

    while not guessed:
        guess = int(input(f"Guess the secret number between {MIN_NUM} and {MAX_NUM}: "))
        tolerance = cmath.isclose(guess, SECRET, abs_tol=20)
        number_of_guesses -= 1
        print(f"Number of guesses remaining: {number_of_guesses}")

        #re-prompts if user enters number that is not in range
        while guess < 1 or guess > 1000:
            print(f"Between {MIN_NUM} and {MAX_NUM}, DUMBASS!")
            guess = int(input(f"Guess the secret number between {MIN_NUM} and {MAX_NUM}: "))

        # if user guesses the exact number
        if guess == SECRET:
            print(f"Congratulations! You guessed the number! It was {SECRET}")
            print(f"Guesses remaining: {number_of_guesses}")
            if number_of_guesses > int(top_score):
                score.write_text(str(number_of_guesses))
                print(f"Congratulations! You broke the high score with {number_of_guesses} guesses remaining!")
            try_again_easy()
            break
        #if user guesses number +/- 20 numbers from SECRET
        elif tolerance:
            print(f"Close enough! you win! The number was {SECRET}")
            if number_of_guesses > int(top_score):
                score.write_text(str(number_of_guesses))
                print(f"Congratulations! You broke the high score with {number_of_guesses} guesses remaining!")
            try_again_easy()
            break
        elif not tolerance:
            if guess > SECRET:
                print("Incorrect! Try lower!")
            elif guess < SECRET:
                print("Incorrect! Higher!")
        #if user doesn't guess the SECRET number in the given number of guesses
        if number_of_guesses == 0:
            print("Sorry, you ran out of guesses!")
            try_again_easy()
            break