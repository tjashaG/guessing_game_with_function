import random

MIN_NUM = 1
MAX_NUM = 1000
SECRET = random.randint(MIN_NUM, MAX_NUM)
guess = None
# function 1 = check if guess is correct
def check_if_guessed(number):
    number_of_guesses = 0
    if number == SECRET:
            print(f"You guessed it! The number was {SECRET}.")
    elif number < SECRET:
            print("Wrong number. Try higher!")
            number_of_guesses += 1
    else:
            print("Wrong number. Go lower!")
            number_of_guesses += 1
    return number_of_guesses

print(SECRET)

while guess != SECRET:
    guess = int(input(f"Guess a number between {MIN_NUM} and {MAX_NUM}: "))
    while guess < 1 or guess > 1000:
        print(f"Between {MIN_NUM} and {MAX_NUM}, DUMBASS!")
        guess = int(input(f"Guess a number between {MIN_NUM} and {MAX_NUM}: "))
    check_if_guessed(guess)
#print(check_if_guessed(guess))





