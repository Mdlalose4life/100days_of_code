from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

db = SQLAlchemy()


class Users(db.Model):
    __tablename__ = 'users'
    id = db.Column(db.Integer,  primary_key=True)
    name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), unique=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)


# Create a string
def __repr__(self):
    return '<Name %r>' % self.name
