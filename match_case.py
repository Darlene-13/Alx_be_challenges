import random

random.randint(1,10)   # THis will generate random integers between 1 and 10
UserInput = input("Enter a any random number:")

match UserInput:
    case UserInput if UserInput.isdigit() and 1 <= int(UserInput) <= 10:
        print(f"Congradulations!! You entered a valid number: {UserInput}")
    case UserInput if UserInput.isdigit() < 1:
        print("Ooops your guess is a bit too low, try again!")
    case UserInput if not UserInput.isdigit() > 10:
        print("Ooops your guess is a bit too high, try again!")