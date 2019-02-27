# Like And Share Twitter Bot [![Build Status](https://travis-ci.com/namelivia/like-and-share-twitter-bot.svg?branch=master)](https://travis-ci.com/namelivia/like-and-share-twitter-bot)

This is a Python script I made one day after work, it will search for a tweet and then make favorite or follow the profile, all condimented with a bit of randomness.

## Requeriments

* python3
* pip3

## Installation

Clone the project, navigate to its root folder and execute `pip3 install -e . --user` for installing it's dependencies.

## Configuration

Copy `like_and_share_twitter_bot/config.example.py` to `like_and_share_twitter_bot/config.py`

Then open the file with a text editor and replace the default values with your actual values.

* `consumerKey`: Your Twitter account consumer key.
* `consumerSecret`: Your Twitter account consumer secret.
* `accessTokenKey`: Your Twitter account access token key.
* `accessTokenSecret`: Your Twitter account access token secret.
* `searchString`: The [Twitter search](https://help.twitter.com/en/using-twitter/twitter-advanced-search) string. e.g. `cats OR kitties`
* `chanceToAct`: The chances to actually do something or just idle (from 0 to 100). e.g. `40`
* `chanceToFavorite`: The chances to mark a tweet as favorite (from 0 to 100). e.g. `20`
* `chanceToFollow`: The chances to follow the profile who tweeted (from 0 to 100). e.g. `15`
* `language`: The language code for the [Twitter search](https://help.twitter.com/en/using-twitter/twitter-advanced-search). e.g. `en`

## Usage

Just execute `like_and_share_twitter_bot/like_and_share_twitter_bot.py` and if everything is properly configured it will search for a tweet (or not), will make it favorite (or not) and follow the profile who tweeted (or not).

## Testing

For executing the tests just execute `python3 -m unittest discover` on the project's root folder.

## Contributing
Any suggestion, bug reports, or any other kind enhacements are welcome. Just [open an issue first](https://github.com/namelivia/like-and-share-twitter-bot/issues/new) for creating a PR remember this project has linting checkings so any PR should comply with them before beign merged, this checks will be automatically applied when opening or modifying the PR's.
