#!/usr/bin/python3
from flask import Flask, render_template, flash
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime
from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired

# FILTERS
# safe
# capitalize
# lower
# upper
# tittle
# trim
# striptags

# Create an instance of a application
app = Flask(__name__)
# add database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///kamva.db'
# Secrete key
app.config['SECRET_KEY'] = 'secret_key'
# Initialize the database
db = SQLAlchemy(app)

# Create the model


class Users(db.Model):
    id = db.Column(db.Integer,  primary_key=True)
    first_name = db.Column(db.String(60), nullable=False)
    last_name = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(100), unique=True)
    created_on = db.Column(db.DateTime, default=datetime.utcnow)

# Create a string


def __repr__(self):
    return '<Name %r' % self.first_name

# create a form class


class UserForm(FlaskForm):
    name = StringField("What's you name", validators=[DataRequired()])
    submit = SubmitField("submit")

# create name page


@app.route('/name', methods=['GET', 'POST'])
def name():
    name = None
    form = UserForm()
    # Validators
    if form.validate_on_submit():
        name = form.name.data
        form.name.data = ''
        flash("the form submitted successfully")
    return render_template("name.html", name=name, form=form)


@app.route('/user', methods=['GET'])
def user():
    favourite_cars = ['Toyota Hillux',
                      'BMW x6',
                      'Audi Q7',
                      'Potch Kayena',
                      'Toyota Land Cruzer',
                      10]
    return render_template('user.html', favourite_cars=favourite_cars)


@app.route('/users/<name>')
def UserName(name):
    return render_template('UserName.html', name=name)

# Create the error pages
# invalid URL


@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html"), 404

# invalid URL


@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html"), 500


if __name__ == '__main__':
    app.run(debug=True)
