import random

def generate_secret_code():
    return [random.randint(0, 9) for _ in range(4)]

def give_feedback(secret_code, guess):
    cows = sum(1 for x, y in zip(secret_code, guess) if x == y)
    bulls = sum(1 for x in guess if x in secret_code) - cows
    return cows, bulls

# Example of usage:
secret_code = generate_secret_code()
attempts = 0

while True:
    guess = [int(x) for x in input("Enter your guess (4 digits): ")]
    attempts += 1

    if guess == secret_code:
        print(f"Congratulations! You guessed the code in {attempts} attempts.")
        break
    else:
        cows, bulls = give_feedback(secret_code, guess)
        print(f"Feedback: {cows} cows, {bulls} bulls. Try again.")
