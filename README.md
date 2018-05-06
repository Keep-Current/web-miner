# Keep-Current - The Web Crawler

<!-- Badges section here. -->
[![Build Status](https://img.shields.io/travis/liadmagen/Keep-Current-Crawler/master.svg?label=travis)][travis-badge-url]

After studying a topic, keeping current with the news, published papers, advanced technologies and such proved to be a hard work.
One must attend conventions, subscribe to different websites and newsletters, go over different emails, alerts and such while filtering the relevant data out of these sources.

In this project, we aspire to create a platform for students, researchers, professionals and enthusiasts to discover news on relevant topics. The users are encouraged to constantly give a feedback on the suggestions, in order to adapt and personalize future results.

The goal is to create an automated system that scans the web, through a list of trusted sources, classify and categorize the documents it finds, and match them to the different users, according to their interest. It then presents it as a timely summarized digest to the user, whether by email or within a site.

## Who are we?

This project intends to be a shared work of *Vienna Data Science Cafe* Meet-Up members, with the purpose, beside the obvious result, to also be used as a learning platform, while advancing the Natural Language Processing / Machine Learning field by exploring, comparing and hacking different models.

Please feel free to [contribute](CONTRIBUTING.md).

Project board is on [Trello](https://trello.com/b/KmMEPjfT/keep-current) and we use [Slack](https://vdsg.slack.com/messages/C9BNW5N9L/details) as our communication channel.

## I want to help

We welcome anyone who would like to join and contribute. We meet regularly every month in Vienna through the Data Science Cafe meetup of the VDSG, show our progress and discuss the next steps.

## Web Crawler

This repository deploys a web crawler, that given a specific set of sources (URLs), should locate new documents (web-pages) and save them in the DB for future processing.
When possible, in websites that allow, an API can be used. For example, for [arxiv.org](https://arxiv.org/help/api/index).

### Recommended tools:

We lean heavily on existing tools as well as developing our own new methods. Among the existing tools we are using [scrapy](https://scrapy.org/) which later we hope to host on [scrapy-cloud](https://scrapinghub.com/scrapy-cloud).
Another related tool that should be considered is [scrapy-splash](https://github.com/scrapy-plugins/scrapy-splash) which can render JS-based pages before storing them.
and [Textract](https://github.com/deanmalmgren/textract) can be used to extract the content, the text, to be saved.

## The repository

This repository is the web crawler / spider.
If you wish to assist in different aspects (Data Engineering / Web development / DevOps), we have divided the project to several additional repositories focusing on these topics:

* The machine-learning engine can be found in our [Main repository](https://github.com/Keep-Current/Keep-Current)
* Web Development & UI/UX experiments can be found in our [App repository](https://github.com/Keep-Current/Keep-Current-App)
* Data Engineering tasks are more than welcomed in our [Data Engineering repository](https://github.com/Keep-Current/Keep-Current-Storage)
* Devops tasks are all across the project. We are trying to develop this project in a serverless architecture, and currently looking into Docker and Kubernetes as well as different hosting providers and plans. Feel free to join the discussion and provide your input!

[travis-badge-url]: https://travis-ci.org/liadmagen/Keep-Current.svg?branch=master