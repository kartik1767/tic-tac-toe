from ast import Pass
from turtle import position


board = [ "-", "-", "-" ,
        "-" , "-", "-",
        "-", "-", "-"]

# If game is still going
game_is_still_going = True

# Winner/ Tied
winner = None

# Current Player Info
current_player = "X"

def display_board():
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def play_game():
    
    
    #Displaying of Initial Board
    display_board()
    
    while game_is_still_going:
        
        handle_turn(current_player)
        
        check_if_game_over()
        
        flip_player()
        
    #The game has ended
    if winner == "X" or winner == "O":
        print( winner + "  WON!")
    elif winner == None:
        print("Tie!")   
    
    
    # display_board()
    

def handle_turn(player):
    
    print(player + "'s turn!")
    position = (input(" Enter any number from 1-9 : "))
    
    valid = False
    while not valid:
        while position not in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            position = input("Invalid Input! Enter any number from 1-9 : ")
        
        position = int(position) - 1
        
        if board[position] == "-":
            valid  = True
        else:
            print("Uou can't go there. Go Again. ")
    
    board[position] = player
    display_board()
    
def check_if_game_over():
    check_for_winner()
    check_if_tie()
    

def check_for_winner():
    
    global winner
    
    #check for rows
    row_winner = check_row()
    
    #check for diagonals
    diagonal_winner = check_diagonal()
    
    #check for columns
    column_winner = check_column()
    
    # Get the Winner
    if row_winner:
        winner = row_winner
    elif column_winner:
        winner = column_winner
    elif diagonal_winner:
        winner = diagonal_winner
    else:
        winner = None
    
    return


def check_row():
    # Set up the global variable
    global game_is_still_going
    
    # check if any of the rows have all the same value 
    row_1 = board[0] == board[1] == board[2] != "-"
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"
    
    # If any row does have a match flag that there is a win
    if row_1 or row_2 or row_3:
        game_is_still_going = False
    
    if row_1:
        return board[0]
    elif row_2:
        return board[3]
    elif row_3:
        return board[6]
    return   
    
def check_diagonal():
    # Set up the global variable
    global game_is_still_going
    
    # check if any of the diagonal have all the same value 
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"
    
    # If any row does have a match flag that there is a win
    if diagonal_1 or diagonal_2:
        game_is_still_going = False
    
    if diagonal_1:
        return board[0]
    elif diagonal_2:
        return board[2]
    return

def check_column():
    # Set up the global variable
    global game_is_still_going
    
    # check if any of the column have all the same value 
    column_1 = board[0] == board[3] == board[6] != "-"
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"
    
    # If any column does have a match flag that there is a win
    if column_1 or column_2 or column_3:
        game_is_still_going = False
    
    if column_1:
        return board[0]
    elif column_2:
        return board[1]
    elif column_3:
        return board[2]
    return


def check_if_tie():
    global game_is_still_going
    
    if "-" not in board:
        game_is_still_going = False
    return

def flip_player():
    global current_player
    
    if current_player == "X":
        current_player = "O"
        
    elif current_player == "O":
        current_player= "X"
    return
    
    
    
play_game()