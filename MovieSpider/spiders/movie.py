# -*- coding: utf-8 -*-
import scrapy
from MovieSpider.items import MoviespiderItem

class MovieSpider(scrapy.Spider):
    name = 'movie'
    allowed_domains = ['dytt8.net']
    start_urls = ['http://www.dytt8.net/html/gndy/dyzz/index.html']

    def parse(self, response):

        # 从响应体中提取出所有的电影信息
        movie_list = response.xpath("//div[@class='co_content8']//table")
        print(movie_list)
        # 遍历所有的电影，提取出详细的信息
        for movie in movie_list:
            # 创建一个模型
            item = MoviespiderItem()
            # 用item提取一级页面中的内容
            item["title"] = movie.xpath(".//a/text()").extract_first()
            item['date'] = movie.xpath(".//font/text()").extract_first()
            item['info'] = movie.xpath(".//tr[last()]/td/text()").extract_first()

            # 获取二级页面中的内容
            next_url = "http://www.dytt8.net" + movie.xpath(".//a/@href").extract_first()
            # 此时需要继续从二级页面中提取信息，就需要调用下载器继续下载
            yield scrapy.Request(url=next_url,callback=self.parse_next,meta={"movie_item":item})
            # Request下载器，有一个参数叫meta，它可以把meta里面的内容作为响应对象的一个属性传递出去


    # 定义一个成员方法，用于解析二级页面
    def parse_next(self,response):
        # item = MoviespiderItem()
        # 提取出上个页面中未完成item
        item = response.meta["movie_item"]

        # 在二级页面中提取其他的信息并存入item
        # 提取海报连接
        item['img'] = response.xpath("//div[@id='Zoom']//img[1]/@src").extract_first()
        # 提取剧情
        item["story"] = response.xpath("//div[@id='Zoom']").xpath("string(.)").extract_first()
        # 下载连接
        item["downloader"] = response.xpath("//td[@bgcolor='#fdfddf']/a/@href").extract_first()
        yield item



