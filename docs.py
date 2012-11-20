import flask, flask.views
import os
import utils

class Docs(flask.views.MethodView):
	@utils.login_required
	def get(self):
		docs = os.listdir('static/docs')
		return flask.render_template("docs.html", docs=docs)