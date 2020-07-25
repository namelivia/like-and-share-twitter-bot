from unittest import TestCase
from like_and_share_twitter_bot.bot import Bot
import mock


class TestBot(TestCase):
    def setUp(self):
        self.twitter = mock.Mock()
        self.config = mock.Mock()
        self.random = mock.Mock()
        self.bot = Bot(
            self.twitter,
            self.config,
            self.random
        )

    def test_runnig(self):
        #  TODO
        pass
