#!/usr/bin/env python
# coding: utf-8

# **Team Members**
# 
# 
# *   Hamdan Sethi (SP23-BAI-015)
# *   Zeeshan Aftab (SP23-BAI-053)
# *   Muhammad Laraib Afridi (SP23-BAI-34)
# 
# 
# 
# 
# 

# In[ ]:





# In[ ]:





# ### **Game Problem: Othello**

# **Introduction:**
# Othello, also known as Reversi, is a classic 2-player board game played on an 8x8 grid. The game is designed around flipping opponent's pieces to gain control of the board.
# 
# **Game Rules:**
# 
# 1. **Goal:**
#    The goal of Othello is to have the majority of your colored discs showing at the end of the game. This is usually defined by having more of your color discs on the board than your opponent's color.
# 
# 2. **Starting Position:**
#    At the beginning of the game, four discs are placed in the center of the board in a square configuration, with two discs of each color diagonally adjacent.
# 
# 3. **Your Turn:**
#    On your turn, you place one of your discs on an empty square. You must place the disc so that it surrounds at least one of your opponent's discs in a straight line (horizontally, vertically, or diagonally). This results in the opponent's discs being flipped to your color. If you cannot make a legal move, you forfeit your turn.
# 
# 4. **Flipping Discs:**
#    When you place a disc, any of your opponent's discs that are sandwiched between the newly placed disc and any of your discs already on the board are flipped to your color.
# 
# 5. **Opponent's Turn:**
#    After you place your disc and flip any necessary discs, it becomes your opponent's turn to place their disc on the board.
# 
# 6. **Game End:**
#    The game ends when either:
#    - One player cannot make a legal move. In this case, the other player continues to place discs until the board is filled or both players cannot make a move.
#    - The board is filled with discs. In this case, the player with the majority of their color discs on the board wins.
# 
# **Strategies:**
#    - Corners are key positions in the game. Controlling corners can give you a significant advantage.
#    - Maintaining control over edges can also be beneficial as they are harder to flip.
#    - Strive to create opportunities for gaining control over large portions of the board by flipping multiple discs in a single move.
# 
# **Conclusion:**
# Othello is a game of strategy and foresight. By carefully planning your moves and anticipating your opponent's responses, you can gain control of the board and secure victory.

# ### **MONTE CARLO SEARCH TREE (MCTS):**

# **Algorithm Explanation:**
# MCTS is a search algorithm that explores possible states (board configurations) reachable by following the game's rules. Unlike brute force approaches, MCTS focuses on exploring more promising nodes first, reducing the search space significantly.
# 
# **Aim of MCTS:**
# The goal of implementing MCTS in Othello is to leverage its capabilities to determine the best move within a given time frame. By allowing the program to "think" ahead for a move, MCTS aims to improve decision-making.
# 
# **Description of MCTS Components:**
# 
# 1. **Selection:**
#    - Starting from the initial board, the algorithm searches one layer deeper, selecting nodes with higher UCT (Upper Confidence Bound for Trees) values.
#    - If a node's children haven't been explored, an unexplored child is selected based on a policy (e.g., selecting the leftmost unexplored child).
# 
# 2. **Expansion:**
#    - After selecting a node, if all other nodes in the same layer have been explored, the algorithm generates its children nodes, expanding the tree.
#    - If the node is terminal, the algorithm selects the next node for expansion.
# 
# 3. **Simulation:**
#    - From the selected node, the algorithm runs a simulated game where moves are played randomly until reaching a terminal node.
#    - The outcome of the simulation (win, tie, or lose) is recorded.
# 
# 4. **Backpropagation:**
#    - Starting from the terminal node reached in the simulation, the algorithm updates the number of visits and scores obtained.
#    - The process recursively backtracks to the parent node until reaching the root node.
# 
# When the given time expires, the algorithm returns the move that leads to the child of the root node with the highest number of visits, indicating its higher probability of leading to winning states during simulations.
# 
# Applying MCTS to Othello involves representing the game state, defining legal moves, simulating games, and evaluating board positions. The algorithm iteratively refines its understanding of which moves are more promising based on simulation results, ultimately guiding the AI to make better-informed decisions.
# 
# By implementing MCTS in Othello, the AI can make strategic moves based on a deeper exploration of possible game states, leading to a more challenging and engaging gameplay experience.

