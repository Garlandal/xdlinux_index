#!/usr/bin/env python
from flask import Flask, Request, Response, Blueprint

import time
import sys
import os
import json
import config

#import projects.index.views
from projects.index.views import index_page

app = Flask('wsgi')
app.secret_key = config.SECRET_KEY
app.config.from_object(config)

app.register_blueprint(index_page)

if __name__ == "__main__":
	app.run(debug = True,host = '0.0.0.0')
