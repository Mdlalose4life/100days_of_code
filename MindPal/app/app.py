#!/usr/bin/python3
import os
from flask import Flask, render_template, redirect, flash, url_for
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from models import db, Conditions, Strategies

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'mindpal.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db.init_app(app)
migrate = Migrate(app, db)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    conditions = Conditions.query.all()
    strategies = {}
    for condition in conditions:
        strategies[condition.id] = condition.strategy
    return render_template('conditions.html', conditions=conditions, strategies=strategies)


@app.route('/strategy_details/<int:strategy_id>')
def strategy_details(strategy_id):
    strategy = Strategies.query.get(strategy_id)
    if strategy:
        return render_template('strategy_details.html', strategy=strategy)
    else:
        flash('Strtegy not found.', 'error')
        return redirect(url_for('home'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)
