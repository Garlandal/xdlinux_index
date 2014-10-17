#coding: utf-8

import os
import json
import pymongo

#mongoDB config
local = os.environ.get("MONGODB",None)
services = json.loads(os.environ.get("VCAR_SERVICES","{}"))
if services:
	creds = services['mongodb-1.8'][0]['credentials']
	mongo_uri = "mongodb://%s:%s@%s:%d%s" % (
			creds["username"],
			creds["password"],
			creds["hostname"],
			creds["port"],
			creds["db"]
			)
else:
	mongo_uri = None

#index_post = pymongo.Connection(mongo_uri).xdlinux.index.post
index_post = pymongo.Connection(mongo_uri).db["post"]


#site info
SECRET_KEY = "&%&*t&*gu(t*^$%r*ygoih)y^(*^*oyhoiut*&%$r*t)*)"
SITE_TITLE = '西電開源社區'
SITE_URL = ''
INDEX_PERPAGE = 8

#Index admin username and password
INDEX_ADMIN_USER = 'xdlinux'
INDEX_ADMIN_PASSWORD = '000000'
DEFAULT_TIMEZONE = 'Asia/Shanghai'
