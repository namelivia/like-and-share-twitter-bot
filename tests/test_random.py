from unittest import TestCase
from like_and_share_twitter_bot.random import Random


class TestRandom(TestCase):
    def test_getting_a_random_percentage(self):
        self.assertLessEqual(Random().get_percentage(), 100)
        self.assertGreaterEqual(Random().get_percentage(), 0)
