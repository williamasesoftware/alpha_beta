from alphabeta import TicTacToe
from alphabeta import alpha_beta_value, max_value, min_value


def play(state):
    """Makes turn and prints the result of it until the game is over
    :param state: The initial state of the game (TicTacToe)
    """
    while not state.is_end_state():
        if state.is_max_node():
            print("Player X's turn")
        else:
            print("Player O's turn")

        # Use alpha-beta algorithm to decide next move
        best_child = max(state.generate_children(), key=lambda x: alpha_beta_value(x))

        # Make the move
        state = best_child
        print(state)

    # Print the final score
    score = state.value()
    if score == 0:
        print("It's a tie!")
    elif score == 1:
        print("Player X wins!")
    else:
        print("Player O wins!")


def main():
    """
    You need to implement the following functions/methods:
    play(state): makes turn and prints the result of it until the game is over
    value() in TicTacToe class: returns the current score of the game
    generate_children() in TicTacToe class: returns a list of all possible states after this turn
    alpha_beta_value(node): implements the MinMax algorithm with alpha-beta pruning
    max_value(node, alpha, beta): implements the MinMax algorithm with alpha-beta pruning
    min_value(node, alpha, beta):implements the MinMax algorithm with alpha-beta pruning
    """
    empty_board = 3 * '???'
    state = TicTacToe(empty_board, True)
    print(state)
    play(state)


if __name__ == '__main__':
    main()
