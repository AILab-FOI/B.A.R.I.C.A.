from database import db
from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

class User(UserMixin):
    def __init__(self, id):
        self.id = id
        self.name = "name"+ str(id)
        self.password = self.name+"_secret"
    def __repr__( self ):
        return "%d/%s/%s" % ( self.id, self.name, self.password )

class DBUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.name) 