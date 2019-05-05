from database import db
from flask import Flask
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

#------------------------------------------------------------------
#new type user - in use now
class DBUser(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(64), index=True, unique=True)
    password_hash = db.Column(db.String(128))
    #foreign key
    role_id = db.Column(db.Integer, db.ForeignKey('db_role.id')) #snake naming DBRole = db_role
    
    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    def check_password(self, password):
        return check_password_hash(self.password_hash, password)

    def __repr__(self):
        return '<User {}>'.format(self.name) 

#role table (connected to DBUser one-to-many)
class DBRole(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    role = db.Column(db.String(32), index=True, unique=True)
    #back reference - 
    user = db.relationship('DBUser', backref='role', lazy='dynamic')

    def __repr__(self):
        return '<Role {}>'.format(self.role)