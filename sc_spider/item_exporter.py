from scrapy.contrib.exporter import JsonItemExporter


class UnicodeJsonItemExporter(JsonItemExporter):
    def __init__(self, file, **kwargs):
        super().__init__(file, **kwargs)
        self.encoder.ensure_ascii = False
