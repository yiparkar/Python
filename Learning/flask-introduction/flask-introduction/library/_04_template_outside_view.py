from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route('/')
def hello_world():
    library_name = "Yogesh"
    return render_template("index.html",library_name=library_name)