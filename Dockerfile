# Dockerfile

FROM python:3.8-alpine

LABEL maintainer="mapachana"

WORKDIR /app
COPY ./poetry.lock ./pyproject.toml ./tasks.py /app/

RUN apk update; apk add curl; ln -s /usr/bin/python /usr/bin/python3.8; addgroup -S testgroup && adduser -S test -G testgroup
USER test
WORKDIR /app/test

RUN pip3 install invoke; wget -q -O - "$@" https://raw.githubusercontent.com/python-poetry/poetry/master/get-poetry.py | python -

ENV PATH=$PATH:/home/test/.local/bin:/home/test/.poetry/bin

RUN  poetry config virtualenvs.create false; invoke installdeps --dev

ENTRYPOINT ["invoke", "test"]

