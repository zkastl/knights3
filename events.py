from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import flask, flask.views
import os
import json

class Events(flask.views.MethodView):
	def get(self):
		return flask.render_template('events.html',entries=g.db['entries'])

	def post(self):
		if not 'username' in flask.session:
			print session.get('logged_in')
			print "ABORTED"
			abort(401)
		g.db['entries'].insert(0, {'title':request.form['title'], 'text':request.form['text']})
		flash('New entry was successfully posted')
		return redirect(url_for('events'))