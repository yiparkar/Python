from flask import Flask
from flask import render_template, abort

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

@app.route('/author/<string:authors_last_name>')
def author(authors_last_name):
    if authors_last_name not in AUTHORS_INFO:
        abort(404)
    return render_template('routing/author.html', author=AUTHORS_INFO[authors_last_name])

@app.route('/author/<string:authors_last_name>/edit')
def author_admin(authors_last_name):
    abort(401)

@app.errorhandler(404)
def not_found(error):
    return render_template('routing/404.html'), 404
