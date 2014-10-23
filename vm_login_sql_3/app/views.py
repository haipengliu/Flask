from flask import render_template, flash, redirect, session, url_for, request
from app import app, models
from forms import LoginForm
from models import User

@app.route('/', methods=['GET', 'POST'])
@app.route('/login', methods=['GET', 'POST'])
def login():
  form = LoginForm()
   
  if request.method == 'POST':
      if form.validate() == False:
          return render_template('login.html', form=form)
      else:
          session['username'] = form.username.data
          return redirect(url_for('index'))
                 
  elif request.method == 'GET':
    return render_template('login.html', form=form)

  return render_template('login.html', form=form)

@app.route('/logout')
def logout():
  session.pop('username', None)
  return redirect(url_for('login'))

@app.route('/index')
def index():
  if 'username' not in session:
    return redirect(url_for('login'))
 
  user = User.query.filter_by(username = session['username']).first()
 
  if user is None:
    return redirect(url_for('login'))
  else:
    return render_template('index.html', user = user)
