import scrapy
from ..items import DummyItem
from time import sleep

class DummySpider(scrapy.Spider):
    name = 'dummy'
    start_urls = ['https://pogo.indigodata.co.jp/']
    
    wait_time = 0

    def __init__(self, *args, **kwargs):
        super(DummySpider, self).__init__(*args, **kwargs)
        self.custom_arg = kwargs.get('custom_arg')
        
        try:
            self.wait_time = int(kwargs.get('wait_time', 0))
        except:
            pass

    def parse(self, response):
        data = response.xpath('//*[@id="loginForm"]/div[1]/div/input/@placeholder').get()
        item = DummyItem(data)
        
        sleep(self.wait_time)
        
        yield item
