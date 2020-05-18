# Global Variables

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

#Check if we continue playing
game_is_playing = True

#To understand who is winner. Initially there is no winner
winner = None

#Create player, who starts first and check who is current player. Usually X starts first
current_player = "X"

# Show the board
def run_board():
  print(board[0] + " | " + board[1] + " | " + board[2] + "     1 | 2 | 3")
  print(board[3] + " | " + board[4] + " | " + board[5] + "     4 | 5 | 6")
  print(board[6] + " | " + board[7] + " | " + board[8] + "     7 | 8 | 9")

#Runs all the game
def run_game():

    #Should run initial board
    run_board()

    #The loop for each turn in the game
    while game_is_playing:

    #Create move in game for current player
        move(current_player)
    #Check if the game has ended
        check_for_gameover()
    #Switch to the second player
        switch_player()
    #End of the game
    if winner == "X" or winner == "O":
        print("Game over! " + winner + " won")
    elif winner == None:
        print("Game over, it's a tie")

# Handle a turn for an arbitrary player
def move(player):

  # Ask for move from the current player
    print(player + "'s turn.")
    position = input("Choose a position from 1-9: ")

  # Verification of the input
    valid = False
    while not valid:

    # If anything out of the range 1-9
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Error, please choose a position from 1-9: ")

        position = int(position) - 1

    # Check whether spot is available
        if board[position] == "-":
            valid = True
        else:
            print("Spot is unavailable, please try another one.")

    board[position] = player

    run_board()

def check_for_gameover():

    check_for_winner()

    check_for_tie()

def check_for_winner():
    # Set global variables
  global winner
  # Check if there was a winner anywhere
  row_winner = check_rows()
  column_winner = check_columns()
  diagonal_winner = check_diagonals()
  # Get the winner
  if row_winner:
    winner = row_winner
  elif column_winner:
    winner = column_winner
  elif diagonal_winner:
    winner = diagonal_winner
  else:
    winner = None


    # Check the rows for a win
def check_rows():
  # Set global variables
  global game_is_playing
  # Check if any of the rows have all the same value (and is not empty)
  row_1 = board[0] == board[1] == board[2] != "-"
  row_2 = board[3] == board[4] == board[5] != "-"
  row_3 = board[6] == board[7] == board[8] != "-"
  # If any row does have a match, flag that there is a win
  if row_1 or row_2 or row_3:
    game_is_playing = False
  # Return the winner
  if row_1:
    return board[0]
  elif row_2:
    return board[3]
  elif row_3:
    return board[6]
  # Or return None if there was no winner
  else:
    return None


# Check the columns for a win
def check_columns():
  # Set global variables
  global game_is_playing
  # Check if any of the columns have all the same value (and is not empty)
  column_1 = board[0] == board[3] == board[6] != "-"
  column_2 = board[1] == board[4] == board[7] != "-"
  column_3 = board[2] == board[5] == board[8] != "-"
  # If any column does have a match, flag that there is a win
  if column_1 or column_2 or column_3:
    game_is_playing = False
  # Return the winner
  if column_1:
    return board[0]
  elif column_2:
    return board[1]
  elif column_3:
    return board[2]
  # Or return None if there was no winner
  else:
    return None


# Check the diagonals for a win
def check_diagonals():
  # Set global variables
  global game_is_playing
  # Check if any of the columns have all the same value (and is not empty)
  diagonal_1 = board[0] == board[4] == board[8] != "-"
  diagonal_2 = board[2] == board[4] == board[6] != "-"
  # If any diagonal does have a match, flag that there is a win
  if diagonal_1 or diagonal_2:
    game_is_playing = False
  # Return the winner
  if diagonal_1:
    return board[0]
  elif diagonal_2:
    return board[2]
  # Or return None if there was no winner
  else:
    return None

def check_for_tie():
    # Set global variables
  global game_is_playing
  # If board is full
  if "-" not in board:
    game_is_playing = False
    return True
  # Else there is no tie
  else:
    return False

#We switch player for X to 0 and 0 to X
def switch_player():
  # Global variables
  global current_player
  # If the current player was X, make it O
  if current_player == "X":
    current_player = "O"
  # Or if the current player was O, make it X
  elif current_player == "O":
    current_player = "X"
    return


run_game()
