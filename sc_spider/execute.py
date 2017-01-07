from scrapy.cmdline import execute

execute("scrapy crawl songsan -o ../out/items.jl -s JOBDIR=../out/job_sc_spider".split())