# ### **Alpha-Beta Pruning for Othello: A Simple**

# #### What's Alpha-Beta Pruning?
# Alpha-Beta Pruning is a smart way to make the computer decide where to place its Othello pieces. It helps the computer skip checking some moves that won't help it win, making it faster and smarter.
# 
# #### Steps to Make It Work for Othello
# 
# 1. *Game Setup*
#     - Set up the board with its dimensions and piece types.
#     
# 2. *Place a Piece*
#     - Create a function to place a piece on the board at a specific spot.
# 
# 3. *Check Available Spots*
#     - Make sure a spot is free to place a piece.
# 
# 4. *Find the Next Spot*
#     - Look for the next available spot in a column to place a piece.
# 
# 5. *Show the Board*
#     - Print out the board, but flip it so it looks right-side-up.
# 
# 6. *Check for a Winning Move*
#     - Check if someone has won by connecting their pieces.
# 
# 7. *Evaluate the Board*
#     - Decide how good the board looks for winning, from the computer's perspective.
# 
# 8. *Check the Game's End*
#     - See if the game has ended because someone won or there are no more moves left.
# 
# 9. *Minimax Algorithm*
#     - This is where the computer thinks ahead, trying to find the best move by imagining possible future moves.
#     
# 10. *Find Valid Spots*
#     - See where the computer can place its piece.
# 
# 11. *Pick the Best Move*
#     - Choose the best spot to place the piece based on how likely it is to win.
# 
# 12. *Main Game Loop*
#     - Start the game, let players and the computer take turns, and see who wins or if it's a tie.
# 
# This setup lets you play Othello against the computer, and the computer uses Alpha-Beta Pruning to decide its moves.

# ### **Comparative Analysis: MCTS vs. Alpha-Beta Pruning in Othello**

# #### Efficiency
# 
# *MCTS:*
# - MCTS builds and explores a game tree by running random simulations from each possible move. The number of simulations and tree depth affect its efficiency.
# - While MCTS can be computationally expensive, you can control its complexity by setting a limit on the number of simulations.
# - Initially, MCTS explores many nodes, but it narrows down as it runs more simulations.
# 
# *Alpha-Beta Pruning:*
# - Alpha-Beta Pruning is a methodical approach to game tree exploration, pruning off less promising paths.
# - Unlike MCTS, it explores the tree systematically, setting bounds (alpha and beta) on possible node values.
# - By eliminating inferior moves early, Alpha-Beta Pruning greatly reduces the number of nodes visited compared to basic minimax.
# 
# #### Accuracy
# 
# *MCTS:*
# - MCTS decides moves based on random simulations. Its accuracy depends on the quality and quantity of these simulations.
# - With enough simulations, MCTS can make strong decisions, especially in complex games where balancing exploration and exploitation is crucial.
# - However, its accuracy can suffer with inadequate simulations or overly complex game dynamics.
# 
# *Alpha-Beta Pruning:*
# - In deterministic games like Othello, Alpha-Beta Pruning ensures finding the best move by fully exploring the game tree.
# - Accuracy in Alpha-Beta Pruning relies on a good evaluation function and search depth. Deeper searches with better heuristics make for more accurate decisions.
# - In practice, Alpha-Beta Pruning often makes highly accurate moves in games like Othello due to its exhaustive search.
# 
# #### Conclusion
# 
# - *Efficiency:* Alpha-Beta Pruning generally outperforms MCTS in efficiency, especially in games with smaller search spaces like Othello. MCTS, however, shines in scalability, making it suitable for more complex games.
#   
# - *Accuracy:* Alpha-Beta Pruning tends to be more precise than MCTS, promising the best move when fully explored. MCTS, on the other hand, can be resilient in complex, uncertain environments, making good choices by balancing exploration and exploitation.
# 
# - *Choice:* Your pick between MCTS and Alpha-Beta Pruning should consider game complexity, available computing power, and the trade-off between efficiency and accuracy. For Othello, where the search space is manageable, Alpha-Beta Pruning's accuracy might be preferable, while MCTS could be better for more sprawling games where exhaustive search isn't possible.

