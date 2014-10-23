from app import db
from werkzeug import generate_password_hash, check_password_hash 

class User(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key = True)
    username = db.Column(db.String(64), unique = True)
    password = db.Column(db.String(120), unique = True)
     
    def __init__(self, username, password):
        self.username = username
        self.set_password(password)
     
    def set_password(self, password):
        self.password = generate_password_hash(password)
   
    def check_password(self, password):
        return check_password_hash(self.password, password)
    
    def __repr__(self):
        return '<User %r>' % (self.username)
