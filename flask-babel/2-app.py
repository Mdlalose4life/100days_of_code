#!/usr/bin/env python3
""" basic Flask app in 0-app.py
"""
from flask import Flask, render_template, request
from babel import numbers, dates
from datetime import datetime, time, date
from flask_babel import Babel, format_date, gettext

app = Flask(__name__)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
babel = Babel(app)


@babel.localeselector
def get_locale():
    return 'en'
    #request.accept_languages.best_match(['en', 'es', 'de'])

@app.route('/')
def hello_world():
    """
    Root route
    """

    blessing = gettext('Blessing')

    d = date(2023, 3, 23)

    us_dates = format_date(d)

    results = {'us_dates' : us_dates}
    return render_template('2-index.html', results=results,
                           blessing=blessing)

if __name__ == '__main__':
    app.run(debug=True)