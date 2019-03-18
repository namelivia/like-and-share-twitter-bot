#!/usr/bin/python3
import random
import twitter
import config
import urllib.parse
import random

class LikeAndShareTwitterBot:

    def main(self):
        api = twitter.Api(
            consumer_key=config.GENERAL_CONFIG['consumerKey'],
            consumer_secret=config.GENERAL_CONFIG['consumerSecret'],
            access_token_key=config.GENERAL_CONFIG['accessTokenKey'],
            access_token_secret=config.GENERAL_CONFIG['accessTokenSecret'],
        )
        terms = urllib.parse.quote_plus(config.GENERAL_CONFIG['searchString'])
        query = "q={}&result_type=recent&lang={}&count=100".format(terms, config.GENERAL_CONFIG['language'])
        results = api.GetSearch(raw_query=query)
        selected = random.choice(results)
        with open('/tmp/liked_tweets', 'a') as myfile:
            myfile.write(selected.text)
        if random.randint(0,100) < config.GENERAL_CONFIG['chanceToFavorite']:
          try:
            api.CreateFavorite(selected)
          except twitter.error.TwitterError as e:
            #Do nothing for now
            pass
        if random.randint(0,100) < config.GENERAL_CONFIG['chanceToFollow']:
          try:
            api.CreateFriendship(selected.user.id)
          except twitter.error.TwitterError as e:
            #Do nothing for now
            pass

if __name__ == '__main__':
    if random.randint(0,100) < config.GENERAL_CONFIG['chanceToAct']:
        LikeAndShareTwitterBot().main()
