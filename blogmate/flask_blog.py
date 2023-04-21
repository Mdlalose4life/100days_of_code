from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author': 'Sbusiso Mdlalose',
        'title': 'long day',
        'content': 'nightmere tea',
        'date_posted': '21 April 2022'
    },
    {
        'author': 'Senzo Nzima',
        'title': 'off the stage',
        'content': 'single dance song',
        'date_posted': '24 April 2022'
    },
        {
        'author': 'Sbonga Qwabe',
        'title': 'writting night',
        'content': 'Empty Pen',
        'date_posted': '28 April 2022'
    }
]

@app.route("/")
@app.route("/home")
def hello():
    return render_template('home.html', posts=posts)

@app.route("/about")
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)