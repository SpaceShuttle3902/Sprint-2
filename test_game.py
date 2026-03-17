import unittest
from game_logic import PegSolitaireGame


class TestPegSolitaireGame(unittest.TestCase):

    # Test 1: Board initialization
    def test_board_initialization(self):
        game = PegSolitaireGame(size=7)

        center = game.size // 2

        # The center hole should be empty
        self.assertEqual(game.board[center][center], 0)

        # All other positions should contain pegs
        peg_count = sum(sum(row) for row in game.board)
        self.assertEqual(peg_count, game.size * game.size - 1)


    # Test 2: Valid move
    def test_valid_move(self):
        game = PegSolitaireGame(size=7)

        center = game.size // 2

        # Move peg from two spaces left of center into the center hole
        r1, c1 = center, center - 2
        r2, c2 = center, center

        result = game.make_move(r1, c1, r2, c2)

        # Move should be valid
        self.assertTrue(result)

        # Starting position should now be empty
        self.assertEqual(game.board[r1][c1], 0)

        # Peg that was jumped over should be removed
        self.assertEqual(game.board[center][center - 1], 0)

        # Destination should now contain a peg
        self.assertEqual(game.board[r2][c2], 1)


    # Test 3: Game over detection
    def test_game_over(self):
        game = PegSolitaireGame(size=7)

        # Create a board with only one peg left
        game.board = [[0]*game.size for _ in range(game.size)]
        game.board[3][3] = 1

        # With only one peg, there should be no valid moves
        self.assertTrue(game.is_game_over())


if __name__ == "__main__":
    unittest.main()