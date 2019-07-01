FROM alpine:latest
MAINTAINER celestian "petr.celestian@gmail.com"

RUN apk add --no-cache bash nodejs

COPY . /app
WORKDIR /app

RUN docker/build.sh

EXPOSE 5000


ENTRYPOINT ["docker/entrypoint.sh"]
