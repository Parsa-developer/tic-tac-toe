import random

def create_board():
    return [' ' for _ in range(9)]

def display_board(board):
    print('\n')
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print('-'*9)
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print('-'*9)
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("\nPositions: 1 | 2 | 3")
    print("           4 | 5 | 6")
    print("           7 | 8 | 9")

def check_win(board, player):
    for i in range(0, 9, 3):
        if board[i] == board[i+1] == board[i+2] == player:
            return True
    for i in range(3):
        if board[i] == board[i+3] == board[i+6] == player:
            return True
    if board[0] == board[4] == board[8] == player:
        return True
    if board[2] == board[4] == board[6] == player:
        return True
    return False

def is_board_full(board):
    return ' ' not in board

def get_available_moves(board):
    return [i for i, spot in enumerate(board) if spot==' ']

def minimax(board, depth, is_maximizing):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if is_board_full(board):
        return 0
    
    if is_maximizing:
        best_score = float('-inf')
        for move in get_available_moves(board):
            board[move] = 'O'
            score = minimax(board, depth + 1, False)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = float('-inf')
        for move in get_available_moves(board):
            board[move] = 'X'
            score = minimax(board, depth + 1, True)
            board[move] = ' '
            best_score = max(score, best_score)
        return best_score
    
def ai_move(board):
    best_score = float('-inf')
    best_move = None

    for move in get_available_moves(board):
        board[move] = 'O'
        score = minimax(board, 0, False)
        board[move] = ' '
        if score > best_score:
            best_score = score
            best_move = move
    return best_move

def player_move(board):
    while True:
        try:
            move = int(input("Enter your move (1-9): ")) - 1
            if 0 <= move <= 8 and board[move] == ' ':
                return move
            else:
                print("Invalid move! The position must be between 1-9 and not already taken.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")

def play_game():
    board = create_board()
    print("Welcome to Tic-Tac-Toe! 🎲")
    print("You are X, and the AI is O. Enter a number (1-9) to make your move.")
    display_board(board)

    while True:
        move = player_move(board)
        board[move] = 'X'
        display_board(board)

        if check_win(board, 'X'):
            print("Congratulations! You win! 🏆")
            break
        if is_board_full(board):
            print("It's a draw! 🤝")
            break
        print("AI's turn ...")
        ai_pos = ai_move(board)
        board[ai_pos] = 'O'
        display_board(board)

        if check_win(board, 'O'):
            print("AI wins! Better luck next time! 🤖")
            break
        if is_board_full(board):
            print("It's a draw! 🤝")
            break

def main():
    while True:
        play_game()
        play_again = input("\nWould you like to play again? (yes/no): ").lower()
        if play_again != "yes" and "y":
            print("Thanks for playing! 😊")
            break

if __name__ == "__main__":
    main()