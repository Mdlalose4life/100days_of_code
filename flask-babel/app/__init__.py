#!/usr/bin/env python
"""
"""
from flask_babel import flask_babel
from flask import request
from flask_babel import _

app = Flask(__name__)


babel = Babe(app)

@babel.localeselector
def get_local():
    return request.accept_languages.best_match(app.config['LANGUAGES'])

   