# # **Human VS AI (Alpha Beta Pruning)**

# In[ ]:


import random
import math

class Othello:
    def __init__(self):
        self.board = [[' ' for _ in range(5)] for _ in range(5)]
        self.board[2][2] = 'X'
        self.board[2][3] = 'O'
        self.board[3][2] = 'O'
        self.board[3][3] = 'X'
        self.current_player = 'X'

    def print_board(self):
        print('  0 1 2 3 4')
        print(' ---------')
        for i in range(5):
            print(i, '|'.join(self.board[i]))

    def is_valid_move(self, row, col):
        if row < 0 or row >= 5 or col < 0 or col >= 5 or self.board[row][col] != ' ':
            return False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] != self.current_player:
                while 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] != ' ':
                    r += dr
                    c += dc
                    if 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] == self.current_player:
                        return True
        return False

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] != ' ' and self.board[r][c] != self.current_player:
                    r += dr
                    c += dc
                    if 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] == self.current_player:
                        r -= dr
                        c -= dc
                        while r != row or c != col:
                            self.board[r][c] = self.current_player
                            r -= dr
                            c -= dc
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move!")

    def get_valid_moves(self):
        valid_moves = []
        for row in range(5):
            for col in range(5):
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def is_game_over(self):
        return len(self.get_valid_moves()) == 0

    def get_winner(self):
        x_count = sum(row.count('X') for row in self.board)
        o_count = sum(row.count('O') for row in self.board)
        if x_count > o_count:
            return 'X'
        elif o_count > x_count:
            return 'O'
        else:
            return 'Draw'

class Node:
    def __init__(self, game, parent=None):
        self.game = game
        self.parent = parent
        self.children = []
        self.visits = 0
        self.score = 0

    def expand(self):
        if self.game.is_game_over():
            return

        for row in range(5):
            for col in range(5):
                if self.game.is_valid_move(row, col):
                    new_game = self.game.__class__()
                    new_game.board = [row[:] for row in self.game.board]
                    new_game.current_player = self.game.current_player
                    new_game.make_move(row, col)
                    self.children.append(Node(new_game, parent=self))

    def select_child(self):
        C = 1.41
        return max(self.children, key=lambda c: c.score / c.visits + C * math.sqrt(2 * math.log(self.visits) / c.visits) if c.visits > 0 else float('inf'))

    def backpropagate(self, score):
        self.visits += 1
        self.score += score
        if self.parent:
            self.parent.backpropagate(score)

def mcts_search(game, iterations=10000):
    root = Node(game)
    for _ in range(iterations):
        node = root
        while not node.game.is_game_over():
            if not node.children:
                node.expand()
            if node.children:
                node = node.select_child()
        score = node.game.get_winner() == 'X'
        node.backpropagate(score)
    return max(root.children, key=lambda c: c.visits).game

