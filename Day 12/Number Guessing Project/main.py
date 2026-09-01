import art
import random

print(art.logo)
computer_guess = random.randint(1, 100)

print("Welcome to the number guessing game!")
print("I am thinking of a number between 1 and 100.")
difficulty = input("Choose a Difficulty.Type 'easy' or 'hard' :")
if difficulty == 'easy':
    attempts = 10
elif difficulty == 'hard':
    attempts = 5

while attempts > 0:
    user_guess = int(input("Guess a number between 1 and 100: "))
    if user_guess == computer_guess:
        print(f"you guessed Correctly. The Computer Also Guessed {computer_guess}.")
        break
    elif user_guess > computer_guess:
        print("Too High")
        print("Guess Again")
    elif user_guess < computer_guess:
        print("Too Low")
        print("Guess Again")
    attempts = attempts - 1
    print(f"You have {attempts} attempts remaining to guess the number.")

if attempts == 0:
    print(f"You've run out of attempts. The answer was {computer_guess}.")







