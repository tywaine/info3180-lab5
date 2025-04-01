# Add any model classes for Flask-SQLAlchemy here
from datetime import datetime
from . import db


class Movie(db.Model):
    __tablename__ = 'movies'

    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(50))
    description = db.Column(db.Text)
    poster = db.Column(db.String(250), unique=True)
    created_at = db.Column(db.DateTime, default=datetime.now)

    def __init__(self, title, description, poster, created_at=None):
        self.title = title
        self.description = description
        self.poster = poster
        self.created_at = created_at if created_at else datetime.now()

    def get_id(self):
        try:
            return unicode(self.id)  # python 2 support
        except NameError:
            return str(self.id)  # python 3 support
