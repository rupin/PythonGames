print("Welcome to the Maze Solver!")

# Maze layout (0: empty, 1: wall, S: start, E: end)
maze = [
    ["|", "|", "|", "|", "|"],
    ["|", 'S', " ", " ", "|"],
    ["|", "|", "|", " ", "|"],
    ["|", " ", " ", " ", 'E'],
    ["|", "|", "|", "|", "|"],
]

current_position = (1, 1)

# Main loop for navigating the maze
for _ in range(10):  # You can adjust the number of moves
    print("Current Maze:")
    for row in maze:
        print(" ".join(str(cell) for cell in row))
    
    direction = input("Enter direction (up, down, left, right): ").lower()

    # Update the player's position based on the chosen direction
    if direction == "up" and maze[current_position[0] - 1][current_position[1]] != 1:
        current_position = (current_position[0] - 1, current_position[1])
    elif direction == "down" and maze[current_position[0] + 1][current_position[1]] != 1:
        current_position = (current_position[0] + 1, current_position[1])
    elif direction == "left" and maze[current_position[0]][current_position[1] - 1] != 1:
        current_position = (current_position[0], current_position[1] - 1)
    elif direction == "right" and maze[current_position[0]][current_position[1] + 1] != 1:
        current_position = (current_position[0], current_position[1] + 1)
    else:
        print("Invalid move. Try again.")
        continue

    # Check if the player has reached the end
    if maze[current_position[0]][current_position[1]] == 'E':
        print("Congratulations! You reached the end of the maze.")
        break

print("Thank you for playing!")
