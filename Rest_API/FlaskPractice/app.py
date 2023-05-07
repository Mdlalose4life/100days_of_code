from flask import Flask

app = Flask(__name__)


@app.route('/')
def index():
    """The introduction Basic App"""
    return "I am a Basic flask Application"


@app.route('/<name>')
def greet_name(name):
    """Greet the pesrson"""
    return 'Hello, {}'.format(name)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port='5000')
