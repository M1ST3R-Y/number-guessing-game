
import random


# Game settings
MIN_NUMBER = 1
MAX_NUMBER = 100
MAX_ATTEMPTS = 7


def play_game():
    """
    Starts one round of the Number Guessing Game.
    The player must guess a random number between 1 and 100.
    """

    secret_number = random.randint(MIN_NUMBER, MAX_NUMBER)
    attempts = 0

    print("\n===================================")
    print("       NUMBER GUESSING GAME")
    print("===================================")
    print(f"\nI have chosen a number between {MIN_NUMBER} and {MAX_NUMBER}.")
    print(f"You have {MAX_ATTEMPTS} attempts to guess it!")

    while attempts < MAX_ATTEMPTS:

        try:
            guess = int(input("\nEnter your guess: "))

            # Validate the input range
            if guess < MIN_NUMBER or guess > MAX_NUMBER:
                print(f"Please enter a number between {MIN_NUMBER} and {MAX_NUMBER}.")
                continue

            attempts += 1
            remaining_attempts = MAX_ATTEMPTS - attempts

            # Check the player's guess
            if guess == secret_number:
                print("\nCongratulations! You guessed the number!")
                print(f"The correct number was {secret_number}.")
                print(f"You guessed it in {attempts} attempt(s)!")
                return

            elif guess < secret_number:
                print("Too small! Try a higher number.")

            else:
                print("Too large! Try a lower number.")

            print(f"Attempts remaining: {remaining_attempts}")

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    # Maximum attempts reached
    print("\nGame over! You have used all your attempts.")
    print(f"The correct number was: {secret_number}")


def main():
    """Main function that controls the game."""

    print("Welcome to the Number Guessing Game!")
    print("Try to guess the secret number.")

    while True:
        play_game()

        # Ask the player whether to play again
        while True:
            replay = input("\nWould you like to play again? (yes/no): ")
            replay = replay.strip().lower()

            if replay in ("yes", "y"):
                break

            elif replay in ("no", "n"):
                print("\nThank you for playing! Goodbye!")
                return

            else:
                print("Invalid choice. Please enter yes or no.")


if __name__ == "__main__":
    main()\