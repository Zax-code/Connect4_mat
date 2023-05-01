from board import Board
from ai import IAplay

if __name__ == "__main__":
    board = Board()
    board.print_board()
    i = 0
    while not board.winner and board.chips != 0:
        if i % 2 == 1:
            move = IAplay(board, 3)
            print("AI played: ", move+1)
        else:
            while True:
                col = -1
                try:
                    col = int(input("Enter column: ")) - 1
                except ValueError:
                    print("Invalid move")
                    continue
                if not board.play(col):
                    print("Invalid move")
                    continue
                break
        i += 1

        board.print_board()
        if board.winner:
            print("Winner: ", board.winner)
            break
