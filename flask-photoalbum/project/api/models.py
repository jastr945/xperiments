import datetime

from project import db


class Album(db.Model):
    __tablename__ = "albums"
    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.Column(db.String(300), nullable=False)
    description = db.Column(db.String(1000), nullable=False)
    created_at = db.Column(db.DateTime(timezone=True), nullable=False)

    def __init__(self, title, description, created_at=None):
        if not created_at:
            created_at = datetime.datetime.now()
        self.title = title
        self.description = description
        self.created_at = created_at
