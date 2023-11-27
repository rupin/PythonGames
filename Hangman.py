import random

words = ["python", "hangman", "programming", "computer", "keyboard", "developer", "openai", "language"]
secret_word = random.choice(words)
guessed_letters = []
attempts = 6

print("Welcome to Hangman!")

while attempts > 0:
    print("\nAttempts left:", attempts)

    current_display = ""
    for letter in secret_word:
        if letter in guessed_letters:
            current_display += letter + " "
        else:
            current_display += "_ "

    print("Current word:", current_display.strip())

    guess = input("Guess a letter: ").lower()

    if len(guess) != 1 or not guess.isalpha():
        print("Invalid input. Please enter a single letter.")
        continue

    if guess in guessed_letters:
        print("You've already guessed that letter. Try again.")
        continue

    guessed_letters.append(guess)

    if guess not in secret_word:
        attempts -= 1
        print("Incorrect guess!")

    if set(guessed_letters) == set(secret_word):
        print("Congratulations! You guessed the word:", secret_word)
        break

if attempts == 0:
    print("Sorry, you ran out of attempts. The correct word was:", secret_word)
