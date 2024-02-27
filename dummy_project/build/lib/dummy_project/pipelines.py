# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://docs.scrapy.org/en/latest/topics/item-pipeline.html


# useful for handling different item types with a single interface
from itemadapter import ItemAdapter
from datetime import datetime

class DummyProjectPipeline:
    def process_item(self, item, spider):
        return item
    
import csv

class CsvPipeline:
    def open_spider(self, spider):
        self.file = open('items.csv', 'a', newline='')
        self.file.write(datetime.now().strftime('%Y-%m-%d %H:%M:%S') + '\n')
        self.writer = csv.writer(self.file)

    def close_spider(self, spider):
        self.file.close()

    def process_item(self, item, spider):
        self.writer.writerow(item.values())
        return item