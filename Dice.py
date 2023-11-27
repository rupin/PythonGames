import random

print("Welcome to the Dice Rolling Simulator!")

# Main loop for rolling the dice
for _ in range(5):  # You can adjust the number of rolls as needed
    input("Press Enter to roll the dice...")
    
    # Simulate rolling a six-sided die
    dice_value = random.randint(1, 6)
    
    # Display the result
    print("You rolled:", dice_value)
    
    # Check for special conditions (e.g., doubles)
    if dice_value % 2 == 0:
        print("Even number!")
    else:
        print("Odd number!")

    if dice_value == 6:
        print("You rolled a six!")
    
    print("-" * 20)

print("Thank you for playing!")
