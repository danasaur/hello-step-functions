FROM continuumio/miniconda

RUN apt-get update
RUN apt-get install -y \
    build-essential \
    curl \
    python-dev

RUN mkdir -p /code/
WORKDIR /code

ADD . /code

RUN apt-get -y install zip