def alpha_beta_search(game, depth, alpha=-float('inf'), beta=float('inf')):
    if depth == 0 or game.is_game_over():
        x_count = sum(row.count('X') for row in game.board)
        o_count = sum(row.count('O') for row in game.board)
        return x_count - o_count

    if game.current_player == 'X':
        max_eval = -float('inf')
        for row in range(5):
            for col in range(5):
                if game.is_valid_move(row, col):
                    new_game = game.__class__()
                    new_game.board = [row[:] for row in game.board]
                    new_game.current_player = game.current_player
                    new_game.make_move(row, col)
                    eval = alpha_beta_search(new_game, depth - 1, alpha, beta)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(5):
            for col in range(5):
                if game.is_valid_move(row, col):
                    new_game = game.__class__()
                    new_game.board = [row[:] for row in game.board]
                    new_game.current_player = game.current_player
                    new_game.make_move(row, col)
                    eval = alpha_beta_search(new_game, depth - 1, alpha, beta)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def get_best_move(game, depth):
    best_score = -float('inf')
    best_move = None
    for row in range(5):
        for col in range(5):
            if game.is_valid_move(row, col):
                new_game = game.__class__()
                new_game.board = [row[:] for row in game.board]
                new_game.current_player = game.current_player
                new_game.make_move(row, col)
                score = alpha_beta_search(new_game, depth)
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

if __name__ == "__main__":
    game = Othello()
    mode = input("Choose mode (1: Human vs AI (Alpha-Beta), 2: Human vs AI (Monte Carlo), 3: AI (Alpha-Beta) vs AI (Monte Carlo)): ")

    if mode == '1':
        while not game.is_game_over():
            game.print_board()
            if game.current_player == 'X':
                valid_move = False
                while not valid_move:
                    try:
                        row = int(input("Enter row: "))
                        col = int(input("Enter col: "))
                        if 0 <= row < 5 and 0 <= col < 5:
                            valid_move = True
                        else:
                            print("Invalid row or column. Please enter a number between 0 and 4.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                game.make_move(row, col)
            else:
                best_move = get_best_move(game, depth=3)
                game.make_move(best_move[0], best_move[1])

    elif mode == '2':
        while not game.is_game_over():
            game.print_board()
            if game.current_player == 'X':
                game = mcts_search(game)
            else:
                valid_move = False
                while not valid_move:
                    try:
                        row = int(input("Enter row: "))
                        col = int(input("Enter col: "))
                        if 0 <= row < 5 and 0 <= col < 5:
                            valid_move = True
                        else:
                            print("Invalid row or column. Please enter a number between 0 and 4.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                game.make_move(row, col)

    elif mode == '3':
        while not game.is_game_over():
            game.print_board()
            if game.current_player == 'X':
                game = mcts_search(game)
            else:
                best_move = get_best_move(game, depth=3)
                game.make_move(best_move[0], best_move[1])

    else:
        print("Invalid mode selected. Please choose 1, 2, or 3.")
        exit(1)

    print("Game Over!")
    winner = game.get_winner()
    if winner == 'Draw':
        print("It's a draw!")
    else:
        print(f"{winner} wins!")


# # **Human vs AI (Monte Carlo (X) )**

# In[ ]:


import random
import math

class Othello:
    def __init__(self):
        self.board = [[' ' for _ in range(5)] for _ in range(5)]
        self.board[2][2] = 'X'
        self.board[2][3] = 'O'
        self.board[3][2] = 'O'
        self.board[3][3] = 'X'
        self.current_player = 'X'

    def print_board(self):
        print('  0 1 2 3 4')
        print(' ---------')
        for i in range(5):
            print(i, '|'.join(self.board[i]))

    def is_valid_move(self, row, col):
        if row < 0 or row >= 5 or col < 0 or col >= 5 or self.board[row][col] != ' ':
            return False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] != self.current_player:
                while 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] != ' ':
                    r += dr
                    c += dc
                    if 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] == self.current_player:
                        return True
        return False

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] != ' ' and self.board[r][c] != self.current_player:
                    r += dr
                    c += dc
                    if 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] == self.current_player:
                        r -= dr
                        c -= dc
                        while r != row or c != col:
                            self.board[r][c] = self.current_player
                            r -= dr
                            c -= dc
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move!")

    def get_valid_moves(self):
        valid_moves = []
        for row in range(5):
            for col in range(5):
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def is_game_over(self):
        return len(self.get_valid_moves()) == 0

    def get_winner(self):
        x_count = sum(row.count('X') for row in self.board)
        o_count = sum(row.count('O') for row in self.board)
        if x_count > o_count:
            return 'X'
        elif o_count > x_count:
            return 'O'
        else:
            return 'Draw'

