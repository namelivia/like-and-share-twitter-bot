import random
import twitter
import urllib.parse


class Bot:
    def __init__(self, twitter, config):
        self.twitter = twitter
        self.config = config

    def should_act(self):
        return random.randint(0, 100) < self.config.get('chance_to_act')

    def _should_favorite(self):
        return random.randint(0, 100) < self.config.get('chance_to_favorite')

    def _should_follow(self):
        return random.randint(0, 100) < self.config.get('chance_to_follow')

    def run(self):
        terms = urllib.parse.quote_plus(self.config.get('search_string'))
        tweet = twitter.get_tweet(terms)
        if self._should_favorite():
            self.twitter.make_favorite(tweet)
        if self._should_follow():
            self.twitter.follow_author(tweet)
