""" 
Path    : models.py.py
Function:
coding  : utf-8
Version : V1.0
Time    : 2023/1/11 22:11
Author  : Walon Cyler
Modified: 
"""

from app import db

class Account(db.Model):
    __tablename__ = 'account'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    date = db.Column(db.DateTime, nullable=False)
    item = db.Column(db.String(100), nullable=False)
    spend = db.Column(db.Integer, nullable=False)
    categroy = db.Column(db.String(100), nullable=False)

class Article(db.Model):
    __tablename__ = 'article'
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(100), nullable=False)
    content = db.Column(db.Text, nullable=False)