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

    def test_runnig(self):
        #  TODO
        pass
