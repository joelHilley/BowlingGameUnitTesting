import unittest
from Bowling import BowlingGame


class TestBowling(unittest.TestCase):

    def setUp(self):
        self.game = BowlingGame()

    # Test final frame scoring by testing a perfect game bowled
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
    # test method throw_many(self, number_of_throws, pins)
    # Also tests using all three methods together
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

    # Test final frame strike
    def test_final_frame_strikes(self):
        """
        0 pins knocked over on first 18 throws
        3 strikes in final three rolls
        :return: score: 30
        """
        self.game.throw_many(18, 0)
        self.game.throw_one(10)
        self.game.throw_one(10)
        self.game.throw_one(10)
        self.game.calculate_score()
        self.assertEqual(self.game.score, 30)

        # Test scoring of 3 rolls in 10th frame
    def test_final_frame_spare(self):
        """
        0 pins knocked over on first 18 throws.
        Spare in final 2 rolls, and 5 pins knocked over
        in the corresponding third roll of the 10th frame
        :return: score: 15
        """
        self.game.throw_many(18, 0)
        self.game.throw_one(6)
        self.game.throw_one(4)
        self.game.throw_one(5)
        self.game.calculate_score()
        self.assertEqual(self.game.score, 15)

    # Test when a 1 is bowled on every throw
    def test_all_ones(self):
        """
        Throws: 20
        Pins per throw: 1
        :return: score: 20
        """
        self.game.throw_many(20, 1)
        self.game.calculate_score()
        self.assertEqual(self.game.score, 20)

# Test multiple calls of method, throw_many()
    def test_multiple_throw_many(self):
        """
        Throws: 21
        mixed group of throw_many arguements
        :return: score: 207
        """
        self.game.throw_many(3, 4)
        self.game.throw_many(5, 3)
        self.game.throw_many(12, 10)
        self.game.calculate_score()
        self.assertEqual(self.game.score, 207)


if __name__ == '__main__':
    unittest.main()
