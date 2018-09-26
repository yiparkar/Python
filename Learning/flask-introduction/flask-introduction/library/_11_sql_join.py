import sqlite3
from flask import Flask, g, render_template
from . import config

app = Flask(__name__)


def connect_db():
    return sqlite3.connect(config.DATABASE_NAME)

@app.before_request
def before_request():
    g.db = connect_db()

@app.route('/')
def hello_world():
    cursor = g.db.execute('Select au.id,au.name,co.name from Author au INNER JOIN Country co ON au.country_id= co.Id;')
    authors = [dict(id=row[0], name=row[1], country=row[2]) for row in cursor.fetchall()]
    return render_template('database/authors_template_country_sql_join.html',authors=authors)

