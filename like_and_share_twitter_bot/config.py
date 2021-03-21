class Config:
    def __init__(self, source):
        self.config = {
            "idle_period": int(source["IDLE_PERIOD"]),
            "consumer_key": source["CONSUMER_KEY"],
            "consumer_secret": source["CONSUMER_SECRET"],
            "access_token_key": source["ACCESS_TOKEN_KEY"],
            "access_token_secret": source["ACCESS_TOKEN_SECRET"],
            "search_string": source["SEARCH_STRING"],
            "language": source["LANGUAGE"],
            "chance_to_favorite": int(source["CHANCE_TO_FAVORITE"]),
            "chance_to_follow": int(source["CHANCE_TO_FOLLOW"]),
            "chance_to_act": int(source["CHANCE_TO_ACT"]),
        }

    def get(self, key):
        return self.config[key]
