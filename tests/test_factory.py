from unittest import TestCase
from like_and_share_twitter_bot.factory import Factory
from like_and_share_twitter_bot.bot import Bot
import mock


class TestFactory(TestCase):

    @mock.patch('like_and_share_twitter_bot.factory.Twitter')
    def test_building_bot(
        self,
        m_twitter
    ):
        config = mock.Mock()
        config.get.return_value = 'config_value'
        factory = Factory(config)
        bot = factory.build()
        m_twitter.assert_called_once_with(
            'config_value',
            'config_value',
            'config_value',
            'config_value',
            'config_value'
        )
        self.assertIsInstance(bot, Bot)
