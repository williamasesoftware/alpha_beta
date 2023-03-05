import unittest
from main_value import TicTacToe

class TestTicTacToe(unittest.TestCase):
    
    def test_x_wins(self):
        game = TicTacToe()
        game.board[0][0] = 'X'
        game.board[1][1] = 'O'
        game.board[0][1] = 'X'
        game.board[2][2] = 'O'
        game.board[0][2] = 'X'
        self.assertEqual(game.alphabeta_value(), -1)
        
    def test_o_wins(self):
        game = TicTacToe()
        game.board[0][0] = 'X'
        game.board[1][1] = 'O'
        game.board[0][1] = 'X'
        game.board[1][0] = 'O'
        game.board[2][2] = 'X'
        game.board[2][1] = 'O'
        self.assertEqual(game.alphabeta_value(), 1)
    
    """
    def test_tie(self):
        game = TicTacToe()
        game.board = [['X', 'O', 'X'], 
                    ['O', 'X', 'O'], 
                    ['O', 'X', 'O']]
        self.assertEqual(game.evaluate_board(), 0)
    """
        
if __name__ == '__main__':
    unittest.main()
