# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import csv

class IspMinerPipeline(object):
    def __init__(self):
        # self.total_file = open("Result.csv", 'w', encoding='utf-8', newline='')
        self.total_file = open("Result.csv", 'wb')
        self.writer = csv.writer(self.total_file)
        header = ["IP", "Domain", "Country", "Region", "City", "ISP", "ASN"]
        self.writer.writerow(header)

    def process_item(self, item, spider):
        ip = item.get("IP", "")
        domain = item.get("Domain", "")
        country = item.get("Country", "")
        region = item.get("Region", "")
        city = item.get("City", "")
        isp = item.get("ISP", "")
        asn = item.get("ASN", "")

        self.writer.writerow([ip, domain, country, region, city, isp, asn])
        return item