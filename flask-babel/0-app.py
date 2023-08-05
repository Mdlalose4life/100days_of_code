#!/usr/bin/env python3
""" basic Flask app in 0-app.py
"""
from flask import Flask, render_template
from babel import numbers

app = Flask(__name__)

@app.route('/')
def hello_world():
 
    """
    Root route
    """
    us_num = numbers.format_decimal(12345, locale='en_US')
    se_num = numbers.format_decimal(12345, locale='sv_SE')
    de_num = numbers.format_decimal(12345, locale='de_DE')
    results = {'us_num':us_num, 'se_num':se_num, 'de_num':de_num}
    return render_template('0-index.html', results=results)

if __name__ == '__main__':
    app.run(debug=True)