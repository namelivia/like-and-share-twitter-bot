#!/usr/bin/python3
import random
import twitter
import urllib.parse
import random
import os


class LikeAndShareTwitterBot:
    def main(self):
        api = twitter.Api(
            consumer_key=os.environ['CONSUMER_KEY']
            consumer_secret=os.environ['CONSUMER_SECRET']
            access_token_key=os.environ['ACCESS_TOKEN_KEY']
            access_token_secret=os.environ['ACCESS_TOKEN_SECRET']
        )
        terms = urllib.parse.quote_plus(os.environ['SEARCH_STRING'])
        query = "q={}&result_type=recent&lang={}&count=100".format(
            terms, os.environ['LANGUAGE']
        )
        results = api.GetSearch(raw_query=query)
        selected = random.choice(results)
        with open("/tmp/liked_tweets", "a") as myfile:
            myfile.write(selected.text)
        if random.randint(0, 100) < os.environ['CHANCE_TO_FAVORITE']:
            try:
                api.CreateFavorite(selected)
            except twitter.error.TwitterError as e:
                # Do nothing for now
                pass
        if random.randint(0, 100) < os.environ['CHANCE_TO_FOLLOW']:
            try:
                api.CreateFriendship(selected.user.id)
            except twitter.error.TwitterError as e:
                # Do nothing for now
                pass


if __name__ == "__main__":
    while True:
        if random.randint(0, 100) < os.environ['CHANCE_TO_ACT']:
            LikeAndShareTwitterBot().main()
        sleep(os.environ['IDLE_PERIOD'])
