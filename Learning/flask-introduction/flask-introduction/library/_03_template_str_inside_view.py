from flask import Flask
from flask import render_template_string

app = Flask(__name__)

@app.route('/')
def hello_world():
    library_name = "Yogesh"
    authors = ["Yogesh", "Chetana", "Suresh"]
    html = """
        <html>
            <h1>Welcome to the {{libraryname}} library</h1>
            <ul>
            {% for author in authors %}
            <li>{{ author }} </li>
            {% endfor %}
            </ul>
        </html>
        """
    rendered_html = render_template_string(html, libraryname=library_name, authors= authors)
    return rendered_html