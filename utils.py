import flask
import functools

"""
This module checks for pages that require a login.  This allows for nosey users
to be stopped if they try for a hidden page that still requires a login.  It 
redirects users to the login page if the session doesn't have the username/pw
stored.
"""
def login_required(method):
	@functools.wraps(method)
	def wrapper(*args, **kwargs):
		if 'username' in flask.session:
			return method(*args, **kwargs)
		else:
			flask.flash("a login is required to see this page!")
			return flask.redirect(flask.url_for('login'))
	return wrapper