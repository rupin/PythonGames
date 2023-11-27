import random

print("Welcome to Rock, Paper, Scissors!")

# Main loop for playing the game
for _ in range(3):  # You can adjust the number of rounds as needed
    # Get user's choice
    user_choice = input("Enter your choice (Rock, Paper, or Scissors): ").lower()

    # Validate user input
    if user_choice not in ["rock", "paper", "scissors"]:
        print("Invalid choice. Please enter Rock, Paper, or Scissors.")
        continue

    # Generate computer's choice
    computer_choice = random.choice(["rock", "paper", "scissors"])

    print(f"\nComputer chose: {computer_choice}")

    # Determine the winner
    if user_choice == computer_choice:
        print("It's a tie!")
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("You win!")
    else:
        print("Computer wins!")

    print("-" * 30)

print("Thank you for playing!")
