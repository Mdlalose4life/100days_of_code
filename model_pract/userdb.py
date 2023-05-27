from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kamva.db'
app.config['SECRET_KEY'] = 'secret_key'
db = SQLAlchemy(app)


class Users(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), unique=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)


# Create a string
def __repr__(self):
    return '<Name %r>' % self.first_name


with app.app_context():
    db.create_all()
