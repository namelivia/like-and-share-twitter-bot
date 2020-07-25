from unittest import TestCase
from like_and_share_twitter_bot.bot import Bot
import mock


class TestBot(TestCase):
    def setUp(self):
        self.twitter = mock.Mock()
        self.config = mock.Mock()
        self.bot = Bot(
            self.twitter,
            self.config
        )

    def test_runnig(self):
        #  TODO
        pass
