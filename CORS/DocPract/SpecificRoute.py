from flask import Flask
from flask_cors import CORS

app = Flask(__name__)
cors = CORS(app, resources={r"/api/*": {"origins": ["*"]}})


@app.route('/api/home')
@cors
def home():
    return "Test the cors"


"""Corse enabled to be active for all api/* routes"""
""""We continue with the code here"""
