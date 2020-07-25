from like_and_share_twitter_bot.factory import Factory
from like_and_share_twitter_bot.config import Config
import time
import os

if __name__ == "__main__":

    config = Config(os.environ)
    while True:
        bot = Factory(config).build()
        if bot.should_act():
            bot.run()
        del bot
        time.sleep(config.get("idle_period"))
