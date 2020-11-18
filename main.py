from difficulty import *

if __name__ == "__main__":

    print("Welcome to the number guessing game, player!")
    level = int(input("Type 1 for easy, 2 for medium and 3 for difficult: "))

    if level == 1:
        easy()
    elif level == 2:
        medium()
    elif level == 3:
        difficult()
    else:
        print("Enter valid choice!")