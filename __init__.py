#coding=utf8
import os

from flask import Flask
from flask.ext.mongoengine import MongoEngine
from flask.ext.admin import Admin

import xdlinux

app = Flask(__name__)
app.config['MONGODB_SEETINGS'] = {
		'db':'xdlinux',
		'host':'mongodb://localhost/'
		}

db = MongoEngine(app)




if __name__ == "__main__":
	app.run()
