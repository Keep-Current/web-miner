# Keep-Current - The Web Miner

<!-- Badges section here. -->

[![Codacy Badge](https://api.codacy.com/project/badge/Grade/883c8e93b4934566b9dfdc6b91fa85e7)](https://app.codacy.com/app/Keep-Current/web-miner?utm_source=github.com&utm_medium=referral&utm_content=Keep-Current/web-miner&utm_campaign=badger)
[![Build Status](https://travis-ci.org/Keep-Current/web-miner.svg?branch=master)](https://travis-ci.org/Keep-Current/web-miner)
[![CircleCI](https://circleci.com/gh/Keep-Current/web-miner.svg?style=svg)](https://circleci.com/gh/Keep-Current/web-miner)
[![BCH compliance](https://bettercodehub.com/edge/badge/Keep-Current/web-miner?branch=master)](https://bettercodehub.com/)
[![codecov](https://codecov.io/gh/Keep-Current/web-miner/branch/master/graph/badge.svg)](https://codecov.io/gh/Keep-Current/web-miner)
[![codebeat badge](https://codebeat.co/badges/03da69a3-74cf-468d-80f9-bc62651323f7)](https://codebeat.co/projects/github-com-keep-current-web-miner-master)

## Web Miner

This repository is the web miner of the [Keep-Current project](#keep-current-project).

The goal is to deploy a web crawler, that given a specific set of sources (URLs), should locate new documents (web-pages) and save them in the DB for future processing.
When possible and legal, an API can be used.
For example, for [arxiv.org](https://arxiv.org/help/api/index).

### Potential tools to implement

We lean heavily on existing tools as well as developing our own new methods.

- [scrapy](https://scrapy.org/) which later we hope to host on [scrapy-cloud](https://scrapinghub.com/scrapy-cloud)
- [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash) which can render JS-based pages before storing them.
- [Textract](https://github.com/deanmalmgren/textract) can be used to extract the content (the text) to be saved.

### Getting started

for running this project locally, you need first to install the dependency packages.
To install them, you can use

- [pipenv](https://docs.pipenv.org/)
- [anaconda](https://anaconda.org/)
- [virtualenv](https://virtualenv.pypa.io/en/stable/)

#### Installation using pipenv (which combines virtualenv with pip)

Install pipenv

```bash
sudo easy_install pip # if you haven't installed pip
pip install pipenv # install pipenv

brew install pipenv # with homebrew (on macOS)
```

Install the packages and run the server

```bash
pipenv install # install all packages

pipenv run flask run # run the server
```

If you are on Windows OS, some packages may not be installed. Specifically - feedparser. In case the web server doesn't run, please install these packages manually using

```bash
pip install feedparser
```

#### Installing using Anaconda

If you have anaconda installed, it's recommended to create an environment for the project, and install the dependencies in it.

```bash
conda create -q -n web-miner python=3.6 # create the environment

source activate web-miner # activate the environment

pip install -r requirements.txt # install the packages
```

and test your installation by running the web server:

```bash
flask run # start server
```

#### Installing using virtualenv and pip

```bash
sudo easy_install pip # installl pip if you haven't

pip3 install --upgrade virtualenv # install virtualenv

virtualenv --python3 <targetDirectory> # create the environment

source <targetDirectory>/./bin/activate # activate the virtualenv

pip install -r requirements.txt # install the packages

python3 manage.py server # start server
```

### Architecture

### Project Architecture

We follow the [clean architecture style](https://8thlight.com/blog/uncle-bob/2012/08/13/the-clean-architecture.html) and structure the codebase accordingly.

![cleanArchitecture image](https://cdn-images-1.medium.com/max/1600/1*B7LkQDyDqLN3rRSrNYkETA.jpeg)

_Image credit to [Uncle Bob](https://8thlight.com/blog/uncle-bob/)_

Most important rule:

> Source code dependencies can only point inwards. Nothing in an inner circle can know anything at all about something in an outer circle. In particular, the name of something declared in an outer circle must not be mentioned by the code in the an inner circle. That includes, functions, classes. variables, or any other named software entity.

## Who are we?

This project intends to be a shared work of meetup members, with the purpose, beside the obvious result, to also be used as a learning platform, while advancing the Natural Language Processing / Machine Learning field by exploring, comparing and hacking different models.

Please visit

- the project board on [Github](https://github.com/orgs/Keep-Current/projects)
- the repository board on [Github](https://github.com/Keep-Current/web-miner/projects)
- our chat room on [Slack](https://keep-current.slack.com). If you're new, you can join using [this link](https://join.slack.com/t/keep-current/shared_invite/enQtMzY3Mzk1NjE2MzIzLWZlZWFjMDM1YWYxYmI5ZWE4YmZjNWYzMmNjMzlhMDYzOTIxZDViODhmNTMzZDI0NThmZWVlOTRjNjczZGJiOWE)

for more.

## How to Contribute

You can find our Project board here on [GitHub](https://github.com/Keep-Current/web-miner/projects) and we use [Slack](https://keep-current.slack.com) as our communication channel. If you're new, you can join using [this link](https://join.slack.com/t/keep-current/shared_invite/enQtMzY4MTA0OTQ0NTAzLTcxY2U5NmIwNmM0NmU2MmMyMWQ0YTIyMTg4MWRjMWUyYmVlNWQxMzU3ZWJlNjM4NzVmNTFhM2FjYjkzZDU3YWM)

We welcome anyone who would like to join and contribute.

Please see our [contribute guide](CONTRIBUTING.md).

We meet regularly every month in Vienna through

- the [Data Science Cafe meetup of the VDSG](https://www.meetup.com/Vienna-Data-Science-Group-Meetup/) or
- the [WeAreDevelopers :: Keep-Current meetup](https://www.meetup.com/WeAreDevelopers/)

to show our progress and discuss the next steps.

## Keep-Current Project

After studying a topic, keeping current with the news, published papers, advanced technologies and such proved to be a hard work.
One must attend conventions, subscribe to different websites and newsletters, go over different emails, alerts and such while filtering the relevant data out of these sources.

In this project, we aspire to create a platform for students, researchers, professionals and enthusiasts to discover news on relevant topics. The users are encouraged to constantly give a feedback on the suggestions, in order to adapt and personalize future results.

The goal is to create an automated system that scans the web, through a list of trusted sources, classify and categorize the documents it finds, and match them to the different users, according to their interest. It then presents it as a timely summarized digest to the user, whether by email or within a site.

This repository is the web miner. It encourage you to learn about software architecture, mining the web, setting up web-spiders, scheduling CRON Jobs, creating pipelines, etc.

If you wish to assist in different aspects (Data Engineering / Web development / DevOps), we have divided the project to several additional repositories focusing on these topics:

- The machine-learning engine can be found in our [Main repository](https://github.com/Keep-Current/Engine)
- Web Development & UI/UX experiments can be found in our [App repository](https://github.com/Keep-Current/WebApp)
- Data Engineering tasks are more than welcomed in our [Data Engineering repository](https://github.com/Keep-Current/Data-Engineering)
- Devops tasks are all across the project. This project is developed mostly in a serverless architecture. Using Docker and Kubernetes enables freedom in deploying it on different hosting providers and plans.

_Feel free to join the discussion and provide your input!_

[travis-badge-url]: https://travis-ci.org/Keep-Current/web-miner.svg?branch=master
