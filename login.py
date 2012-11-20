import flask, flask.views
from flask import session, g
import json

users = {'zak':'cheese','harry': 'potter'}

class Login(flask.views.MethodView):
	def get(self):
		return flask.render_template('login.html')

	def post(self):
		print g.db['users']
		if 'logout' in flask.request.form:
			flask.session.pop('username', None)
			return flask.redirect(flask.url_for('login'))

		#not entirely sure what the section to the blank line does?
		#possibly error checking?
		required = ['username', 'passwd']
		for r in required:
			if r not in flask.request.form:
				flask.flash("Error: {0} is required.".format(r))
				return flask.redirect(flask.url_for('login'))

		username = flask.request.form['username']
		passwd = flask.request.form['passwd']

		if username in users and users[username] == passwd:
			flask.session['username'] = username
			return flask.redirect(flask.url_for('main'))
		else:
			flask.flash("Incorrect Username or Password.")
			return flask.redirect(flask.url_for('login'))