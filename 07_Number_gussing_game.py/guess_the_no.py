import random

secret_number = random.randint(1,100)  # Generate a random number between 1 and 100
print("Welcome to the Number Guessing Game!")

number = int(input("Enter your guess: "))  
#Get the user's guess
attempts = 0
while number != secret_number:
    attempts += 1
    if number < secret_number:
        print("Too low! Try again.")
    elif number > secret_number:
        print("Too high! Try again.")
    number = int(input("Enter your guess: "))  #Get the user's guess again
print("Congratulations!") 
print("It took you", attempts, "attempts to guess the number.")
