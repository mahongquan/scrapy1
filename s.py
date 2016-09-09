from scrapy.selector import Selector
body=open("explore.html","r").read()
s=Selector(text=body)
#.xpath('//span/text()').extract()
#print(r)