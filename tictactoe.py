def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-"*9)

def check_winner(board,player):
    for row in board:
        if row.count(player) ==3:
            return True
    
    for col in range(3):
        column = []
        for row in range(3):
            column.append(board[row][col])
        if column.count(player) == 3:
            return True
    
    left_to_right_diagonal = []
    for i in range(3):
        left_to_right_diagonal.append(board[i][i])
    if left_to_right_diagonal.count(player) == 3:
        return True
    
    right_to_left_diagonal = []
    for i in range(3):
        right_to_left_diagonal.append(board[i][2-i])
    if right_to_left_diagonal.count(player) == 3:
        return True
    return False

def is_draw(board):
    for row in board:
        if " " in row:
            return False
    return True

def get_move(board, player):
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
    board = []
    for i in range(3):
        row = []
        for j in range(3):
            row.append(" ")
        board.append(row)
    
    player1 = input("player 1 choose X or O: ").upper()
    while player1 not in "XO":
        player1 = input("Invalid choice, choose X or O: ").upper()
    if player1 == "X":
        player2 ="O"
    else:
        player2 = "X"
    
    current_player = player1

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
            if current_player == player1:
                current_player = player2
            else:
                current_player = player1

if __name__ == "__main__":
    main()