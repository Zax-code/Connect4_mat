class Board:
    def __init__(self):
        self.col = 12
        self.row = 6
        self.board = [[' ' for _ in range(self.col)] for _ in range(self.row)]
        self.turn = 'X'
        self.winner = None
        self.chips = self.col * self.row

    def undo(self, col):
        self.turn = 'X' if self.turn == 'O' else 'O'
        self.chips += 1
        self.winner = None
        for i in range(self.row):
            if self.board[i][col] != ' ':
                self.board[i][col] = ' '
                break

    def print_board(self):
        for row in self.board:
            print('|' + '|'.join(cell.center(5) for cell in row)+'|')
            print('|' + '|'.join('-'*5 for _ in row) + '|')
        print('|' + '|'.join(str(i).center(5)
                             for i, _ in enumerate(self.board[0], 1)) + '|')
        print('|' + '|'.join('_'*5 for _ in self.board[0]) + '|')
        print('|'+' '*(self.col*5+self.col-1)+'|')
        print()

    def play(self, col):
        if col >= self.col or col < 0:
            return False
        if self.board[0][col] != ' ':
            return False
        for i in range(self.row-1, -1, -1):
            if self.board[i][col] == ' ':
                self.board[i][col] = self.turn
                self.check_winner(col, i)
                self.chips -= 1
                self.turn = 'X' if self.turn == 'O' else 'O'
                return True

    def check_winner(self, col, row):
        if self.check_horizontal(col, row) or self.check_vertical(col, row) or \
                self.check_diagonal(col, row):
            self.winner = self.turn

    def check_horizontal(self, col, row):
        count = 1
        for i in range(1, 4):
            if col-i >= 0 and self.board[row][col-i] == self.turn:
                count += 1
            else:
                break
        for i in range(1, 4):
            if col+i < self.col and self.board[row][col+i] == self.turn:
                count += 1
            else:
                break

        return count >= 4

    def check_vertical(self, col, row):
        count = 1
        for i in range(1, 4):
            if row-i >= 0 and self.board[row-i][col] == self.turn:
                count += 1
            else:
                break
        for i in range(1, 4):
            if row+i < self.row and self.board[row+i][col] == self.turn:
                count += 1
            else:
                break

        return count >= 4

    def check_diagonal(self, col, row):
        count1 = 1
        count2 = 1
        for i in range(1, 4):
            if col-i >= 0 and row-i >= 0 and self.board[row-i][col-i] == self.turn:
                count1 += 1
            else:
                break
        for i in range(1, 4):
            if col+i < self.col and row+i < self.row and self.board[row+i][col+i] == self.turn:
                count1 += 1
            else:
                break
        for i in range(1, 4):
            if col + i < self.col and row - i >= 0 and self.board[row-i][col+i] == self.turn:
                count2 += 1
            else:
                break
        for i in range(1, 4):
            if col - i >= 0 and row + i < self.row and self.board[row+i][col-i] == self.turn:
                count2 += 1
            else:
                break
        return count1 >= 4 or count2 >= 4
