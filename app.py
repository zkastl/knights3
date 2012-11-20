"""
    Knights of Columbus OKState site

    author: Zachary Kastl
    copyright:  2012

    acknowledgments:    Armin Ronacher (for both flask itself and the flaskr microblog)
                        www.youtube.com/user/calicoJake (for the layout)
    Uses Python 2.7.2
    Tracked with Git 2

"""

from __future__ import with_statement
import flask
import settings

#imports from the blog
from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import request, session, g, redirect, url_for, abort, \
     render_template, flash
import json

#views
from main import Main
from login import Login
from remote import Remote
from music import Music
from events import Events
from users import Users
from docs import Docs

# configuration
DATABASE = 'test.json'

app = flask.Flask(__name__)
app.secret_key = settings.secret_key

#URL rules:  add as needed for the various dynamic pages
app.add_url_rule('/', view_func=Main.as_view('main'), methods=('get','post'))
app.add_url_rule('/<page>/', view_func=Main.as_view('main'), methods=('get','post'))
app.add_url_rule('/login/', view_func=Login.as_view('login'), methods=('get','post'))
app.add_url_rule('/remote/', view_func=Remote.as_view('remote'), methods=('get','post'))
app.add_url_rule('/music/', view_func=Music.as_view('music'), methods=('get', 'post'))
app.add_url_rule('/events/', view_func=Events.as_view('events'), methods=('get','post'))
app.add_url_rule('/users/', view_func=Users.as_view('users'), methods=('get','post'))
app.add_url_rule('/docs/', view_func=Docs.as_view('docs'), methods=('get','post'))

#error handling wrapper
@app.errorhandler(404)
def page_not_found(error):
	return flask.render_template('404.html'), 404

#database handling wrappers
@app.before_request
def before_request():
    """Make sure we are connected to the database each request."""
    try:
        db = open(DATABASE).read()
    except IOError:
        db = '{"users":[],"entries":[]}'
    g.db = json.loads(db)
    
@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        open(DATABASE, 'w').write(json.dumps(g.db, indent=4))

app.debug = True
if __name__ == '__main__':
    app.run('0.0.0.0')
