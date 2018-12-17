FROM wearedevelopers/alpine-ml:v0.6

LABEL MAINTAINER="https://github.com/Keep-Current/web-miner"

WORKDIR /usr/local/bin
WORKDIR /usr/local/engine

COPY ./requirements.txt ./

RUN apk update && \
    apk --no-cache add libstdc++ openssl libressl-dev ca-certificates && \
    apk --no-cache add --virtual builddeps g++ gfortran musl-dev lapack-dev gcc make && \
    pip install -r requirements.txt && \
    apk del builddeps     && \
    rm -rf /root/.cache

# Copies Everything
COPY ./ ./

#--log-level=info --log-file=./logs/gunicorn.log --access-logfile=./logs/gunicorn-access.log
CMD gunicorn -w 4 -b 0.0.0.0:${PORT} wsgi:app 