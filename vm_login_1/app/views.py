#coding:utf-8
from flask import render_template, url_for
from app import app, lm
from forms import LoginForm


@app.route('/') 
@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html', title = u'请登陆', form = form)

