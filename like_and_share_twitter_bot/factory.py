from .bot import Bot
from .twitter import Twitter


class Factory():
    def __init__(self, config):
        self.config = config

    def build(self):
        twitter = Twitter(
            self.config.get("consumer_key"),
            self.config.get("consumer_secret"),
            self.config.get("access_token_key"),
            self.config.get("access_token_secret"),
            self.config.get("language")
        )
        return Bot(
            twitter,
            self.config
        )
