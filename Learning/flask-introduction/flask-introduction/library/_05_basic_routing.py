from flask import Flask
from flask import render_template

app = Flask(__name__)


AUTHORS_INFO = {
    'iparkar': {
        'full_name':'Yogesh iparkar',
        'nationality': 'Indian',
        'born': '1984',
        'work': 'Software'
    },
    'burkule': {
        'full_name':'Suresh Burkule',
        'nationality': 'Indian',
        'born': '1950',
        'work': 'Marketing'
    }
}

@app.route('/')
def authors():
    return render_template('routing/authors.html')

@app.route('/author/<authors_last_name>')
def author(authors_last_name):
    return render_template('routing/author.html', author=AUTHORS_INFO[authors_last_name])