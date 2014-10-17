#!/usr/bin/env python
# _*_ coding: utf-8 _*_

from flask import Blueprint, Flask, request, session, g, redirect
from flask import render_template, abort
from helpers import *
from pymongo import DESCENDING, ASCENDING
from bson.objectid import ObjectId


import base
import config
import markdown
import time

index_page = Blueprint("index_page", __name__, template_folder = 'templates')


@index_page.route("/")
@index_page.route("/index")
def index():
	posts = config.index_post.find().sort("created_date",DESCENDING).limit(4)
	return render_template("home.html", 
			getDay = getDay,
			getMonth = getMonth,
			getYear = getYear,
			posts = posts,
			hitokoto = hitokoto)

@index_page.route("/index/login", methods = ["GET", "POST"])
def login():
	if request.method == "GET":
		if base.isAdmin():
			return redirect("/")
		else:
			return render_template("login.html",
					hitokoto = hitokoto)
	username = request.form["username"]
	password = request.form['password']
	if base.userAuth(username,password):
		base.currentUserSet(username)
		return redirect("/")
	else:
		return redirect("/index/login")

@index_page.route("/index/logout")
def logout():
	session.pop("user", None)
	return redirect("/index/login")

@index_page.route("/index/post/add", methods = ["GET", "POST"])
def add_post():
	if request.method == "GET":
		base.checkAdmin()
		return render_template("postadd.html",
				hitokoto = hitokoto)
	base.checkAdmin()
	title = request.form["post[title]"]
	origin_content = request.form["post[content]"]
	content = markdown.markdown(origin_content)
	if title != "" and origin_content != "":
		config.index_post.insert({
			"title":title,
			"content":content,
			"origin_content":origin_content,
			"created_date":time.time(),
			"update_date":time.time()})
		return redirect("/")
	else:
		return render_template("postadd.html", error = u'内容或者标题不能为空')

@index_page.route("/index/post/<pid>")
def show_post(pid):
	ids = ObjectId(pid)
	posts = config.index_post.find({"_id": ids})
	for i in posts:
		post = i
	if type(post) != type({}):
		abort(404)
	return render_template("post.html",
			post = post,
			hitokoto = hitokoto,
			formatDate = formatDate,
			formatDate2 = formatDate2)

@index_page.route("/index/post/edit/<pid>", methods = ["GET", "POST"])
def edit_post(pid):
	if request.method == "GET":
		base.checkAdmin()
		post = None
		for i in config.index_post.find({"_id":ObjectId(pid)}):
			post = i
		if post is None:
			abort(404)
		return render_template("postedit.html", post = post, hitokoto = hitokoto)
	base.checkAdmin()
	title = request.form["post[title]"]
	origin_content = request.form["post[content]"]
	content = markdown.markdown(origin_content)
	if title != '' and origin_content != '':
		for i in config.index_post.find({"_id":ObjectId(pid)}):
			post = i
		post["title"] = title
		post["origin_content"] = origin_content
		post["content"] = content
		config.index_post.update({"_id":ObjectId(pid)},post)
		return redirect("/index/post/%s" % pid)
	else:
		return render_template("postedit.html",  error = u'标题或内容不能为空')


