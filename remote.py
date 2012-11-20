import flask, flask.views
import os
import utils

class Remote(flask.views.MethodView):
	@utils.login_required
	def get(self):
		return flask.render_template('remote.html')

	@utils.login_required
	def post(self):
		results = eval(flask.request.form['expression'])
		flask.flash(results)
		return flask.redirect(flask.url_for('remote'))