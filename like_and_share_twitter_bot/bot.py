import twitter
import urllib.parse


class Bot:
    def __init__(self, twitter, config, random):
        self.twitter = twitter
        self.config = config
        self.random = random

    def should_act(self):
        return self.random.get_percentage() < self.config.get('chance_to_act')

    def _should_favorite(self):
        return self.random.get_percentage() < self.config.get(
            'chance_to_favorite'
        )

    def _should_follow(self):
        return self.random.get_percentage() < self.config.get(
            'chance_to_follow'
        )

    def run(self):
        terms = urllib.parse.quote_plus(self.config.get('search_string'))
        tweet = twitter.get_tweet(terms)
        if self._should_favorite():
            self.twitter.make_favorite(tweet)
        if self._should_follow():
            self.twitter.follow_author(tweet)
