import random
from hangman_stages import hangman_stages
import json


# Load the word list from the JSON file
def load_word_list():
    try:
        with open('word_list.json', 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        print("The word_list.json file was not found.")
        return {}


def main():
    print("Welcome to the Hangman game!")
    print("Let's start playing!")

    # Load word list from the JSON file
    word_list = load_word_list()

    # If the word list is empty, exit the game
    if not word_list:
        print("No word list available. Exiting.")
        return

    while True:  # This allows the game to restart and choose a new category
        # Get the category from the user
        category = choose_category(word_list)

        # Start the game
        game_setup(word_list, category)

        # Ask if the user wants to play again
        play_again = input("Do you want to play again? (yes/no): ").strip()
        while play_again.lower() not in ["yes", "no"]:
            print("Invalid input. Please enter 'yes' or 'no'.")
            play_again = input("Do you want to play again? (yes/no): ").strip()

        if play_again.lower() != "yes":
            print("Thanks for playing! Goodbye!")
            break


def choose_category(word_list):
    print("Choose a category:")
    categories = list(word_list.keys())  # Get the list of categories
    for i, category in enumerate(categories, 1):
        print(f"{i}. {category}")

    while True:
        try:
            choice = int(input("Enter the number of your choice: ")) - 1
            selected_category = categories[choice]
            return selected_category
        except (ValueError, IndexError):
            print("Invalid input. Please choose a valid number from the list.")


def game_setup(word_list, category):
    attempts = 6
    guessed_letters = []  # Keep track of guessed letters
    choose_word(word_list[category], attempts,
                guessed_letters)  # Pass selected category's word list and guessed letters


def choose_word(word_list, attempts, guessed_letters):
    random_word = random.choice(word_list)  # Pick a random word
    display_word = ["_"] * len(random_word)  # Set up the word with underscores

    while attempts > 0 and "_" in display_word:  # Continue until attempts run out or word is guessed
        print(f"Attempts left: {attempts}")
        print("Word to guess:", " ".join(display_word))
        print(hangman_stages[6 - attempts])  # Display the hangman figure based on remaining attempts

        print("Used letters:", ", ".join(sorted(guessed_letters)))  # Show the letters that have already been guessed

        guess = guess_letter()  # Get the letter guess from the player

        if guess in guessed_letters:  # Check if the letter has already been guessed
            print(f"You've already guessed {guess}. Try a different letter.")
            continue

        if guess in random_word:  # Correct guess
            for i in range(len(random_word)):
                if random_word[i] == guess:
                    display_word[i] = guess
            print(f"Good job! {guess} is in the word.")
        else:  # Incorrect guess
            attempts -= 1
            print(f"Sorry! {guess} is not in the word.")
            print(f"You have {attempts} attempts left.")

        guessed_letters.append(guess)  # Add guessed letter to the list

    if "_" not in display_word:
        print("Congratulations! You guessed the word:", random_word)
    else:
        print("Game over! The word was:", random_word)


def guess_letter():
    while True:
        guess = input("Enter a letter: ").lower()  # Get user input and convert to lowercase
        if len(guess) == 1 and guess.isalpha():  # Validate input (only a single letter)
            return guess
        else:
            print("Invalid input. Please enter a single letter.")


if __name__ == "__main__":
    main()
