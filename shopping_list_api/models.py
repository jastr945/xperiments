from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


class Item(db.Model):
    __tablename__ = "items"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(300), nullable=False)
    note = db.Column(db.String(1000), nullable=True)

    def __init__(self, title, note):
        self.title = title
        self.note = note


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(100), nullable=False)
    password_hash = db.Column(db.String(100), nullable=False)

    def __init__(self, name, password_hash):
        self.name = name
        self.password_hash = password_hash
