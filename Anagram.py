import random

words = ["python", "hangman", "programming", "computer", "keyboard", "developer", "openai", "language"]
original_word = random.choice(words)
shuffled_word = list(original_word)
random.shuffle(shuffled_word)
shuffled_word = ''.join(shuffled_word)

print("Welcome to the Anagram Game!")
print("Unscramble the following word:", shuffled_word)

for attempt in range(3):
    guess = input("Your guess: ").lower()

    if guess == original_word:
        print("Congratulations! You guessed the correct word.")
        break
    else:
        print("Incorrect guess. Try again!")

else:
    print("Sorry, you ran out of attempts. The correct word was:", original_word)
