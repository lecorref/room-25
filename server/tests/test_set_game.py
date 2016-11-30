"""Test game settings"""
import unittest
from src import Game, Mode, Tile

class TestSetGame(unittest.TestCase):
    def test_player_mode_error(self):
        self.assertRaises(ValueError, Game, 0, Mode.suspicion)
        self.assertRaises(ValueError, Game, 7, Mode.suspicion)
        self.assertRaises(ValueError, Game, 3, Mode.suspicion)
        self.assertRaises(ValueError, Game, 2, Mode.solo)
        self.assertRaises(ValueError, Game, 3, Mode.solo)
        self.assertRaises(ValueError, Game, 3, Mode.team)
        self.assertRaises(ValueError, Game, 7, Mode.team)
        self.assertRaises(ValueError, Game, 5, Mode.team)
        self.assertRaises(ValueError, Game, 4, Mode.competition)
        self.assertRaises(ValueError, Game, 1, Mode.competition)
        self.assertRaises(ValueError, Game, 1, Mode.cooperation)

    # a player is a person. a character is controlled by a player
    def test_set_turn_and_character_per_player(self):
        game1 = Game(6, Mode.suspicion)
        self.assertEqual(game1.turn, 10)
        self.assertEqual(game1.character, 1)

        game2 = Game(1, Mode.solo)
        self.assertEqual(game2.turn, 8)
        self.assertEqual(game2.character, 4)

        game3 = Game(4, Mode.team)
        self.assertEqual(game3.turn, 10)
        self.assertEqual(game3.character, 1)

        game4 = Game(3, Mode.competition)
        self.assertEqual(game4.turn, 10)
        self.assertEqual(game4.character, 2)

        game5 = Game(3, Mode.cooperation)
        self.assertEqual(game5.turn, 8)
        self.assertEqual(game5.character, 2)

        game6 = Game(5, Mode.cooperation)
        self.assertEqual(game6.character, 1)

    def test_board_setup(self):
        game = Game(6, Mode.suspicion)
        show = [["back", "back", "back", "back", "back"], \
                ["back", "back", "back", "back", "back"], \
                ["back", "back", "center", "back", "back"], \
                ["back", "back", "back", "back", "back"], \
                ["back", "back", "back", "back", "back"]]
        board = game.get_board()
        self.assertEqual(show, board.show())
        tile = board.get_tile(2, 3)
        self.assertRaises(IndexError, board.get_tile, 3, 6)
        self.assertRaises(IndexError, board.get_tile, 7, 4)
        self.assertIsInstance(tile, Tile)
        board.turn_all_tiles()
        self.assertTrue("exit" not in board[0][2] and board[1][1:3] \
            and board[2] and board[3][1:3]and board[4][2])


if __name__ == '__main__':
    unittest.main()

