# Keep-Current - The Web Miner

<!-- Badges section here. -->
[![Build Status](https://travis-ci.org/Keep-Current/web-miner.svg?branch=master)](https://travis-ci.org/Keep-Current/Web-Miner)
[![BCH compliance](https://bettercodehub.com/edge/badge/Keep-Current/web-miner?branch=master)](https://bettercodehub.com/)

## Web Miner

This repository is the web miner of the [Keep-Current project](#keep-current-project).

The goal is to deploy a web crawler, that given a specific set of sources (URLs), should locate new documents (web-pages) and save them in the DB for future processing.
When possible and legal, an API can be used.
For example, for [arxiv.org](https://arxiv.org/help/api/index).

### Potential tools to implement

## Web Miner

This repository deploys a web spider and documenr miner, that given a specific set of sources (URLs), should locate new documents (web-pages) and save them in the DB for future processing.
When possible, in websites that allow, an API can be used. For example, for [arxiv.org](https://arxiv.org/help/api/index).

We lean heavily on existing tools as well as developing our own new methods.

- [scrapy](https://scrapy.org/) which later we hope to host on [scrapy-cloud](https://scrapinghub.com/scrapy-cloud)
- [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash) which can render JS-based pages before storing them.
- [Textract](https://github.com/deanmalmgren/textract) can be used to extract the content (the text) to be saved.

### Getting started

for running this project locally, please install pipenv.

```
pip install pipenv
```

Then run:

```
pipenv install
```

after all the dependencies are installed, please run

```
pipenv run python manage.py server
```

### Architecture

We follow the [clean architecture style](http://blog.thedigitalcatonline.com/blog/2016/11/14/clean-architectures-in-python-a-step-by-step-example/) and structure the codebase accordingly.

![ceanArchitecture image](https://cdn-images-1.medium.com/max/1600/1*B7LkQDyDqLN3rRSrNYkETA.jpeg)

*Image creadit to [Thang Chung under MIT terms](https://github.com/thangchung/blog-core)*

## Who are we?

This project intends to be a shared work of meetup members, with the purpose, beside the obvious result, to also be used as a learning platform, while advancing the Natural Language Processing / Machine Learning field by exploring, comparing and hacking different models.

Please visit
- the project board on [Github](https://github.com/orgs/Keep-Current/projects)
- the repository board on [Github](https://github.com/Keep-Current/web-miner/projects)
- our chat room on [Slack](https://keep-current.slack.com). If you're new, you can join using [this link](https://join.slack.com/t/keep-current/shared_invite/enQtMzY4MTA0OTQ0NTAzLTcxY2U5NmIwNmM0NmU2MmMyMWQ0YTIyMTg4MWRjMWUyYmVlNWQxMzU3ZWJlNjM4NzVmNTFhM2FjYjkzZDU3YWM)

for more.

## How to Contribute
You can find our Project board here on (GitHub)[https://github.com/Keep-Current/web-miner/projects] and we use [Slack](https://keep-current.slack.com) as our communication channel. If you're new, you can join using [this link](https://join.slack.com/t/keep-current/shared_invite/enQtMzY4MTA0OTQ0NTAzLTcxY2U5NmIwNmM0NmU2MmMyMWQ0YTIyMTg4MWRjMWUyYmVlNWQxMzU3ZWJlNjM4NzVmNTFhM2FjYjkzZDU3YWM )

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

*Feel free to join the discussion and provide your input!*

[travis-badge-url]: https://travis-ci.org/Keep-Current/web-miner.svg?branch=master
