import urllib.parse


class Bot:
    def __init__(
        self,
        twitter,
        chance_to_act,
        chance_to_follow,
        chance_to_favorite,
        search_string,
        random,
    ):
        self.twitter = twitter
        self.chance_to_act = chance_to_act
        self.chance_to_favorite = chance_to_favorite
        self.chance_to_follow = chance_to_follow
        self.search_string = search_string
        self.random = random

    def should_act(self):
        return self.random.get_percentage() < self.chance_to_act

    def _should_favorite(self):
        return self.random.get_percentage() < self.chance_to_favorite

    def _should_follow(self):
        return self.random.get_percentage() < self.chance_to_follow

    def run(self):
        terms = urllib.parse.quote_plus(self.search_string)
        tweet = self.twitter.get_tweet(terms)
        if self._should_favorite():
            self.twitter.make_favorite(tweet)
        if self._should_follow():
            self.twitter.follow_author(tweet)
