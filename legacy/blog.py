# -*- coding: utf-8 -*-
"""
    Flaskr
    ~~~~~~

    A microblog example application written as Flask tutorial with
    Flask and sqlite3.

    :copyright: (c) 2010 by Armin Ronacher.
    :license: BSD, see LICENSE for more details.
"""
from __future__ import with_statement
from sqlite3 import dbapi2 as sqlite3
from contextlib import closing
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash
import json

# configuration
DATABASE = 'test.json'
DEBUG = True
SECRET_KEY = 'development key'
USERNAME = 'ticey'
PASSWORD = 'Minecraft*200'

# create our little application :)
app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('FLASKR_SETTINGS', silent=True)

@app.before_request
def before_request():
    """Make sure we are connected to the database each request."""
    try:
        db = open(DATABASE).read()
    except IOError:
        db = '{"entries":[]}'
    g.db = json.loads(db)


@app.teardown_request
def teardown_request(exception):
    """Closes the database again at the end of the request."""
    if hasattr(g, 'db'):
        open(DATABASE, 'w').write(json.dumps(g.db, indent=4))


@app.route('/')
def show_entries():
    return render_template('show_entries.html', entries=g.db['entries'])


@app.route('/add', methods=['POST'])
def add_entry():
    if not session.get('logged_in'):
        abort(401)
    g.db['entries'].insert(0, {'title':request.form['title'], 'text':request.form['text']})
    flash('New entry was successfully posted')
    return redirect(url_for('show_entries'))
    

@app.route('/login', methods=['GET', 'POST'])
def login():
    error = None
    if request.method == 'POST':
        if request.form['username'] != app.config['USERNAME']:
            error = 'Invalid username'
        elif request.form['password'] != app.config['PASSWORD']:
            error = 'Invalid password'
        else:
            session['logged_in'] = True
            flash('You were logged in')
            return redirect(url_for('show_entries'))
    return render_template('login2.html', error=error)


@app.route('/logout')
def logout():
    session.pop('logged_in', None)
    flash('You were logged out')
    return redirect(url_for('show_entries'))


if __name__ == '__main__':
    app.run()
