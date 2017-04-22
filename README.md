# sc_spider
A [SongCi](https://en.wikipedia.org/wiki/Ci_(poetry)) spider project. (Chinese: 宋词爬虫)

## Overview
An efficient spider based on [scrapy](https://github.com/scrapy/scrapy) to crawl [SongCi](https://en.wikipedia.org/wiki/Ci_(poetry)) from web.

Results can be saved into multiple formats of files, as well as into [MongoDB](https://www.mongodb.com/) collections.

## Requirements

* Python 3.5+
* (Optional) Docker && Docker-compose
* (Optional) Mongodb

## Usage

You may choose one of the following methods.

However, using docker is the recommended way, as you don't need to bother installing and configuring MongoDB and other stuff.

### Docker

1. Install Docker && Docker-compose.

```bash
docker-compose up
```

### Command Line (scrapy)

1. Install MongoDB
2. Install project requirements: `pip install -r requirements.txt`

```bash
cd sc_scrapy
scrapy crawl gushiwen -s MONGO_URI=localhost:27017
```

### Command Line (python)

1. Install MongoDB
2. Install project requirements: `pip install -r requirements.txt`
3. Edit your hosts file, adding: `127.0.0.1  mongo`
Or
4. Modify `MONGO_URI` settings in `sc_scrapy/settings.py`.

```bash
cd sc_scrapy
python execute.py
```

## Features

* Fast and flexible
* Able to pause and resume crawls, as Requests are serializable.
* Multiple output formats (thanks to scrapy) with UTF8 literals support

## Releases

You can download the latest stable releases from: https://github.com/wings27/sc_spider/releases
