FROM python:3.7-alpine
WORKDIR /app
COPY . /app
RUN pip install -e .
CMD ["python", "like_and_share_twitter_bot/like_and_share_twitter_bot.py"]
