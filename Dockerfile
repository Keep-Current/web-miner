FROM python:3.7.0 AS web-miner
MAINTAINER "https://github.com/Keep-Current/web-miner"
LABEL Maintainer="Liad Magen https://www.github.com/keep-current/web-miner"
RUN mkdir -p /webminer
WORKDIR /webminer
# Copies Everything
COPY . .        
RUN CGO_ENABLED=0 GOOS=linux pip install --upgrade pip \
    && pip install pipenv \
    && pipenv install
CMD [ "flask", "run", "--host=0.0.0.0" ]
