FROM mhart/alpine-node
MAINTAINER celestian "petr.celestian@gmail.com"

RUN apk add --no-cache bash

COPY . /app
WORKDIR /app

RUN docker/build.sh

EXPOSE 5000


ENTRYPOINT ["docker/entrypoint.sh"]
