# -*- coding: utf-8 -*-
from urllib import parse
import scrapy
import os
# o = parse.urlparse('http://url.something.com/bla.html?querystring=stuff')
# print(dir(o))
# print(o.query)
# url_without_query_string = o.scheme + "://" + o.netloc + o.path
dict1={}
out_dir="./out"
def queryToDic(query):
	dict1={}
	if "&" in query:
		fs=query.split("&")
	else:
		fs=query
	for f in fs:
		(l,r)=f.split("=")
		dict1[l]=r
	return dict1
def save(path,filename,response):
	if path=="" or path==None:
		path=out_dir
	else:
		path=os.path.join(out_dir,path)

	#print(path,filename)
	if filename==None or filename=="":
		#filename = response.url.split("/")[-2] + '.html'
		filename="index.html"
		pass
	else:
		fs=os.path.splitext(filename)
		#print(fs)
		if fs[1]=="":
			path=os.path.join(path,filename)
			filename="index.html"
		else:
			pass
	if not os.path.exists(path):
		try:
			os.makedirs(path)
		except FileExistsError as e:
			pass	

	outfile=os.path.join(path,filename)
	print(response.url)
	print(outfile)
	#input("here------------")
	with open(outfile, 'wb') as f:
		f.write(response.body)

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
					if dict1.get(url)==None:
						#print("--------------------")
						dict1[url]=True
						#print(len(dict1))
						#print(url)
						p=parse.urlparse(url)
						#print(p.query)
						qd=queryToDic(p.query)
						#print(qd.get("path"),qd.get("file"))
						#input("================")
						save(qd.get("path"),qd.get("file"),response)
						yield scrapy.Request(url,callback=self.parse)
					else:
						pass
		except AttributeError as e:
			pass