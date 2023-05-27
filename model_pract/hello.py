#!/usr/bin/python3
from flask import Flask, render_template, flash
from userdb import Users, db
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
# Secrete key
app.config['SECRET_KEY'] = 'secret_key'

# create a form class


class UserForm(FlaskForm):
    name = StringField("name", validators=[DataRequired()])
    email = StringField("email", validators=[DataRequired()])
    submit = SubmitField("submit")


class NameForm(FlaskForm):
    name = StringField("What's your name", validators=[DataRequired()])
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


@app.route('/user/add', methods=['GET', 'POST'])
def add_user():
    name = None
    form = UserForm()
    if form.validate_on_submit():
        user = Users.query.filter_by(email=form.email.data).first()
        if user is None:
            user = Users(name=form.name.data, email=form.email.data)
            db.session.add(user)
    return render_template("add_user.html", form=form)


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