class Node:
    def __init__(self, game, parent=None):
        self.game = game
        self.parent = parent
        self.children = []
        self.visits = 0
        self.score = 0

    def expand(self):
        if self.game.is_game_over():
            return

        for row in range(5):
            for col in range(5):
                if self.game.is_valid_move(row, col):
                    new_game = self.game.__class__()
                    new_game.board = [row[:] for row in self.game.board]
                    new_game.current_player = self.game.current_player
                    new_game.make_move(row, col)
                    self.children.append(Node(new_game, parent=self))

    def select_child(self):
        C = 1.41
        return max(self.children, key=lambda c: c.score / c.visits + C * math.sqrt(2 * math.log(self.visits) / c.visits) if c.visits > 0 else float('inf'))

    def backpropagate(self, score):
        self.visits += 1
        self.score += score
        if self.parent:
            self.parent.backpropagate(score)

def mcts_search(game, iterations=10000):
    root = Node(game)
    for _ in range(iterations):
        node = root
        while not node.game.is_game_over():
            if not node.children:
                node.expand()
            if node.children:
                node = node.select_child()
        score = node.game.get_winner() == 'X'
        node.backpropagate(score)
    return max(root.children, key=lambda c: c.visits).game

def alpha_beta_search(game, depth, alpha=-float('inf'), beta=float('inf')):
    if depth == 0 or game.is_game_over():
        x_count = sum(row.count('X') for row in game.board)
        o_count = sum(row.count('O') for row in game.board)
        return x_count - o_count

    if game.current_player == 'X':
        max_eval = -float('inf')
        for row in range(5):
            for col in range(5):
                if game.is_valid_move(row, col):
                    new_game = game.__class__()
                    new_game.board = [row[:] for row in game.board]
                    new_game.current_player = game.current_player
                    new_game.make_move(row, col)
                    eval = alpha_beta_search(new_game, depth - 1, alpha, beta)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(5):
            for col in range(5):
                if game.is_valid_move(row, col):
                    new_game = game.__class__()
                    new_game.board = [row[:] for row in game.board]
                    new_game.current_player = game.current_player
                    new_game.make_move(row, col)
                    eval = alpha_beta_search(new_game, depth - 1, alpha, beta)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def get_best_move(game, depth):
    best_score = -float('inf')
    best_move = None
    for row in range(5):
        for col in range(5):
            if game.is_valid_move(row, col):
                new_game = game.__class__()
                new_game.board = [row[:] for row in game.board]
                new_game.current_player = game.current_player
                new_game.make_move(row, col)
                score = alpha_beta_search(new_game, depth)
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

