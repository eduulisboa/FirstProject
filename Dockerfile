FROM python:3.8-slim-buster

WORKDIR /usr/app

COPY ./Pipfile .

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv lock -r > requirements.txt && \
    pip uninstall --yes pipenv && \
    pip install -r requirements.txt

COPY . .