#!/usr/bin/python3
import os
from flask import Flask, render_template, redirect
from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

basedir = os.path.abspath(os.path.dirname(__file__))

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] =\
    'sqlite:///' + os.path.join(basedir, 'mindpal.db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

# routes


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/home')
def home():
    conditions = Conditions.query.all()
    return render_template('conditions.html', conditions=conditions)


@app.route('/strategy')
def strategy():
    pass

# Models


class User(db.Model):
    """
    This is the user Class
    Attributes
        email: user email address
        password: user password
        first_name: user first name
        last_name: user last name
        conditions: choices of conditions for the users
    """
    __tablename__ = 'users'
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=True,
                           default=datetime.utcnow())
    updated_on = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow())
    first_name = db.Column(db.String(128), nullable=False)
    last_name = db.Column(db.String(128), nullable=False)
    email = db.Column(db.String(128), nullable=False)
    password = db.Column(db.String(128), nullable=False)
    condition = db.relationship("Conditions", backref="users")

    def __repr__(self):
        return f'<Post "{self.first_name}"'


class Conditions(db.Model):
    """
    This class for conditions
    Attributes:
    condition_name : name
    Strategy_id : strategy_id
    user_id : user_id
    """
    __tablename__ = 'conditions'
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=True,
                           default=datetime.utcnow())
    updated_on = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow())
    condition_name = db.Column(db.String(128), nullable=False)
    strategy = db.relationship("Strategies", backref="conditions")
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))

    def __repr__(self):
        return f'<Post "{self.condition_name}"'


class Strategies(db.Model):
    """
    This is a Strategy class
    Attributes:
        stategy_name: the name of the strategy
        strategy_text: the text to a strategy
        youtube_id : The id of a youtube content
        spotify_id : The id of the spotify content
    """
    __tablename__ = 'strategies'
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=True,
                           default=datetime.utcnow())
    updated_on = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow())
    strategy_name = db.Column(db.String(255), nullable=False)
    strategy_text = db.Column(db.Text, nullable=False)
    condition_id = db.Column(db.Integer, db.ForeignKey(
        'conditions.id'))
    youtube_content = db.relationship("YoutubeContent", backref="strategies")
    spotify_content = db.relationship("SpotifyContent", backref="strategies")


class SpotifyContent(db.Model):
    """
    Spotify Content class
    Attributes:
    content_tittle: the title of the content
    podcast_id: the id of the podcast
    strategy_id: the id of the strategy to
    use the content for.
    """
    __tablename__ = 'spotifyContent'
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=True,
                           default=datetime.utcnow())
    updated_on = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow())
    podcast_title = db.Column(db.String(60), nullable=False)
    podcast_id = db.Column(db.String(60), nullable=False)
    strategy_id = db.Column(db.String(60), db.ForeignKey(
        "strategies.id"))


class YoutubeContent(db.Model):
    """
    The youtube content class  
    Atribute
    content_title = Tittle of the youtube content
    strategy = the strategy to use this content for.
    """
    __tablename__ = 'youtubeContent'
    id = db.Column(db.Integer, primary_key=True)
    created_on = db.Column(db.DateTime, nullable=True,
                           default=datetime.utcnow())
    updated_on = db.Column(db.DateTime, nullable=False,
                           default=datetime.utcnow())
    video_title = db.Column(db.String(60), nullable=False)
    video_url = db.Column(db.String(60), nullable=False)
    strategy_id = db.Column(db.String(60), db.ForeignKey("strategies.id"))


app.app_context().push()
if __name__ == '__main__':
    app.run(debug=True)
