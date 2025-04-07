import random

print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100.")
print("Try to guess it!")

# Computer chooses a random number
secret_number = random.randint(1, 100)
attempts = 0
guessed = False

# Game loop
while not guessed:
    # User input
    try:
        guess = int(input("\nYour guess: "))
        attempts += 1
        
        # Check the guess
        if guess < 1 or guess > 100:
            print("Please enter a number between 1 and 100.")
        elif guess < secret_number:
            print("Too low! Try a higher number.")
        elif guess > secret_number:
            print("Too high! Try a lower number.")
        else:
            guessed = True
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!")
    except ValueError:
        print("That's not a valid number. Please try again.")

print("\nThanks for playing!")
