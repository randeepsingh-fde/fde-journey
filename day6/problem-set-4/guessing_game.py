import random

while True:
    try:
        level = int(input("Level: "))
        if level >= 1:
            break
    except ValueError:
        print("Enter a valid positive integer.")

n = random.randint(1, level)

while True:
    try:
        guess = int(input("Guess the number: "))
        if guess >= 1:
            if guess < n:
                print("Too Small!")
            elif guess > n:
                print("Too Large!")
            else:
                print("Just Right!")
                break
    except ValueError:
        print("Enter a valid guess.")