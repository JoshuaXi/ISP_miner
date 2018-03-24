# -*- coding: utf-8 -*-
import scrapy
import re
from scrapy import Spider
from scrapy.http import FormRequest
from isp_miner.items import IspMinerItem
import csv
import os

def readCSV(file_name):
    contents = open(file_name).read().split("\n")
    return contents

class IspSpiderSpider(scrapy.Spider):
    name = 'isp_spider'
    # allowed_domains = ['www.infobyip.com']
    # start_urls = ['http://www.infobyip.com/']

    def start_requests(self):
        cur_path = os.getcwd()
        file_name = cur_path + "/isp_miner/data/IP_test.csv"
        self.lines = readCSV(file_name)
        self.total_cnt = 0

        ip_list = []
        for i, line in enumerate(self.lines):
            if i==0:
                continue
            ip_list.append(line)
            if i % 100 == 0 or i==(len(self.lines)-2):
                ip_stream = " ".join(ip_list)
                # ip_list = "17.172.224.47 23.100.122.175 151.101.184.116 " + \
                #           "205.251.242.103 172.217.12.78"
                request_url = "https://www.infobyip.com/ipbulklookup.php"
                ip_list = []
                yield FormRequest(
                    request_url,
                    method="POST",
                    formdata={"ips": ip_stream, "record_type": "none"},
                    callback=self.parse
                )



    def parse(self, response):
        print(response)
        content = response.xpath("//td[@id='output']")
        rows = content.xpath(".//table/tr")[1:]
        keys = content.xpath(".//table/tr[1]/th/text()").extract()
        for row in rows:
            data = row.xpath("td").extract()
            pattern = re.compile(
                "(<[\w\s\'\"\:\;\/\?\!\@\#\$\%\^\&\*\_\-\=\+.]+>)")
            clear_data = [
                re.sub(pattern, "", d) for d in data
            ]
            clear_data = {key: value for key, value
                          in list(zip(keys, clear_data))}
            self.total_cnt+=1
            print(self.total_cnt, "\t==>\t", clear_data)
            yield IspMinerItem(clear_data)

"""
scrapy crawl isp_spider -s LOG_ENABLED=False
"""