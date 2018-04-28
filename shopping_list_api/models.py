from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash
from flask_login import UserMixin

db = SQLAlchemy()


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(300), nullable=False)
    note = db.Column(db.String(1000), nullable=True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __init__(self, title, note):
        self.title = title
        self.note = note


class User(db.Model, UserMixin):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False, unique=True)
    password_hash = db.Column(db.String(100), nullable=False)
    items = db.relationship('Item', backref=db.backref('items', lazy=True))

    def hash_password(self, password):
        self.password_hash = generate_password_hash(password)

    def verify_password(self, password):
        return check_password_hash(self.password_hash, password)
