import random
import time
from typing import Optional


# set the high scores for different difficulty levels
high_scores: dict[str, Optional[int]] = {
    "Easy": None,
    "Medium": None,
    "Hard": None
}

# auto hinf  level 
def auto_hint(target: int) -> str:
    parity = "even" if target % 2 == 0 else "odd"
    range_hint = "lower half (1–50)" if target <= 50 else "upper half (51–100)"
    return f"Hint: The number is {parity} and in the {range_hint}."



def select_difficulty() -> tuple[int, str, bool]:
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    print("Choose your difficulty level:")
    print("1. Easy (10 chances)")
    print("2. Medium (5 chances)")
    print("3. Hard (3 chances)")

    # loop of playing the game 
    while True:
        try:
            choice = int(input("Enter your choice (1/2/3): "))
            if choice == 1:
                return 10, "Easy", False
            elif choice == 2:
                return 5, "Medium", False
            elif choice == 3:
                return 3, "Hard", True
            else:
                print("Invalid choice. Try 1, 2, or 3.")
        except ValueError:
            print("That doesn’t look like a number. Try again.")

# game the number using the random module
def generate_jackpot() -> int:
    return random.randint(1, 100)

def process_guess(guess: int, jackpot: int) -> str:
    if guess < jackpot:
        return f"Incorrect! The number is higher than {guess}.\n"
    elif guess > jackpot:
        return f"Incorrect! The number is lower than {guess}.\n"
    else:
        return "correct"

def update_high_score(difficulty: str, attempts: int):
    current_best = high_scores.get(difficulty)
    if current_best is None or attempts < current_best:
        high_scores[difficulty] = attempts
        print("New high score for", difficulty, "mode!")
    else:
        print("Your best score for", difficulty, "mode is", current_best, "attempt" + ("s" if current_best > 1 else ""))

def handle_hint(jackpot: int, attempts: int, hint_enabled: bool, hint_given: bool) -> bool:
    if hint_enabled and not hint_given and attempts >= 3:
        print(auto_hint(jackpot), "\n")
        return True
    return hint_given

def play_round(max_attempts: int, difficulty: str, hint_enabled: bool, jackpot: int):
    attempts = 0
    hint_given = False

    while attempts < max_attempts:
        user_input = input(f"Attempt {attempts + 1} of {max_attempts} — Your guess (or type 'hint'): ").strip().lower()

        if user_input == "hint":
            if hint_enabled:
                print(auto_hint(jackpot), "\n")
            else:
                print("Hints are only available in Hard mode.\n")
            continue

        try:
            guess = int(user_input)
            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.\n")
                continue

            attempts += 1
            result = process_guess(guess, jackpot)

            if result == "correct":
                print(f"Congratulations! You guessed the correct number in {attempts} attempt{'s' if attempts > 1 else ''}. The number was {jackpot}.")
                update_high_score(difficulty, attempts)
                return

            print(result)
            hint_given = handle_hint(jackpot, attempts, hint_enabled, hint_given)

        except ValueError:
            print("That wasn’t a valid number. Try typing digits only.\n")

    print(f"You've used all {max_attempts} attempts. The correct number was {jackpot}. Better luck next time.")
    current_best = high_scores.get(difficulty)
    if current_best:
        print("Your best score for", difficulty, "mode is", current_best, "attempt" + ("s" if current_best > 1 else ""))

def play_again():
    try:
        again = int(input("Type 1 to play again, or any other key to exit: "))
        if again == 1:
            print("\nRestarting the game...\n")
            guess_game()
        else:
            print("Thank you for playing! Goodbye!")
    except ValueError:
        print("Invalid input. Exiting the game. Goodbye!")

def guess_game():
    max_attempts, difficulty, hint_enabled = select_difficulty()
    jackpot = generate_jackpot()
    start = time.time()
    play_round(max_attempts, difficulty, hint_enabled, jackpot)
    end = time.time()
    print(f"\nGame duration: {end - start:.2f} seconds.")
    play_again()

def main():
    guess_game()

if __name__ == "__main__":
    main()
