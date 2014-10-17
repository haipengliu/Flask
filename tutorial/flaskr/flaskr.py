# application moduel, by haipeng #

# all the imports
import sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, render_template, flash

# DATABASE's import & configuration
# Can be putted here or create a indepedent .ini or .py file, then import here
DATABASE   = 'tmp/flaskr.db'
DEBUG      = True
SECRET_KEY = 'development key'
USERNAME   = 'admin'
PASSWORD   = 'default'

# create out little application, config it with the same file
app = Flask(__name__)
app.config.from_object(__name__)

def connect_db():
    return sqlite3.connect(app.config['DATABASE'])

if __name__=='__main__':
    app.debug = True
    app.run(host='172.27.17.9:5000')





