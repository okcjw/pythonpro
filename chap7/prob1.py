import random 

def display_instruct():
    print("    Welcome to greatest intellectual challenge of all time: Tic-Tac-Toe.")
    print("    This will be a showdown between your human brain and my silicon processor.\n")
    print("    You will make your move known by entering a number. 0 - 8. The number\n    will correspond to the board position as illustrated:")
    print("\t\t    0 | 1 | 2 ")
    print("\t\t   -----------")
    print("\t\t    3 | 4 | 5 ")
    print("\t\t   -----------")
    print("\t\t    6 | 7 | 8 ")
    print("    Prepare yourself, human. The ultimate battle is about to begin.\n")

def ask_yes_no():
    while True:
        response = input("Do you require the first move? (y/n): ")
        if response == 'y':
            return True
        elif response == 'n':
            return False
        else:
            print("Please enter 'y' or 'n'.")    

def ask_number(question, low, high):
    while True:
        try:
            response = int(input(question))
            if low <= response <= high:
                return response
            else:
                print("Please enter a valid number within the specified range.")
        except ValueError:
            print("Please enter a valid number.")

def pieces():
    return ('X', 'O')

def new_board():
    board = [' '] * 9
    return board

def display_board(board):
    print("")
    print(f"\t{board[0]} | {board[1]} | {board[2]} ")
    print("\t----------")
    print(f"\t{board[3]} | {board[4]} | {board[5]} ")
    print("\t----------")
    print(f"\t{board[6]} | {board[7]} | {board[8]} \n")

def human_move(board, human):
    while True:
        move = int(input("human's turn. Where will you move? <0 - 8>:"))
        if move in range(9) and board[move] == ' ':
            print("Fine..")
            return move
        else:
            print("Invalid move. Try again.")

def computer_move(board, human, computer):
    while True:
        move = random.randint(0, 8)
        if board[move] == ' ':
            print("I shall take square number", move)
            print("")
            return move

def legal_moves(board):
    return [i for i, val in enumerate(board) if val == ' ']

def next_turn(turn):
    return 'X' if turn == 'O' else 'O'

def winner(board):
    win_conditions = [(0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6), (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)]
    for condition in win_conditions:
        if board[condition[0]] == board[condition[1]] == board[condition[2]] != ' ':
            return board[condition[0]]
    if ' ' not in board:
        return 'Tie'
    return None

def congratulate_winner(winner, human, computer):
    if winner == human:
        print("O won!\n")
        print("As I predicted, human, I am triumphat once more.")
        print("Proof that computers are superior to humans in all regards.\n")
    elif winner == computer:
        print("X won!")
        print("No, no! It cannot be! somehow you tricked me, human.")
        print("But never again! I, the computer, so swears it!\n")
    else:
        print("It's a tie!")

def main():
    display_instruct()
    computer, human = pieces()

    first_turn = ask_yes_no()
    if first_turn == True:
        turn = human
    else:
        turn = computer
    
    board = new_board()

    display_board(board)

    while not winner(board):
        if turn == human:
            move = human_move(board, human)
            board[move] = human
        else:
            move = computer_move(board, human, computer)
            board[move] = computer

        display_board(board)
        turn = next_turn(turn)

    cwinner = winner(board)
    congratulate_winner(cwinner, human, computer)

if __name__ == "__main__":
    main()
    input("Press the enter key to quit.")
