FROM python:3.7.0 AS web-miner
MAINTAINER Liad Magen https://www.github.com/keep-current/web-miner
RUN mkdir -p /webminer
WORKDIR ./webminer
# Copies Everything
COPY . .        
RUN CGO_ENABLED=0 GOOS=linux pip install --upgrade pip \
    && pip install -r requirements.txt
CMD [ "python", "./manage.py", "docker" ]