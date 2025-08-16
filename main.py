import random

class TooShortValue(Exception):
    pass


class TooLargeValue(Exception):
    pass

class GuessError(Exception):
    """Base class for exceptions in this module."""
    pass

def guess_game():
    """
    A simple number guessing game where the player has to guess a randomly generated number between 1 and 100.
    The player receives feedback on whether their guess is too high or too low, and the game continues until the player guesses correctly.
    By - Mukesh Kumar 17/08/2025
    """

    jackpot = random.randint(1, 100)
    attempts = 0
    # Welcome message
    print("Welcome to the Number Guessing Game!")

    while True:
        try:
            guess = int(input("Enter your guess between 1-100 : "))
            if guess < 1 or guess > 100:
                raise GuessError("Guess must be between 1 and 100.")
            attempts += 1
            if guess < jackpot:
                raise TooShortValue("Your guess is too low, try again.")
            elif guess > jackpot:
                raise TooLargeValue("Your guess is too high, try again.")
            else:
                print(f"Congratulations! You've guessed the number {jackpot} in {attempts} attempts.")
                break
        except TooShortValue as e:
            print(e)
        except TooLargeValue as e:
            print(e)
        except GuessError as e:
            print(e)
        except ValueError:
            print("Invalid input. Please enter a valid number.")
    
    play_again()


def play_again():
    """
    Function to ask the player if they want to play again.
    If yes, it restarts the game; if no, it exits.
    By - Mukesh Kumar 17/08/2025
    """
    # print("Nice job! Do you want to play again?")
    again = int(input("Nice Job , type 1 to start the game :  "))
    if again == 1:
        guess_game()
    else:
        print("Thank you for playing! Goodbye!")

def main():
    """
    Main function to run the guessing game.
    by - Mukesh Kumar 17/08/2025
    """

    guess_game()



if __name__ == "__main__":
    main()
