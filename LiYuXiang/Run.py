# _*_ coding:utf-8 _*_
import os
class Run:
    def RunList(self, spider_name):
        os.system("scrapy crawl %s" % spider_name)

if __name__ == "__main__":
    _run = Run()
    _run.RunList("List")