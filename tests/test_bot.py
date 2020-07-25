from unittest import TestCase
from like_and_share_twitter_bot.bot import Bot
import mock


class TestBot(TestCase):
    def setUp(self):
        self.twitter = mock.Mock()
        self.config = mock.Mock()
        self.random = mock.Mock()
        self.chance_to_act = 20
        self.chance_to_follow = 20
        self.chance_to_favorite = 20
        self.search_string = 'search_string'
        self.bot = Bot(
            self.twitter,
            self.chance_to_act,
            self.chance_to_favorite,
            self.chance_to_follow,
            self.search_string,
            self.random
        )

    def test_should_act(self):
        # The random number is higher than the chance to act, do nothing
        self.random.get_percentage.return_value = 30
        self.assertFalse(self.bot.should_act())

        # The random number is lower than the chance to act, do something
        self.random.get_percentage.return_value = 10
        self.assertTrue(self.bot.should_act())

    def test_run_doing_everything(self):
        self.random.get_percentage.return_value = 10
        tweet = mock.Mock()
        self.twitter.get_tweet.return_value = tweet
        self.assertIsNone(self.bot.run())
        self.twitter.make_favorite.assert_called_once_with(tweet)
        self.twitter.follow_author.assert_called_once_with(tweet)

    def test_run_doing_nothing(self):
        self.random.get_percentage.return_value = 30
        tweet = mock.Mock()
        self.twitter.get_tweet.return_value = tweet
        self.assertIsNone(self.bot.run())