if __name__ == "__main__":
    game = Othello()
    mode = input("Choose mode (1: Human vs AI (Alpha-Beta), 2: Human vs AI (Monte Carlo), 3: AI (Alpha-Beta) vs AI (Monte Carlo)): ")

    if mode == '1':
        while not game.is_game_over():
            game.print_board()
            if game.current_player == 'X':
                valid_move = False
                while not valid_move:
                    try:
                        row = int(input("Enter row: "))
                        col = int(input("Enter col: "))
                        if 0 <= row < 5 and 0 <= col < 5:
                            valid_move = True
                        else:
                            print("Invalid row or column. Please enter a number between 0 and 4.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                game.make_move(row, col)
            else:
                best_move = get_best_move(game, depth=3)
                game.make_move(best_move[0], best_move[1])

    elif mode == '2':
        while not game.is_game_over():
            game.print_board()
            if game.current_player == 'X':
                game = mcts_search(game)
            else:
                valid_move = False
                while not valid_move:
                    try:
                        row = int(input("Enter row: "))
                        col = int(input("Enter col: "))
                        if 0 <= row < 5 and 0 <= col < 5:
                            valid_move = True
                        else:
                            print("Invalid row or column. Please enter a number between 0 and 4.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                game.make_move(row, col)

    elif mode == '3':
        while not game.is_game_over():
            game.print_board()
            if game.current_player == 'X':
                game = mcts_search(game)
            else:
                best_move = get_best_move(game, depth=3)
                game.make_move(best_move[0], best_move[1])

    else:
        print("Invalid mode selected. Please choose 1, 2, or 3.")
        exit(1)

    print("Game Over!")
    winner = game.get_winner()
    if winner == 'Draw':
        print("It's a draw!")
    else:
        print(f"{winner} wins!")


# # **AI (Monte Carlo (X) ) vs AI (Alpha Beta (O) )**

# In[ ]:


import random
import math

class Othello:
    def __init__(self):
        self.board = [[' ' for _ in range(5)] for _ in range(5)]
        self.board[2][2] = 'X'
        self.board[2][3] = 'O'
        self.board[3][2] = 'O'
        self.board[3][3] = 'X'
        self.current_player = 'X'

    def print_board(self):
        print('  0 1 2 3 4')
        print(' ---------')
        for i in range(5):
            print(i, '|'.join(self.board[i]))

    def is_valid_move(self, row, col):
        if row < 0 or row >= 5 or col < 0 or col >= 5 or self.board[row][col] != ' ':
            return False
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
        for dr, dc in directions:
            r, c = row + dr, col + dc
            if 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] != self.current_player:
                while 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] != ' ':
                    r += dr
                    c += dc
                    if 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] == self.current_player:
                        return True
        return False

    def make_move(self, row, col):
        if self.is_valid_move(row, col):
            self.board[row][col] = self.current_player
            directions = [(1, 0), (-1, 0), (0, 1), (0, -1), (1, 1), (-1, -1), (1, -1), (-1, 1)]
            for dr, dc in directions:
                r, c = row + dr, col + dc
                while 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] != ' ' and self.board[r][c] != self.current_player:
                    r += dr
                    c += dc
                    if 0 <= r < 5 and 0 <= c < 5 and self.board[r][c] == self.current_player:
                        r -= dr
                        c -= dc
                        while r != row or c != col:
                            self.board[r][c] = self.current_player
                            r -= dr
                            c -= dc
            self.current_player = 'O' if self.current_player == 'X' else 'X'
        else:
            print("Invalid move!")

    def get_valid_moves(self):
        valid_moves = []
        for row in range(5):
            for col in range(5):
                if self.is_valid_move(row, col):
                    valid_moves.append((row, col))
        return valid_moves

    def is_game_over(self):
        return len(self.get_valid_moves()) == 0

    def get_winner(self):
        x_count = sum(row.count('X') for row in self.board)
        o_count = sum(row.count('O') for row in self.board)
        if x_count > o_count:
            return 'X'
        elif o_count > x_count:
            return 'O'
        else:
            return 'Draw'

class Node:
    def __init__(self, game, parent=None):
        self.game = game
        self.parent = parent
        self.children = []
        self.visits = 0
        self.score = 0

    def expand(self):
        if self.game.is_game_over():
            return

        for row in range(5):
            for col in range(5):
                if self.game.is_valid_move(row, col):
                    new_game = self.game.__class__()
                    new_game.board = [row[:] for row in self.game.board]
                    new_game.current_player = self.game.current_player
                    new_game.make_move(row, col)
                    self.children.append(Node(new_game, parent=self))

    def select_child(self):
        C = 1.41
        return max(self.children, key=lambda c: c.score / c.visits + C * math.sqrt(2 * math.log(self.visits) / c.visits) if c.visits > 0 else float('inf'))

    def backpropagate(self, score):
        self.visits += 1
        self.score += score
        if self.parent:
            self.parent.backpropagate(score)

