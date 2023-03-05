class TicTacToe:
    
    def __init__(self, board=None, player='X'):
        if board is None:
            self.board = [['-' for i in range(3)] for j in range(3)]
        else:
            self.board = board
        self.player = player
        
    def print_board(self):
        for row in self.board:
            print(' '.join(row))
        print('\n')
        
    def game_over(self):
        for i in range(3):
            if self.board[i][0] != '-' and self.board[i][0] == self.board[i][1] and self.board[i][1] == self.board[i][2]:
                return True
            if self.board[0][i] != '-' and self.board[0][i] == self.board[1][i] and self.board[1][i] == self.board[2][i]:
                return True
        if self.board[0][0] != '-' and self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2]:
            return True
        if self.board[0][2] != '-' and self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0]:
            return True
        for row in self.board:
            if '-' in row:
                return False
        return True
    
    def evaluate_board(self):
        if self.game_over():
            if self.player == 'X':
                return -1
            else:
                return 1
        else:
            return 0
    
    def generate_children(self):
        children = []
        for i in range(3):
            for j in range(3):
                if self.board[i][j] == '-':
                    child = TicTacToe([row[:] for row in self.board], 'X' if self.player == 'O' else 'O')
                    child.board[i][j] = self.player
                    children.append(child)
        return children
    
    def min_value(self, alpha, beta):
        if self.game_over():
            return self.evaluate_board()
        v = float('inf')
        for child in self.generate_children():
            v = min(v, child.max_value(alpha, beta))
            if v <= alpha:
                return v
            beta = min(beta, v)
        return v
    
    def max_value(self, alpha, beta):
        if self.game_over():
            return self.evaluate_board()
        v = float('-inf')
        for child in self.generate_children():
            v = max(v, child.min_value(alpha, beta))
            if v >= beta:
                return v
            alpha = max(alpha, v)
        return v
    
    def alphabeta_value(self):
        if self.player == 'X':
            return self.max_value(float('-inf'), float('inf'))
        else:
            return self.min_value(float('-inf'), float('inf'))


game = TicTacToe()
game.print_board()

game.board[0][0] = 'X'
game.board[1][1] = 'O'
game.board[0][1] = 'X'
game.board[2][2] = 'O'
game.board[0][2] = 'X'

game.print_board()

print("Probabilidad de ganar para X:", game.alphabeta_value())


game = TicTacToe()
game.print_board()

game.board[0][0] = 'X'
game.board[1][1] = 'O'
game.board[0][1] = 'X'
game.board[1][0] = 'O'
game.board[2][2] = 'X'
game.board[2][1] = 'O'

game.print_board()

print("Probabilidad de ganar para O:", game.alphabeta_value())


game = TicTacToe()
game.print_board()

game.board[0][0] = 'X'
game.board[1][1] = 'O'
game.board[0][1] = 'X'
game.board[2][0] = 'O'
game.board[1][0] = 'X'
game.board[2][2] = 'O'
game.board[0][2] = 'X'
game.board[2][1] = 'O'
game.board[1][2] = 'X'

game.print_board()

print("Probabilidad de ganar para X:", game.alphabeta_value())
