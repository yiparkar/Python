from flask import Flask

app = Flask(__name__)

@app.route('/')
def html_view():
    html = """
    <html>
        <h1>Welcome to the library</h1>
        {author_array}
    </html>
    """

    authors = ["Yogesh", "Chetana", "Suresh"]

    author_list = "<ul>"
    author_list += "\n".join([
        "<li>{author}</li>".format(author=author) for author in authors
    ])
    author_list += "</ul>"
    # print(author_list)

    return  html.format(author_array=author_list)