#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from flask import Flask, session, abort

import config

def currentUserGet():
	if "user" in session:
		user = session["user"]
		return user["username"]
	else:
		return None


def isAdmin():
	return currentUserGet() == config.INDEX_ADMIN_USER

def userAuth(username, password):
	return username == config.INDEX_ADMIN_USER and password == config.INDEX_ADMIN_PASSWORD

def currentUserSet(username):
	if username:
		session["user"] = dict({"username":username})
	else:
		session.pop("user",None)

def checkAdmin():
	if not isAdmin():
		abort(404)



