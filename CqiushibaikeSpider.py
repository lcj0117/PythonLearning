__author__ = 'lcj'
# -*- coding:utf-8 -*-

'qiubi Spider'

import urllib
import urllib2
import re
import thread
import time


class QSBK:

    def __init__(self):
        self.pageIndex = 1
        self.user_agent = 'Mozilla/5.0 (Windows NT 6.1; WOW64)'
        # init headers
        self.headers = {'User-Agent': self.user_agent}
        self.stories = []
        self.enable = False

    def getPage(self, pageIndex):
        try:
            url = 'http://www.qiushibaike.com/8hr/page/' + \
                str(pageIndex) + '/?s=4894079'
            # construct the request
            request = urllib2.Request(url, headers=self.headers)
            # get the page code
            response = urllib2.urlopen(request)
            # convert the code to utf-8
            pageCode = response.read().decode('utf-8')
            return pageCode
        except urllib2.URLError, e:
            if hasattr(e, "reason"):
                print 'Can not connect to Qiushibaike', e.reason
                return None
    # get the story list

    def getPageItems(self, pageIndex):
    	pageCode = self.getPage(pageIndex)
        if not pageCode:
            print 'Fail to load the page...'
            return None
        pattern = re.compile(r'.*?<h2>(.*?)</h2>.*?<div class="content">(.*?)</div>.*?<div class="stats"' +
                             r'>.*?<i class="number">(.*?)</i>', re.S)
        items = re.findall(pattern, pageCode)

        pageStories = []

        for item in items:
            replaceBR = re.compile('<br/>')
            text = re.sub(replaceBR, "\n", item[1])
            pageStories.append(
                [item[0].strip(), item[1].strip(), item[2].strip()])
        return pageStories

    def loadPage(self):
    	if self.enable == True:
    		if len(self.stories) < 2:
    			#get new page
    			pageStories = self.getPageItems(self.pageIndex)
    			if pageStories:
    				self.stories.append(pageStories)
    				self.pageIndex += 1
    def getOneStory(self,pageStories,page):
    	for story in pageStories:
    		input = raw_input()
    		self.loadPage()
    		if input == 'Q':
    			self.enable = False
    			return
    		print "PageIndex:%d\tAuthor:%s\tLike:%s\n%s" % (page,story[0],story[2],story[1])
    #start
    def start(self):
    	print "Reading...Enter to check,Q to quit..."
    	self.enable = True
    	self.loadPage()
    	nowPage = 0
    	while self.enable:
    		if len(self.stories) > 0:
    			pageStories = self.stories[0]
    			nowPage += 1
    			del self.stories[0]
    			self.getOneStory(pageStories,nowPage)

spider = QSBK()
spider.start()
