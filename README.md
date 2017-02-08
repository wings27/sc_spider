# sc_spider
Chinese: 宋词爬虫

## Overview
A spider based on [scrapy](https://github.com/scrapy/scrapy) to crawl [SongCi](https://en.wikipedia.org/wiki/Ci_(poetry)) from web.

## Usage
### Requirements
1. Install mongodb
2. `pip install -r requirements.txt`
3. (Optional) Docker && Docker-compose.

### How to Run

You may choose one of the following methods.

#### Docker
```bash
docker-compose up
```

#### Command Line (scrapy)
```bash
cd sc_scrapy
scrapy crawl gushiwen -s MONGO_URI=localhost:27017
```

#### Command Line (python)
Add `127.0.0.1  mongo` to your hosts file. Or modify `MONGO_URI` settings in `sc_scrapy/settings.py`.
And then:
```bash
cd sc_scrapy
python execute.py
```
