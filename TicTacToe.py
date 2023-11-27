# Initialize the empty Tic-Tac-Toe board
board = [[" " for _ in range(3)] for _ in range(3)]

# Display the Tic-Tac-Toe board
def display_board():
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check for a winner
def check_winner():
    # Check rows and columns
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] != " " or board[0][i] == board[1][i] == board[2][i] != " ":
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != " " or board[0][2] == board[1][1] == board[2][0] != " ":
        return True

    return False

# Main game loop
current_player = "X"

print("Welcome to Tic-Tac-Toe!")

for _ in range(9):
    display_board()

    row = int(input(f"Player {current_player}, enter row (0, 1, or 2): "))
    col = int(input(f"Player {current_player}, enter column (0, 1, or 2): "))

    # Check if the selected cell is empty
    if board[row][col] == " ":
        board[row][col] = current_player

        # Check for a winner
        if check_winner():
            display_board()
            print(f"Player {current_player} wins!")
            break

        # Switch to the other player
        current_player = "O" if current_player == "X" else "X"
    else:
        print("Cell already taken. Try again.")

else:
    display_board()
    print("It's a tie!")
