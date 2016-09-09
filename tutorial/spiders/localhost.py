# -*- coding: utf-8 -*-
import scrapy


class LocalhostSpider(scrapy.Spider):
	name = "localhost"
	allowed_domains = ["127.0.0.1"]
	start_urls = (
		'http://127.0.0.1:8000/explore',
	)
	def parse(self, response):
		# filename = response.url.split("/")[-2] + '.html'
		# with open(filename, 'wb') as f:
		# 	f.write(response.body)
		#print(response.url)
		try:
			for  url in response.xpath('//a/@href').extract():
				url=response.urljoin(url)
				if self.start_urls[0] in url:
					print(url)
					yield scrapy.Request(url,callback=self.parse)
		except AttributeError as e:
			pass