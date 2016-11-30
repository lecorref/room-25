"""
This module will contain the game 'room 25' setup and run classes
"""
from enum import Enum
from .board import Board

class Mode(Enum):
    """Game modes"""
    suspicion = 1
    solo = 2
    team = 3
    competition = 4
    cooperation = 5

class Game(object):
    """Class that will run the game
    attributes:
        - turns
        - character
        - board
    """

    dictionnary = {
        Mode.suspicion: (4, 5, 6),
        Mode.solo: tuple([1]),
        Mode.team: (4, 6),
        Mode.competition: (2, 3),
        Mode.cooperation: (2, 3, 4, 5, 6)
        }

    def __init__(self, players, chosen_mode):
        if players not in Game.dictionnary.get(chosen_mode, tuple()):
            raise ValueError('Mode cannot be played with this number \
                    of players')
        self.turn = 8 if chosen_mode in (Mode.solo, Mode.cooperation) else 10
        if players < 4:
            self.character = 4 if chosen_mode is Mode.solo else 2
        else:
            self.character = 1
        self.board = Board()


    def get_board(self):
        """ Return board state """
        return self.board
