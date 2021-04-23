import unittest
from Bowling import BowlingGame


class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    # Test for bowling a perfect game
    def test_perfect_game(self):
        """
        Throws: 12
        Pins per throw: 10
        Frames: 10
        :return: score = 300
        """
        self.game.throw_many(12, 10)
        self.game.calculate_score()
        self.assertEqual(self.game.score, 300)

    # test method throw_one(self,pins)
    def test_throw_one(self):
        """
        Throws: 20
        One throw knocking down 7 pins
        19 throws knocking down 0 pins each throw
        Frames: 10
        :return:score = 8
        """
        self.game.throw_one(7)
        self.game.throw_many(19, 0)
        self.game.calculate_score()
        self.assertEqual(self.game.score, 7)

    # Test all gutter balls
    def test_all_gutters(self):
        """
        Throws: 20
        Pins per throw: 0
        :return:score = 0
        """
        self.game.throw_many(20, 0)
        self.game.calculate_score()
        self.assertEqual(self.game.score, 0)


# runs unit test
if __name__ == '__main__':
    unittest.main()
# end