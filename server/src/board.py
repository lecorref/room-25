"""
This module will contain all board-related class, methods, and functions
"""

import random

def __is_exit_tile(line, col):
    "return true if the line and col correspond to an exit tile"
    if (line == 2) or (col == 2) or (line, col) in [(1, 1), (3, 1), (1, 3), (3, 3)]:
        return False
    return True

class Board(object):
    """
    Class board
    attributes:
        - board (Tiles matrix)
    """

    def __init__(self):
        map_pool = ["empty" for _ in range(23)]
        random.shuffle(map_pool)
        exit_pool = ["exit"]
        while len(exit_pool) < 12:
            exit_pool.append(map_pool.pop())
        self.board = [[None for _ in range(5)] for _ in range(5)]
        for i in range(5):
            for j in range(5):
                if (i is 2) and (j is 2):
                    self.board[i][j] = Tile("center")
                elif __is_exit_tile(i, j):
                    self.board[i][j] = Tile("empty")
                else:
                    self.board[i][j] = Tile("empty")

    def show(self):
        "return the board as a string matrix"
        return [[tile.print_tile() for tile in line] for line in self.board]

    def get_tile(self, line, column):
        "return chosen tile"
        return self.board[line][column]

    def turn_all_tiles(self):
        "Turn the board tiles"
        [[tile.turn_tile() for tile in line] for line in self.board]

    def get_board(self):
        "Return the board attribute"
        return self.board


class Tile(object):
    """
    Class tile
    attributes:
        - name (string)
        - discovered (bool)
    """

    def __init__(self, name):
        self.name = name
        self.discovered = False if name is not "center" else True

    def print_tile(self):
        "return tile name if discovered"
        return self.name if self.discovered else "back"

    def turn_tile(self):
        "Set discovered is true"
        self.discovered = True

