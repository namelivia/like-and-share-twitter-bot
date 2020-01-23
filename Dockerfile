FROM python:3.8-alpine
WORKDIR /app
COPY . /app
RUN python setup.py install
CMD ["python", "like-and-share-twitter-bot/like-and-share-twitter-bot"]
