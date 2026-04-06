# Tic-Tac-Toe CLI Game

# Function to display the board
def show_board(board):
    for row in board:                  # Loop through each row of the board
        print("|".join(row))           # Join elements with "|" and print (like X|O|X)
    print()                            # Print empty line for spacing


# Function to check if a player has won
def check_winner(board, player):
    for i in range(3):                 # Loop through 3 rows and columns
        
        # Check rows (horizontal win)
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True                # If all three are same → player wins
        
        # Check columns (vertical win)
        if board[0][i] == board[1][i] == board[2][i] == player:
            return True                # If all three are same → player wins
    
    # Check main diagonal (top-left to bottom-right)
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    
    # Check second diagonal (top-right to bottom-left)
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True
    
    return False                       # No winning condition met


# Function to check if the game is a draw
def check_draw(board):
    for row in board:                  # Loop through each row
        for cell in row:               # Loop through each cell
            if cell == " ":            # If any empty space exists
                return False           # Game is not finished → not a draw
    return True                        # No empty spaces → draw


# Main function to run the game
def play():
    # Create a 3x3 board filled with empty spaces
    board = [[" " for _ in range(3)] for _ in range(3)]
    
    turn = "X"                         # Start the game with player X

    while True:                        # Infinite loop (runs until break)
        show_board(board)              # Display current board
        print("Player", turn, "turn")  # Show which player's turn
        
        # Take input from user
        row = int(input("Enter row (0-2): "))
        col = int(input("Enter column (0-2): "))
        
        # Check if selected position is already used
        if board[row][col] != " ":
            print("Place already taken, try again")
            continue                  # Skip and ask for input again
        
        # Place player's mark (X or O) on the board
        board[row][col] = turn
        
        # Check if current player wins
        if check_winner(board, turn):
            show_board(board)         # Show final board
            print("Player", turn, "wins!")
            break                     # Stop the game
        
        # Check if the game is a draw
        if check_draw(board):
            show_board(board)
            print("It's a draw!")
            break                     # Stop the game
        
        # Switch player (X → O or O → X)
        if turn == "X":
            turn = "O"
        else:
            turn = "X"


# Start the game
play()