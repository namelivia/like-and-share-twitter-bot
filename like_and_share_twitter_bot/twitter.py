import twitter
import random


class Twitter:
    def __init__(
        self,
        consumer_key,
        consumer_secret,
        access_token_key,
        access_token_secret,
        language,
    ):
        self.api = twitter.Api(
            consumer_key=consumer_key,
            consumer_secret=consumer_secret,
            access_token_key=access_token_key,
            access_token_secret=access_token_secret,
        )
        self.language = language

    def get_tweet(self, terms):
        query = "q={}&result_type=recent&lang={}&count=100".format(terms, self.language)
        results = self.api.GetSearch(raw_query=query)
        return random.choice(results)

    def make_favorite(self, tweet):
        try:
            self.api.CreateFavorite(tweet)
        except twitter.error.TwitterError:
            # Do nothing for now
            pass

    def follow_author(self, tweet):
        try:
            self.api.CreateFriendship(tweet.user.id)
        except twitter.error.TwitterError:
            # Do nothing for now
            pass
