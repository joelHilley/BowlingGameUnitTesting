import unittest
from Bowling import BowlingGame


class BowlingTests(unittest.TestCase):

    # Test for bowling a perfect game
    def test_perfect_game(self):
        """
        Throws: 12
        Pins per throw: 10
        Frames: 10
        :return: score = 300
        """
        game = BowlingGame()
        game.throw_many(12, 10)
        game.calculate_score()
        self.assertEqual(game.score, 300)


if __name__ == '__main__':
    unittest.main()