FROM python:3.7-alpine AS builder
WORKDIR /app
COPY . /app
RUN apk add gcc musl-dev
RUN pip install pipenv

FROM builder AS development
RUN pipenv install --dev

FROM builder AS production
RUN pipenv install
CMD ["pipenv", "run", "python", "main.py"]
