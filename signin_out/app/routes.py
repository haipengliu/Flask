#coding : utf-8
from app import app
from flask import render_template, request, flash, session, redirect, url_for
from forms import SignupForm, ChangePwd
from app import models
 
# mappings start here
@app.route('/', methods=['GET', 'POST'])
@app.route('/signin', methods=['GET', 'POST'])
def signin():
  form = SignupForm()
   
  if request.method == 'POST':
      if form.validate() == False:
          return render_template('signin.html', form=form)
      else:
          session['username'] = form.username.data
          return redirect(url_for('profile'))
                 
  elif request.method == 'GET':
    return render_template('signin.html', form=form)

  return render_template('signin.html', form=form)


@app.route('/changepwd', methods=['GET', 'POST'])
def changepwd():
  form = ChangePwd()
   
  if request.method == 'POST':
    if form.validate() == False:
      return render_template('changepwd.html', form=form)
    else:
      newuser = User(form.firstname.data, form.lastname.data, form.email.data, form.password.data)
      db.session.add(newuser)
      db.session.commit()
       
      session['username'] = newuser.username
      return redirect(url_for('profile'))
   
  elif request.method == 'GET':
    return render_template('changepwd.html', form=form)  
  
  
@app.route('/signout')
def signout():
 
  session.pop('username', None)
  return redirect(url_for('signin'))


@app.route('/profile')
def profile():
    
    if 'username' not in session:
        return redirect(url_for('signin'))
 
    user = models.User.query.filter_by(username = session['username']).first()
 
    if user is None:
        return redirect(url_for('signin'))
    else:
        return render_template('profile.html')
