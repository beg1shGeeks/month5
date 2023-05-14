FROM python:3.9

ENV PYTHONWRITEBYTECODE 1
ENV PYTHONBUFFERED 1

WORKDIR /movie_app

COPY requirements.txt /movie_app

RUN pip install -r /app/requrements.txt

COPY ./movie_app

