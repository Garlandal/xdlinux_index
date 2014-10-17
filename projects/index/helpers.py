#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from hashlib import md5

import os
import time
import re
import urllib
import urllib2
import json

def getDay(timestamp):
	timestamp = float(timestamp)
	FORY = '%d'
	str_time = time.strftime(FORY, time.localtime(timestamp))
	return str_time


def getMonth(timestamp):
	timestamp = float(timestamp)
	FORY = '%b'
	str_time = time.strftime(FORY, time.localtime(timestamp))
	return str_time

def getYear(timestamp):
    timestamp = float(timestamp)
    FORY = '%y'
    str_time = time.strftime(FORY, time.localtime(timestamp))
    return str_time


def formatDate(timestamp):
    timestamp = float(timestamp)
    FORY = '%Y-%m-%d @ %H:%M'
    FORM = '%m-%d @ %H:%M'
    FORH = '%H:%M'
    #os.environ["TZ"] = config.default_timezone
    #time.tzset()
    rtime = time.strftime(FORM, time.localtime(timestamp))
    htime = time.strftime(FORH, time.localtime(timestamp))
    now = int(time.time())
    t = now - timestamp
    if t < 60:
        str = u'刚刚'
    elif t < 60 * 60:
        min = t / 60
        str = u'%d 分钟前' % min
    elif t < 60 * 60 * 24:
        h = t / (60 * 60)
        str = u'%d 小时前 %s' % (h,htime)
    elif t < 60 * 60 * 24 * 3:
        d = t / (60 * 60 * 24)
        if d == 1:
            str = u'昨天 ' + rtime
        else:
            str = u'前天 ' + rtime
    else:
        str = time.strftime(FORY, time.localtime(timestamp))
    return str

def formatDate2(timestamp):
    timestamp = float(timestamp)
    FORY = '%Y-%m-%d @ %H:%M'
    #os.environ["TZ"] = config.default_timezone
    #time.tzset()
    str = time.strftime(FORY, time.localtime(timestamp))
    return str

def showPost(content,pid):
    end = content.find("<more>")
    if end != -1:
        readmore = u'<a class="readmore" href="/post/%s">>> 阅读更多</a>' % (pid)
        return content[0:end]+readmore
    else:
        return content

def formatText(text):
    floor = ur'#(\d+)楼\s'
    for match in re.finditer(floor, text):
        url = match.group(1)
        floor = match.group(0)
        nurl = u'<a class="toreply" href="#;">#<span class="tofloor">%s</span>楼 </a>' % (url)
        text = text.replace(floor, nurl)
    return text

def hitokoto():
	url = 'http://api.hitokoto.us/rand?cat=a&charset=utf-8&length=25'
	content = urllib2.urlopen(url).read()
	json_con = json.loads(content)
	text = json_con['hitokoto']
	return text
