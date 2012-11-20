from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import flask, flask.views
import os
import json

class Users(flask.views.MethodView):
	def get(self):
		return flask.render_template('users.html', users=g.db['users'])

	def post(self):
		if not 'username' in flask.session:
			print session.get('logged_in')
			abort(401)
		un = request.form['username']
		pw = request.form['password']
		pm = request.form['status']
		if un and pw and pm != "":
			g.db['users'].insert(0, {'username':un, 'passwd':pw, 'permissions':pm})
			flash('New user was successfully added')
		else:
			printw ("Nope!")
		return redirect(url_for('users'))