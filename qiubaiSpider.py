#  -*- coding:utf-8 -*- 
import urllib
import urllib2
import re

#page  = 1
url = 'http://www.qiushibaike.com'
user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
headers = {'User-Agent' : user_agent}
try:
	request = urllib2.Request(url,headers = headers)
	response = urllib2.urlopen(request)
	content = response.read().decode('utf-8')
	#print response.read()
	pattern = re.compile(r'.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<div class="stats"'+
		r'>.*?<i class="number">(.*?)</i>',re.S)
	items = re.findall(pattern,content)
	for item in items:
		#print item[0],item[1],item[2]
		print item[0],item[1],item[2]
except urllib2.URLError, e:
	if  hasattr(e,"code"):
		print e.code
	if  hasattr(e,"reason"):
		print e.reason