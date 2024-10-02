# my_heuristics.py
from heuristics import Heuristics
class MyHeuristics(Heuristics):
    def evaluate(self, board, player):
        opponent = 'O' if player == 'X' else 'X'
        score = 0

        # Evaluate rows, columns, and diagonals
        for i in range(len(board)):
            # Evaluate rows
            score += self.score_line(board[i], player, opponent)
            score += self.score_line([board[j][i] for j in range(len(board))], player, opponent)

        # Evaluate diagonals
        score += self.score_line([board[i][i] for i in range(len(board))], player, opponent)
        score += self.score_line([board[i][len(board) - 1 - i] for i in range(len(board))], player, opponent)

        return score

    def score_line(self, line, player, opponent):
        score = 0
        count_x = line.count('X')
        count_o = line.count('O')

        # Score for the player's markers
        score += self.score_consecutive(count_x, 'X', player)
        # Score for the opponent's markers (to block their wins)
        score += self.score_consecutive(count_o, 'O', opponent)

        return score

    def score_consecutive(self, count, marker, player):
        if marker == 'X':
            if count == 2:
                return 40  # Increased incentive for two in a row
            elif count == 3:
                return 400  # More significant reward for three in a row
            elif count >= 4:
                return 2000  # Winning move
        elif marker == 'O':
            if count == 2:
                return -50 if player == 'X' else 30  # Increased penalty for player 'X' and reward for player 'O'
            elif count == 3:
                return -500 if player == 'X' else 300  # Major penalty for player 'X' and incentive for player 'O'
            elif count >= 4:
                return -2000  # Losing move
        return 0

    def best_move(self, board, player):
        best_score = -float('inf')
        best_position = None

        for i in range(len(board)):
            for j in range(len(board)):
                if board[i][j] == ' ':
                    board[i][j] = player
                    score = self.evaluate(board, player)
                    board[i][j] = ' '

                    if score > best_score:
                        best_score = score
                        best_position = (i, j)

        return best_position
