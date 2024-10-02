"""
Let's play the tic-tac-toe game! MyHeuristics vs Basic Heuristics (Player A k=2 vs Player B k=2).
"""
from tictactoe import TicTacToe
from player import Player
from heuristics import Heuristics
from my_heuristics import MyHeuristics

# Define heuristics for both players
basic_h = Heuristics()
my_h = MyHeuristics()

# Define players using different heuristics and ply levels
playerA = Player('X', my_h, 'Player A')  # Player A using MyHeuristics
playerB = Player('O', basic_h, 'Player B')  # Player B using Basic Heuristics

# Set game simulation statistics
stats = {'Player A wins': 0, 'Player B wins': 0, 'Tied': 0}

# Set the board size of the game
board_size = 10

# Set ply levels
playerA.set_k_ply(2)  # Player A uses k=2 ply search
playerB.set_k_ply(2)  # Player B uses k=2 ply search

# Start the game simulation (10 matches, alternating starts)
game = TicTacToe(board_size, playerA, playerB, print_steps=False)

for i in range(5):
    # Player A starts first
    game.reset()
    game.set_players(playerA, playerB)
    result, winner = game.start()
    print(f"Game {2*i + 1} result: {result}")
    if winner is None:
        stats['Tied'] += 1
    else:
        stats['{} wins'.format(winner.name)] += 1

    # Player B starts first
    game.reset()
    game.set_players(playerB, playerA)
    result, winner = game.start()
    print(f"Game {2*i + 2} result: {result}")
    if winner is None:
        stats['Tied'] += 1
    else:
        stats['{} wins'.format(winner.name)] += 1

# Print final statistics after 10 games
print(f"\nFinal Results after 10 games:")
print(f"Player A (MyHeuristics) wins: {stats['Player A wins']}")
print(f"Player B (Basic Heuristics) wins: {stats['Player B wins']}")
print(f"Tied games: {stats['Tied']}")