def mcts_search(game, iterations=10000):
    root = Node(game)
    for _ in range(iterations):
        node = root
        while not node.game.is_game_over():
            if not node.children:
                node.expand()
            if node.children:
                node = node.select_child()
        score = node.game.get_winner() == 'X'
        node.backpropagate(score)
    return max(root.children, key=lambda c: c.visits).game

def alpha_beta_search(game, depth, alpha=-float('inf'), beta=float('inf')):
    if depth == 0 or game.is_game_over():
        x_count = sum(row.count('X') for row in game.board)
        o_count = sum(row.count('O') for row in game.board)
        return x_count - o_count

    if game.current_player == 'X':
        max_eval = -float('inf')
        for row in range(5):
            for col in range(5):
                if game.is_valid_move(row, col):
                    new_game = game.__class__()
                    new_game.board = [row[:] for row in game.board]
                    new_game.current_player = game.current_player
                    new_game.make_move(row, col)
                    eval = alpha_beta_search(new_game, depth - 1, alpha, beta)
                    max_eval = max(max_eval, eval)
                    alpha = max(alpha, eval)
                    if beta <= alpha:
                        break
        return max_eval
    else:
        min_eval = float('inf')
        for row in range(5):
            for col in range(5):
                if game.is_valid_move(row, col):
                    new_game = game.__class__()
                    new_game.board = [row[:] for row in game.board]
                    new_game.current_player = game.current_player
                    new_game.make_move(row, col)
                    eval = alpha_beta_search(new_game, depth - 1, alpha, beta)
                    min_eval = min(min_eval, eval)
                    beta = min(beta, eval)
                    if beta <= alpha:
                        break
        return min_eval


def get_best_move(game, depth):
    best_score = -float('inf')
    best_move = None
    for row in range(5):
        for col in range(5):
            if game.is_valid_move(row, col):
                new_game = game.__class__()
                new_game.board = [row[:] for row in game.board]
                new_game.current_player = game.current_player
                new_game.make_move(row, col)
                score = alpha_beta_search(new_game, depth)
                if score > best_score:
                    best_score = score
                    best_move = (row, col)
    return best_move

if __name__ == "__main__":
    game = Othello()
    mode = input("Choose mode (1: Human vs AI (Alpha-Beta), 2: Human vs AI (Monte Carlo), 3: AI (Alpha-Beta) vs AI (Monte Carlo)): ")

    if mode == '1':
        while not game.is_game_over():
            game.print_board()
            if game.current_player == 'X':
                valid_move = False
                while not valid_move:
                    try:
                        row = int(input("Enter row: "))
                        col = int(input("Enter col: "))
                        if 0 <= row < 5 and 0 <= col < 5:
                            valid_move = True
                        else:
                            print("Invalid row or column. Please enter a number between 0 and 4.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                game.make_move(row, col)
            else:
                best_move = get_best_move(game, depth=3)
                game.make_move(best_move[0], best_move[1])

    elif mode == '2':
        while not game.is_game_over():
            game.print_board()
            if game.current_player == 'X':
                game = mcts_search(game)
            else:
                valid_move = False
                while not valid_move:
                    try:
                        row = int(input("Enter row: "))
                        col = int(input("Enter col: "))
                        if 0 <= row < 5 and 0 <= col < 5:
                            valid_move = True
                        else:
                            print("Invalid row or column. Please enter a number between 0 and 4.")
                    except ValueError:
                        print("Invalid input. Please enter a number.")
                game.make_move(row, col)

    elif mode == '3':
        while not game.is_game_over():
            game.print_board()
            if game.current_player == 'X':
                game = mcts_search(game)
            else:
                best_move = get_best_move(game, depth=3)
                game.make_move(best_move[0], best_move[1])

    else:
        print("Invalid mode selected. Please choose 1, 2, or 3.")
        exit(1)

    print("Game Over!")
    winner = game.get_winner()
    if winner == 'Draw':
        print("It's a draw!")
    else:
        print(f"{winner} wins!")

