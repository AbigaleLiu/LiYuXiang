# _*_ coding:utf-8 _*_
from scrapy import *
from LiYuXiang.items import *

class List(Spider):
    name = "List"
    allowed_domains = "01xiang.com"
    start_urls = ["http://www.01xiang.com/2017y/"]

    def parse(self, response):
        items = LiyuxiangItem()
        for sel in response.selector.xpath("/html/body/table[5]/tr/td/table[2]/tr/td"):
            url = ["http://www.01xiang.com" + url for url in sel.xpath("ul/li/a/@href").extract()]  # 列表推导式
            items["url"] = url
            title = sel.xpath("ul/li/a/@title").extract()
            items["title"] = title
        print(items["url"])
        for item in range(len(items["url"])):
            yield Request(items['url'][item], callback=self.parse_text)

    def parse_text(self, response):
        item = response.meta["url"]
        selectors = response.selector.xpath("/html/body/table[5]/tr/td/table[@class='box']/tr/td/table[2]/tr/td")
        print("text")
        # copy_wirte = selectors.xpath("p")
        # print(copy_wirte)
        for sel in selectors:
            text = sel.xpath("div/text()").extract()
            item["text"] = text
        return item

