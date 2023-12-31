from . import db
from flask_login import UserMixin
from sqlalchemy.sql import func

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    name = db.Column(db.String(150))
    surname = db.Column(db.String(150))
    username = db.Column(db.String(150))
    password = db.Column(db.String(150))
    image = db.Column(db.String(300))
