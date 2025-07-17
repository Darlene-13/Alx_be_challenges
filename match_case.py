import random

secret_number = random.randint(1,10)   # THis will generate random integers between 1 and 10
guess_count = 0 

while True:
    user_input = input("Enter a any random number between 1 and 10:")

    #Match case statement to validate user input
    match user_input:
        case _ if user_input.isdigit():
            number = int(user_input)
            guess_count +=1

            if 1 <= number <=10:
                if number == secret_number:
                    print(f"Congratulations! You entered a valid number: {number}")
                    print(" Wow you guesses the correct number!")
                    print(f"You guessed it in {guess_count} attempts.")
                    break
                elif number < secret_number:
                    print("Your guess it too low, try again!")
                else:
                    print("Your guess it too high, try again!")
            else:
                print("Please enter a number between 1 and 10.")
        case _:
            print("Invalid input please guess a number between 1 and 10.")
