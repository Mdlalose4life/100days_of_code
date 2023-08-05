#!/usr/bin/env python3
""" basic Flask app in 0-app.py
"""
from flask import Flask, render_template
from babel import numbers, dates
from datetime import datetime, time, date

app = Flask(__name__)

@app.route('/')
def hello_world():
    """
    Root route
    """
    d = date(2023, 9, 5)
    dt = datetime(2023, 8, 3, 21, 30)

    us_dates = dates.format_date(d, locale='en_US')
    de_dates = dates.format_date(d, locale='de_DE')
    us_datetime = dates.format_datetime(dt, locale='sv_SE')

    results ={'us_dates' : us_dates, 'de_dates' : de_dates,
              'us_datetime' : us_datetime}



    return render_template('1-index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)