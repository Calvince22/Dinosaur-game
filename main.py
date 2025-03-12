import random

def guess_number_game():
    print("\n🎲 Welcome to Guess the Number! 🎲")
    print("Try to guess a number between 1 & 10.")

    secret_number = random.randint(1, 10)
    attempt = 0

    while True:
        try:
            guess = int(input("Enter guess: "))  # Convert input to integer
            attempt += 1

            if guess < secret_number:
                print("🔼 Too low!")
                if abs(guess - secret_number) == 1:
                    print("🔥 Very close!")
            elif guess > secret_number:
                print("🔽 Too high!")
                if abs(guess - secret_number) == 1:
                    print("🔥 Very close!")
            else:
                print(f"🎉 Congratulations! You guessed the number {secret_number} in {attempt} attempts!")
                break  # Exit the loop

        except ValueError:
            print("❌ Invalid input! Please enter a number.")

# Run the game
guess_number_game()
