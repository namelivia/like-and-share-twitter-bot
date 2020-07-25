from unittest import TestCase
from like_and_share_twitter_bot.config import Config


class TestConfig(TestCase):

    def test_getting_a_configuration_values(self):
        source = {
            'IDLE_PERIOD': '3',
            'CONSUMER_KEY': 'consumerkey',
            'CONSUMER_SECRET': 'consumersecret',
            'ACCESS_TOKEN_KEY': 'accesstokenkey',
            'ACCESS_TOKEN_SECRET': 'accesstokensecret',
            'LANGUAGE': 'en',
            'CHANCE_TO_FAVORITE': '10',
            'CHANCE_TO_FOLLOW': '30',
            'CHANCE_TO_ACT': '20',
        }
        config = Config(source)
        self.assertEqual('consumerkey', config.get('consumer_key'))
        self.assertEqual(3, config.get('idle_period'))
        self.assertEqual(10, config.get('chance_to_favorite'))
        self.assertEqual(30, config.get('chance_to_follow'))
        self.assertEqual(20, config.get('chance_to_act'))
