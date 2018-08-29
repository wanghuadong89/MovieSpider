# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class MoviespiderItem(scrapy.Item):
    # 一级页面
    # title
    title = scrapy.Field()
    # 简介
    info = scrapy.Field()
    # 日期
    date = scrapy.Field()
    # 二级页面
    # 海报
    img = scrapy.Field()
    # 剧情
    story = scrapy.Field()
    # 下载链接
    downloader = scrapy.Field()
