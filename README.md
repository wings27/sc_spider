# sc_spider
宋词爬虫

## Usage

### Dependencies
1. Install mongodb
2. (Optional) Docker && Docker-compose.

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
