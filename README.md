# Like And Share Twitter Bot [![tag](https://img.shields.io/github/tag/namelivia/like-and-share-twitter-bot.svg)](https://github.com/namelivia/like-and-share-twitter-bot/releases) [![Build Status](https://github.com/namelivia/like-and-share-twitter-bot/actions/workflows/build.yml/badge.svg)](https://github.com/namelivia/like-and-share-twitter-bot/actions/workflows/build.yml) [![codecov](https://codecov.io/gh/namelivia/like-and-share-twitter-bot/branch/master/graph/badge.svg)](https://codecov.io/gh/namelivia/like-and-share-twitter-bot)

This is a Python script I made one day after work, it will search for a tweet and then make favorite or follow the profile, all condimented with a bit of randomness.

## Requeriments

* python3.7
* pipenv

## Installation

Clone the project, navigate to its root folder and execute `pipenv install` for installing it's dependencies.

## Configuration

To execute the script the following environment variables must be set.

* `CONSUMER_KEY`: Your Twitter account consumer key.
* `CONSUMER_SECRET`: Your Twitter account consumer secret.
* `ACCESS_TOKEN_KEY`: Your Twitter account access token key.
* `ACCESS_TOKEN_SECRET`: Your Twitter account access token secret.
* `SEARCH_STRING`: The [Twitter search](https://help.twitter.com/en/using-twitter/twitter-advanced-search) string. e.g. `cats OR kitties`
* `CHANCE_TO_ACT`: The chances to actually do something or just idle (from 0 to 100). e.g. `40`
* `CHANCE_TO_FAVORITE`: The chances to mark a tweet as favorite (from 0 to 100). e.g. `20`
* `CHANCE_TO_FOLLOW`: The chances to follow the profile who tweeted (from 0 to 100). e.g. `15`
* `LANGUAGE`: The language code for the [Twitter search](https://help.twitter.com/en/using-twitter/twitter-advanced-search). e.g. `en`
* `IDLE_PERIOD`: The number of seconds the script will wait before executing. e.g. `900`

## Usage

Just execute `pipenv run python main.py` and if everything is properly configured it will search for a tweet (or not), will make it favorite (or not) and follow the profile who tweeted (or not).

## Testing

For executing the tests just execute `python3 -m unittest discover` on the project's root folder.

## Docker deployment

A Docker image for a containerized development is included, when the container is running the bot. Find it on [DockerHub](https://hub.docker.com/r/namelivia/like-and-share-twitter-bot).

## Contributing
Any suggestion, bug reports, or any other kind enhacements are welcome. Just [open an issue first](https://github.com/namelivia/like-and-share-twitter-bot/issues/new) for creating a PR remember this project has linting checkings so any PR should comply with them before beign merged, this checks will be automatically applied when opening or modifying the PR's.
