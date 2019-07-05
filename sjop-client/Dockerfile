FROM mhart/alpine-node AS builder
MAINTAINER celestian "petr.celestian@gmail.com"
COPY . /app
WORKDIR /app
RUN npm run build

FROM mhart/alpine-node
RUN npm --global add serve
WORKDIR /app
COPY --from=builder /app/build .
CMD ["serve", "-p", "8080", "-s", "."]
