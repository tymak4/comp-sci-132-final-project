def print_board(board):
    #prints the board as a 3x3 grid of squares seperated by lines 
    for row in board:
        print(" | ".join(row))
        print("-"*9) 

def check_winner(board,player):
    #this function checks whenever if any of the players has 3 in a row and if so returns True

    #this for loop checks if any of the players has 3 in a row horrizontally
    for row in board:
        if row.count(player) ==3:
            return True
    
    #this for loop checks if any of the players has 3 in a row via up and down
    for col in range(3):
        column = []
        for row in range(3):
            column.append(board[row][col])
        if column.count(player) == 3:
            return True
    
    #this checks if the player has 3 in a row in a left to right diagnol pattern
    left_to_right_diagonal = []
    for i in range(3):
        left_to_right_diagonal.append(board[i][i])
    if left_to_right_diagonal.count(player) == 3:
        return True
    

    #this checks of the player has 3 in a row in a right to left diagonal pattern
    right_to_left_diagonal = []
    for i in range(3):
        right_to_left_diagonal.append(board[i][2-i])
    if right_to_left_diagonal.count(player) == 3:
        return True
    return False

def is_draw(board):
    #this function checks whenever both players cannot win by checking if the board is full
    for row in board:
        if " " in row:
            return False
    return True

def get_move(board, player):
    #this function gets the move of the player as an input either X or O, where they want to put it, 
    # and handles edges cases
    while True:
        try:
            row = int(input(f'player {player}, enter row (0-2): '))
            col = int(input(f'player {player}, enter col (0-2): '))

            if row < 3 and col < 3 and row >= 0 and col >= 0 and type(row) == int and type(col) == int:
                if board[row][col] == " ":
                    return row, col
                else:
                    print("That spot is already taken, please input another choice")
            else:
                print(f'please input a valid choice')
        except:
            print("invalid input, please try again")

def main():
    #creates a board using a 2D list
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        board.append(row)
    
    #handles the user input and the invalid inputs
    player1 = input("player 1 choose X or O: ").upper()
    while player1 not in "XO":
        player1 = input("Invalid choice, choose X or O: ").upper()
    if player1 == "X":
        player2 ="O"
    else:
        player2 = "X"
    
    current_player = player1

    #runs a loop checking each input if any of the players has won or both players tied
    game_over = False
    while not game_over:
        print_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player
        if check_winner(board, current_player):
            print_board(board)
            print(f'Player {current_player} wins!')
            game_over = True
        if is_draw(board):
            print_board(board)
            print("draw")
            game_over = True
        else:
            #switches the current player each turn so that both people can input their choice
            # and can determine who won 
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1

if __name__ == "__main__":
    main()