import datetime
import pytz

from project import db


my_timezone = pytz.timezone("US/Pacific")
created_at=datetime.datetime.now(my_timezone)
print(created_at)


class User(db.Model):
    __tablename__ = "users"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    username = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    active = db.Column(db.Boolean(), default=False, nullable=False)
    created_at = db.Column(db.DateTime, nullable=False)

    def __init__(self, username, email, created_at=datetime.datetime.now(my_timezone)):
        self.username = username
        self.email = email
        self.created_at = created_at
