from unittest import TestCase
from like_and_share_twitter_bot.twitter import Twitter
import mock


class TestTwitter(TestCase):

    @mock.patch('like_and_share_twitter_bot.twitter.twitter.Api')
    def setUp(self, m_api_factory):
        self.twitter_api_mock = mock.Mock()
        m_api_factory.return_value = self.twitter_api_mock
        consumer_key = 'consumer_key'
        consumer_secret = 'consumer_secret'
        access_token_key = 'access_token_key'
        access_token_secret = 'access_token_secret'
        language = 'en'
        self.twitter = Twitter(
            consumer_key,
            consumer_secret,
            access_token_key,
            access_token_secret,
            language
        )
        m_api_factory.assert_called_once_with(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token_key,
            access_token_secret=access_token_secret
        )

    def test_get_tweet(self):
        terms = ['term1&term2']
        tweets = [mock.Mock(), mock.Mock()]
        self.twitter_api_mock.GetSearch.return_value = tweets
        self.twitter_api_mock.GetSearch.assert_called_once_with(
            "q=term1&term2&result_type=recent&lang=en&count=100"
        )
        self.assertIn(tweets, self.twitter.get_tweet(terms))

    def test_make_favorite(self):
        tweet = mock.Mock()
        self.assertIsNone(self.twitter.make_favorite(tweet))
        self.twitter_api_mock.CreateFavorite.assert_called_once_with(
            tweet
        )

    def test_follow_autor(self):
        tweet = mock.Mock()
        tweet.user = mock.Mock()
        tweet.user.id = 20
        self.assertIsNone(self.twitter.follow_author(tweet))
        self.twitter_api_mock.CreateFriendship.assert_called_once_with(
            20
        )
